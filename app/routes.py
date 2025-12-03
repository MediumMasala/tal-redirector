"""
API routes for the Tal Redirector service.
"""

from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from app import __version__
from app.config import settings
from app.logging_config import get_logger
from app.templates import ERROR_PAGE_TEMPLATE, FALLBACK_PAGE_TEMPLATE, CHROME_INTENT_TEMPLATE, CHROME_OPEN_TEMPLATE, AUTO_COPY_TEMPLATE, ULTIMATE_TEMPLATE, LINKEDIN_TEMPLATE, CHROME_ESCAPE_TEMPLATE, META_REFRESH_TEMPLATE
from app.utils import (
    build_wa_me_url,
    get_device_type,
    get_env_type,
    get_webview_source,
    is_android,
    is_desktop,
    is_ios,
    is_risky_environment,
    validate_phone,
)

logger = get_logger("routes")

router = APIRouter()


# =============================================================================
# Health & Status Endpoints
# =============================================================================


@router.get("/", tags=["Health"])
async def health_check():
    """
    Health check endpoint.

    Returns service status and basic info.
    """
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": __version__,
        "environment": settings.environment,
    }


@router.get("/health", tags=["Health"])
async def detailed_health():
    """
    Detailed health check endpoint.

    Returns comprehensive service health information.
    """
    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": __version__,
        "environment": settings.environment,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "checks": {
            "config_loaded": True,
            "logging_enabled": settings.enable_request_logging,
            "metrics_enabled": settings.enable_metrics,
        },
    }


# =============================================================================
# Main Redirect Endpoint
# =============================================================================


@router.get("/w", tags=["Redirect"])
async def whatsapp_redirect(
    request: Request,
    phone: str = Query(
        ...,
        description="WhatsApp number in E.164 format without '+' (e.g., 9198XXXXXXXX)",
        min_length=10,
        max_length=15,
    ),
    text: Optional[str] = Query(
        None,
        description="Prefilled WhatsApp message",
        max_length=1000,
    ),
    src: Optional[str] = Query(
        None,
        description="Traffic source (e.g., 'linkedin_ad', 'twitter', 'email')",
        max_length=50,
    ),
    campaign: Optional[str] = Query(
        None,
        description="Campaign identifier",
        max_length=100,
    ),
    ad_id: Optional[str] = Query(
        None,
        description="Ad identifier",
        max_length=100,
    ),
    debug: int = Query(
        0,
        description="Set to 1 to force showing the fallback HTML page",
        ge=0,
        le=1,
    ),
):
    """
    Main WhatsApp redirect endpoint.

    Intelligently redirects users to WhatsApp chat:
    - Direct 302 redirect for safe environments (iOS, desktop, Android browser)
    - Fallback HTML page for risky environments (Android webviews)

    The fallback page includes:
    - Auto-redirect attempt via JavaScript
    - Manual "Open WhatsApp" button
    - Instructions to open in browser
    - Copyable link as last resort
    """
    # Get request context
    request_id = getattr(request.state, "request_id", "unknown")
    user_agent = request.headers.get("user-agent", "")
    client_ip = request.client.host if request.client else None

    # Validate phone number
    is_valid, error_msg = validate_phone(phone)
    if not is_valid:
        logger.warning(
            "Invalid phone number",
            extra={
                "request_id": request_id,
                "phone": phone,
                "error": error_msg,
            },
        )
        html = ERROR_PAGE_TEMPLATE.format(
            error_message="The phone number provided is invalid. Please check the link and try again.",
            error_code="INVALID_PHONE",
        )
        return HTMLResponse(content=html, status_code=400)

    # Build WhatsApp URL
    wa_url = build_wa_me_url(phone, text)

    # Environment detection
    device_type = get_device_type(user_agent)
    webview_source = get_webview_source(user_agent)
    env_type = get_env_type(user_agent)
    is_risky = is_risky_environment(user_agent)

    # Log the redirect request
    log_extra = {
        "request_id": request_id,
        "phone": phone[:4] + "****" + phone[-2:] if len(phone) > 6 else "****",  # Mask phone
        "text": text[:50] if text else None,
        "src": src,
        "campaign": campaign,
        "ad_id": ad_id,
        "device_type": device_type,
        "webview_source": webview_source,
        "env_type": env_type,
        "is_risky": is_risky,
        "debug_mode": debug == 1,
        "client_ip": client_ip,
    }

    logger.info("Redirect request received", extra=log_extra)

    # Always direct redirect - no intermediary pages
    logger.info(
        "Direct redirect",
        extra={"request_id": request_id, "env_type": env_type},
    )
    return RedirectResponse(url=wa_url, status_code=302)


