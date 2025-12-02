"""
Utility functions for URL building and User-Agent detection.
"""

import re
from typing import Optional
from urllib.parse import quote

from app.config import settings


def build_wa_me_url(phone: str, text: Optional[str] = None) -> str:
    """
    Build a wa.me URL for WhatsApp deep linking.

    Args:
        phone: WhatsApp number in E.164 format without '+', e.g., '9198XXXXXXX'
        text: Optional prefilled message text

    Returns:
        Full wa.me URL, e.g., 'https://wa.me/9198XXXXXXX?text=Hi%20Tal'
    """
    # Clean phone number - remove any non-digit characters
    clean_phone = re.sub(r"\D", "", phone)

    url = f"https://wa.me/{clean_phone}"
    if text:
        url += f"?text={quote(text)}"
    return url


def validate_phone(phone: str) -> tuple[bool, str]:
    """
    Validate phone number format.

    Args:
        phone: Phone number string to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Remove any non-digit characters for validation
    clean_phone = re.sub(r"\D", "", phone)

    if not clean_phone:
        return False, "Phone number is required"

    if len(clean_phone) < settings.phone_min_length:
        return False, f"Phone number must be at least {settings.phone_min_length} digits"

    if len(clean_phone) > settings.phone_max_length:
        return False, f"Phone number must be at most {settings.phone_max_length} digits"

    if not clean_phone.isdigit():
        return False, "Phone number must contain only digits"

    return True, ""


# =============================================================================
# User-Agent Detection
# =============================================================================

def is_android(ua: str) -> bool:
    """Check if User-Agent indicates an Android device."""
    return "android" in ua.lower()


def is_ios(ua: str) -> bool:
    """Check if User-Agent indicates an iOS device (iPhone/iPad)."""
    ua_lower = ua.lower()
    return "iphone" in ua_lower or "ipad" in ua_lower or "ipod" in ua_lower


def is_linkedin_webview(ua: str) -> bool:
    """
    Check if User-Agent indicates LinkedIn's in-app browser.

    LinkedIn webview typically contains 'LinkedIn' in the UA string.
    Some versions also include 'LinkedInApp'.
    """
    ua_lower = ua.lower()
    return "linkedin" in ua_lower or "linkedinapp" in ua_lower


def is_twitter_webview(ua: str) -> bool:
    """
    Check if User-Agent indicates Twitter/X's in-app browser.

    Twitter webview typically contains 'Twitter' or 'X-Client' in the UA.
    """
    ua_lower = ua.lower()
    return "twitter" in ua_lower or "x-client" in ua_lower


def is_facebook_webview(ua: str) -> bool:
    """
    Check if User-Agent indicates Facebook's in-app browser.

    Facebook webview typically contains 'FBAN' or 'FBAV' in the UA.
    """
    ua_lower = ua.lower()
    return "fban" in ua_lower or "fbav" in ua_lower or "fb_iab" in ua_lower


def is_instagram_webview(ua: str) -> bool:
    """
    Check if User-Agent indicates Instagram's in-app browser.

    Instagram webview typically contains 'Instagram' in the UA.
    """
    return "instagram" in ua.lower()


def is_desktop(ua: str) -> bool:
    """
    Check if User-Agent indicates a desktop browser.

    Heuristic: contains 'macintosh', 'windows', or 'linux' (non-Android)
    and is not a mobile device.
    """
    ua_lower = ua.lower()
    is_mac = "macintosh" in ua_lower
    is_win = "windows" in ua_lower
    is_linux_desktop = "linux" in ua_lower and not is_android(ua)

    return (is_mac or is_win or is_linux_desktop) and not is_android(ua) and not is_ios(ua)


def is_webview(ua: str) -> bool:
    """Check if User-Agent indicates any known in-app webview."""
    return (
        is_linkedin_webview(ua)
        or is_twitter_webview(ua)
        or is_facebook_webview(ua)
        or is_instagram_webview(ua)
    )


def get_webview_source(ua: str) -> Optional[str]:
    """
    Get the source of the webview if detected.

    Returns:
        String identifier of the webview source, or None if not a known webview.
    """
    if is_linkedin_webview(ua):
        return "linkedin"
    if is_twitter_webview(ua):
        return "twitter"
    if is_facebook_webview(ua):
        return "facebook"
    if is_instagram_webview(ua):
        return "instagram"
    return None


def get_device_type(ua: str) -> str:
    """
    Get the device type from User-Agent.

    Returns:
        One of: 'android', 'ios', 'desktop', 'unknown'
    """
    if is_android(ua):
        return "android"
    if is_ios(ua):
        return "ios"
    if is_desktop(ua):
        return "desktop"
    return "unknown"


def get_env_type(ua: str) -> str:
    """
    Determine the full environment type from User-Agent for logging.

    Returns a human-readable string describing the detected environment.
    Example: 'android_linkedin_webview', 'ios', 'desktop'
    """
    device = get_device_type(ua)
    webview = get_webview_source(ua)

    if webview:
        return f"{device}_{webview}_webview"
    return device


def is_risky_environment(ua: str) -> bool:
    """
    Determine if the environment is considered 'risky' for direct redirects.

    Risky environments are those where direct wa.me redirects may not work
    reliably, typically Android devices in social media webviews.

    iOS is generally safe because Apple's Universal Links handle wa.me well.
    Desktop is safe because browsers handle the redirect properly.
    Android in a regular browser is safe.
    Android in a social media webview (LinkedIn, Twitter, FB, IG) is risky.
    """
    # Only Android webviews are considered risky
    # iOS handles wa.me links well even in webviews
    return is_android(ua) and is_webview(ua)