# =============================================================================
# Chrome Intent Route (for Android webviews)
# =============================================================================


@router.get("/wc", tags=["Redirect"])
async def whatsapp_chrome_redirect(
    request: Request,
    phone: str = Query(
        ...,
        description="WhatsApp number in E.164 format without '+' (e.g., 9198XXXXXXXX)",
        min_length=10,
        max_length=15,
    ),
    text: Optional[str] = Query(
        None,
        description="Prefilled WhatsApp message",
        max_length=1000,
    ),
    src: Optional[str] = Query(
        None,
        description="Traffic source (e.g., 'linkedin_ad', 'twitter', 'email')",
        max_length=50,
    ),
    campaign: Optional[str] = Query(
        None,
        description="Campaign identifier",
        max_length=100,
    ),
    ad_id: Optional[str] = Query(
        None,
        description="Ad identifier",
        max_length=100,
    ),
):
    """
    WhatsApp redirect using Chrome intent for Android.

    This route attempts to open Chrome browser on Android devices,
    which can then properly handle WhatsApp links even from webviews
    like LinkedIn's in-app browser.

    On non-Android devices, redirects directly to wa.me.
    """
    import re

    # Get request context
    request_id = getattr(request.state, "request_id", "unknown")
    user_agent = request.headers.get("user-agent", "")
    client_ip = request.client.host if request.client else None

    # Validate phone number
    is_valid, error_msg = validate_phone(phone)
    if not is_valid:
        logger.warning(
            "Invalid phone number",
            extra={
                "request_id": request_id,
                "phone": phone,
                "error": error_msg,
            },
        )
        html = ERROR_PAGE_TEMPLATE.format(
            error_message="The phone number provided is invalid. Please check the link and try again.",
            error_code="INVALID_PHONE",
        )
        return HTMLResponse(content=html, status_code=400)

    # Build WhatsApp URL
    wa_url = build_wa_me_url(phone, text)
    clean_phone = re.sub(r"\D", "", phone)

    # Environment detection
    device_type = get_device_type(user_agent)
    env_type = get_env_type(user_agent)

    # Log the redirect request
    logger.info(
        "Chrome intent redirect request",
        extra={
            "request_id": request_id,
            "phone": phone[:4] + "****" + phone[-2:] if len(phone) > 6 else "****",
            "text": text[:50] if text else None,
            "src": src,
            "campaign": campaign,
            "ad_id": ad_id,
            "device_type": device_type,
            "env_type": env_type,
            "client_ip": client_ip,
            "route": "/wc",
        },
    )

    # For non-Android, just redirect to wa.me
    if not is_android(user_agent):
        logger.info(
            "Non-Android device - direct redirect",
            extra={"request_id": request_id, "device_type": device_type},
        )
        return RedirectResponse(url=wa_url, status_code=302)

    # For Android, show Chrome intent page
    logger.info(
        "Android device - showing Chrome intent page",
        extra={"request_id": request_id, "env_type": env_type},
    )
    html = CHROME_INTENT_TEMPLATE.format(
        wa_url=wa_url,
        phone=clean_phone,
        text=text or "",
    )
    return HTMLResponse(content=html, status_code=200)


# =============================================================================
# Simple Chrome Opener Route
# =============================================================================


@router.get("/c", tags=["Redirect"])
async def chrome_redirect(
    request: Request,
    phone: str = Query(..., min_length=10, max_length=15),
    text: Optional[str] = Query(None, max_length=1000),
    src: Optional[str] = Query(None, max_length=50),
    campaign: Optional[str] = Query(None, max_length=100),
    ad_id: Optional[str] = Query(None, max_length=100),
):
    """
    Simple Chrome opener for Android.

    Uses meta refresh + JavaScript + iframe to aggressively try to open Chrome.
    On non-Android, redirects directly to wa.me.
    """
    import re
    from urllib.parse import quote

    user_agent = request.headers.get("user-agent", "")

    # Validate phone
    is_valid, error_msg = validate_phone(phone)
    if not is_valid:
        html = ERROR_PAGE_TEMPLATE.format(
            error_message="Invalid phone number.",
            error_code="INVALID_PHONE",
        )
        return HTMLResponse(content=html, status_code=400)

    # Build URLs
    clean_phone = re.sub(r"\D", "", phone)
    wa_url = build_wa_me_url(phone, text)

    # Chrome intent URL - opens wa.me URL in Chrome
    chrome_intent_url = f"intent://wa.me/{clean_phone}"
    if text:
        chrome_intent_url += f"?text={quote(text)}"
    chrome_intent_url += f"#Intent;scheme=https;package=com.android.chrome;S.browser_fallback_url={quote(wa_url)};end"

    # Log
    logger.info(
        "Chrome opener request",
        extra={
            "phone": clean_phone[:4] + "****",
            "src": src,
            "campaign": campaign,
            "route": "/c",
        },
    )

    # Non-Android: direct redirect
    if not is_android(user_agent):
        return RedirectResponse(url=wa_url, status_code=302)

    # Android: show Chrome opener page
    html = CHROME_OPEN_TEMPLATE.format(
        chrome_intent_url=chrome_intent_url,
        wa_url=wa_url,
    )
    return HTMLResponse(content=html, status_code=200)


# =============================================================================
# Auto-Copy Route
# =============================================================================


@router.get("/a", tags=["Redirect"])
async def auto_copy_redirect(
    request: Request,
    phone: str = Query(..., min_length=10, max_length=15),
    text: Optional[str] = Query(None, max_length=1000),
    src: Optional[str] = Query(None, max_length=50),
    campaign: Optional[str] = Query(None, max_length=100),
    ad_id: Optional[str] = Query(None, max_length=100),
):
    """
    Auto-copy route for LinkedIn Android.

    Automatically copies the WhatsApp link to clipboard on page load.
    User just needs to open Chrome and paste.

    On non-Android/non-webview, redirects directly to wa.me.
    """
    import re

    user_agent = request.headers.get("user-agent", "")

    # Validate phone
    is_valid, error_msg = validate_phone(phone)
    if not is_valid:
        html = ERROR_PAGE_TEMPLATE.format(
            error_message="Invalid phone number.",
            error_code="INVALID_PHONE",
        )
        return HTMLResponse(content=html, status_code=400)

    # Build URL
    wa_url = build_wa_me_url(phone, text)

    # Log
    logger.info(
        "Auto-copy request",
        extra={
            "phone": phone[:4] + "****" if len(phone) > 4 else "****",
            "src": src,
            "campaign": campaign,
            "route": "/a",
        },
    )

    # Safe environment: direct redirect
    if not is_risky_environment(user_agent):
        return RedirectResponse(url=wa_url, status_code=302)

    # Risky environment: show auto-copy page
    html = AUTO_COPY_TEMPLATE.format(wa_url=wa_url)
    return HTMLResponse(content=html, status_code=200)


# =============================================================================
# Ultimate Route - Everything + QR Code
# =============================================================================


@router.get("/u", tags=["Redirect"])
async def ultimate_redirect(
    request: Request,
    phone: str = Query(..., min_length=10, max_length=15),
    text: Optional[str] = Query(None, max_length=1000),
    src: Optional[str] = Query(None, max_length=50),
    campaign: Optional[str] = Query(None, max_length=100),
    ad_id: Optional[str] = Query(None, max_length=100),
):
    """
    Ultimate route - tries everything + shows QR code.

    - Auto-copies link to clipboard
    - Tries all WhatsApp URL schemes
    - Shows QR code for camera scan
    - Copy and Share buttons
    - Clear instructions

    On safe environments, redirects directly.
    """
    import re
    from urllib.parse import quote

    user_agent = request.headers.get("user-agent", "")

    # Validate
    is_valid, _ = validate_phone(phone)
    if not is_valid:
        return HTMLResponse(
            ERROR_PAGE_TEMPLATE.format(error_message="Invalid phone", error_code="INVALID"),
            status_code=400
        )

    # Build URLs
    clean_phone = re.sub(r"\D", "", phone)
    wa_url = build_wa_me_url(phone, text)
    wa_url_encoded = quote(wa_url, safe='')
    text_encoded = quote(text or '', safe='')

    # Log
    logger.info("Ultimate redirect", extra={"phone": clean_phone[:4] + "****", "src": src, "route": "/u"})

    # Safe: direct redirect
    if not is_risky_environment(user_agent):
        return RedirectResponse(url=wa_url, status_code=302)

    # Risky: show ultimate page
    html = ULTIMATE_TEMPLATE.format(
        wa_url=wa_url,
        wa_url_encoded=wa_url_encoded,
        phone=clean_phone,
        text_encoded=text_encoded,
    )
    return HTMLResponse(content=html, status_code=200)


# =============================================================================
# LinkedIn-Optimized Route
# =============================================================================


@router.get("/l", tags=["Redirect"])
async def linkedin_redirect(
    request: Request,
    phone: str = Query(..., min_length=10, max_length=15),
    text: Optional[str] = Query(None, max_length=1000),
    src: Optional[str] = Query(None, max_length=50),
    campaign: Optional[str] = Query(None, max_length=100),
    ad_id: Optional[str] = Query(None, max_length=100),
):
    """
    LinkedIn redirect route - direct redirect to WhatsApp.

    LinkedIn's WebView will block this, showing a "Retry" button.
    When user taps Retry, LinkedIn opens Chrome where the redirect works.
    This preserves the full deep link context (phone + message).
    """
    # Validate phone
    is_valid, error_msg = validate_phone(phone)
    if not is_valid:
        html = ERROR_PAGE_TEMPLATE.format(
            error_message="Invalid phone number.",
            error_code="INVALID_PHONE",
        )
        return HTMLResponse(content=html, status_code=400)

    # Build WhatsApp URL
    wa_url = build_wa_me_url(phone, text)

    # Log
    logger.info(
        "LinkedIn redirect - direct to WhatsApp (Retry flow)",
        extra={
            "phone": phone[:4] + "****" if len(phone) > 4 else "****",
            "src": src,
            "campaign": campaign,
            "route": "/l",
            "redirect_to": "wa.me",
        },
    )

    # Direct redirect - LinkedIn blocks, user taps Retry, Chrome opens, WhatsApp works
    return RedirectResponse(url=wa_url, status_code=302)


# =============================================================================
# Meta-Refresh Route (Generic Browser Intent)
# =============================================================================


@router.get("/m", tags=["Redirect"])
async def meta_refresh_redirect(
    request: Request,
    phone: str = Query(..., min_length=10, max_length=15),
    text: Optional[str] = Query(None, max_length=1000),
    src: Optional[str] = Query(None, max_length=50),
    campaign: Optional[str] = Query(None, max_length=100),
    ad_id: Optional[str] = Query(None, max_length=100),
):
    """
    Meta-refresh route using generic browser intent.

    Uses intent:// with scheme=https and action=android.intent.action.VIEW
    WITHOUT specifying a package. This asks Android to open the URL in
    the default browser, potentially bypassing WebView restrictions.

    On non-Android, redirects directly to wa.me.
    """
    import re
    from urllib.parse import quote

    user_agent = request.headers.get("user-agent", "")

    # Validate phone
    is_valid, error_msg = validate_phone(phone)
    if not is_valid:
        html = ERROR_PAGE_TEMPLATE.format(
            error_message="Invalid phone number.",
            error_code="INVALID_PHONE",
        )
        return HTMLResponse(content=html, status_code=400)

    # Build URLs
    clean_phone = re.sub(r"\D", "", phone)
    wa_url = build_wa_me_url(phone, text)
    text_encoded = quote(text or "", safe="")

    # Log
    logger.info(
        "Meta-refresh redirect request",
        extra={
            "phone": clean_phone[:4] + "****" if len(clean_phone) > 4 else "****",
            "src": src,
            "campaign": campaign,
            "route": "/m",
        },
    )

    # Non-Android: direct redirect
    if not is_android(user_agent):
        return RedirectResponse(url=wa_url, status_code=302)

    # Android: show meta-refresh page with generic browser intent
    html = META_REFRESH_TEMPLATE.format(
        wa_host="wa.me",
        phone=clean_phone,
        text_encoded=text_encoded,
        wa_url=wa_url,
    )
    return HTMLResponse(content=html, status_code=200)


# =============================================================================
# Debug/Test Endpoints (only in non-production)
# =============================================================================


@router.get("/debug/ua", tags=["Debug"])
async def debug_user_agent(request: Request):
    """
    Debug endpoint to inspect User-Agent detection.

    Only available in non-production environments.
    """
    if settings.environment == "production":
        return {"error": "Not available in production"}

    user_agent = request.headers.get("user-agent", "")

    return {
        "user_agent": user_agent,
        "detection": {
            "device_type": get_device_type(user_agent),
            "is_android": is_android(user_agent),
            "is_ios": is_ios(user_agent),
            "is_desktop": is_desktop(user_agent),
            "webview_source": get_webview_source(user_agent),
            "env_type": get_env_type(user_agent),
            "is_risky": is_risky_environment(user_agent),
        },
    }
