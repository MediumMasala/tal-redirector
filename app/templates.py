"""
HTML templates for fallback pages.

All templates use inline CSS/JS to avoid external dependencies.
"""

FALLBACK_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="robots" content="noindex, nofollow">
    <meta name="theme-color" content="#1a1a2e">
    <title>Open Tal on WhatsApp</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #eee;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            -webkit-font-smoothing: antialiased;
        }}

        .card {{
            background: rgba(22, 33, 62, 0.95);
            border-radius: 20px;
            padding: 32px 24px;
            max-width: 400px;
            width: 100%;
            text-align: center;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
        }}

        .logo {{
            width: 56px;
            height: 56px;
            margin: 0 auto 16px;
            background: #25D366;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .logo svg {{
            width: 32px;
            height: 32px;
            fill: white;
        }}

        h1 {{
            font-size: 1.4rem;
            margin-bottom: 8px;
            color: #fff;
            font-weight: 600;
        }}

        .subtitle {{
            color: #9ca3af;
            font-size: 0.9rem;
            line-height: 1.5;
            margin-bottom: 24px;
        }}

        /* LinkedIn Warning Banner - shown only on LinkedIn Android */
        .linkedin-warning {{
            display: none;
            background: linear-gradient(135deg, #0077B5 0%, #005885 100%);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 20px;
            text-align: left;
        }}

        .linkedin-warning.show {{
            display: block;
        }}

        .linkedin-warning-title {{
            font-size: 0.95rem;
            font-weight: 600;
            color: #fff;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .linkedin-warning-steps {{
            color: rgba(255,255,255,0.95);
            font-size: 0.85rem;
            line-height: 1.8;
        }}

        .linkedin-warning-steps ol {{
            padding-left: 20px;
            margin: 0;
        }}

        .linkedin-warning-steps li {{
            margin-bottom: 4px;
        }}

        .linkedin-warning-steps strong {{
            color: #fff;
        }}

        .step-number {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 22px;
            height: 22px;
            background: rgba(255,255,255,0.2);
            border-radius: 50%;
            font-size: 0.75rem;
            font-weight: 600;
            margin-right: 8px;
        }}

        .menu-icon {{
            display: inline-block;
            font-weight: bold;
            background: rgba(255,255,255,0.2);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 1.1rem;
        }}

        /* Primary CTA */
        .cta-button {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 16px 24px;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            color: #fff;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 12px;
            text-decoration: none;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        }}

        .cta-button:hover {{
            transform: translateY(-1px);
        }}

        .cta-button:active {{
            transform: translateY(0);
        }}

        .cta-button svg {{
            width: 22px;
            height: 22px;
            fill: white;
        }}

        /* Secondary buttons row */
        .secondary-buttons {{
            display: flex;
            gap: 10px;
            margin-top: 12px;
        }}

        .secondary-btn {{
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            padding: 12px 16px;
            background: #374151;
            color: #fff;
            font-size: 0.85rem;
            font-weight: 500;
            border: none;
            border-radius: 10px;
            text-decoration: none;
            cursor: pointer;
            transition: background 0.2s;
        }}

        .secondary-btn:hover {{
            background: #4b5563;
        }}

        .secondary-btn.copied {{
            background: #25D366;
        }}

        .secondary-btn svg {{
            width: 18px;
            height: 18px;
            fill: currentColor;
        }}

        /* Status message */
        .status-msg {{
            font-size: 0.8rem;
            color: #25D366;
            margin-top: 12px;
            min-height: 1.2em;
        }}

        /* Divider */
        .divider {{
            display: flex;
            align-items: center;
            margin: 24px 0 20px;
            color: #4b5563;
            font-size: 0.75rem;
        }}

        .divider::before,
        .divider::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: #2a2a4a;
        }}

        .divider span {{
            padding: 0 12px;
        }}

        /* Instructions for non-LinkedIn users */
        .instructions {{
            text-align: left;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
            padding: 14px 16px;
        }}

        .instructions-title {{
            font-size: 0.8rem;
            color: #9ca3af;
            margin-bottom: 10px;
            font-weight: 500;
        }}

        .instructions ol {{
            color: #d1d5db;
            font-size: 0.8rem;
            line-height: 1.8;
            padding-left: 18px;
        }}

        .instructions strong {{
            color: #fff;
        }}

        /* Footer */
        .footer {{
            margin-top: 20px;
            padding-top: 16px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            font-size: 0.7rem;
            color: #4b5563;
        }}

        /* Hide non-LinkedIn instructions when LinkedIn warning is shown */
        .linkedin-detected .instructions {{
            display: none;
        }}

        @media (max-width: 360px) {{
            .card {{
                padding: 24px 18px;
            }}
            .secondary-buttons {{
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>
    <div class="card" id="card">
        <div class="logo">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
        </div>

        <h1>Chat with Tal on WhatsApp</h1>
        <p class="subtitle" id="subtitle">Tap the button below to start chatting</p>

        <!-- LinkedIn Android Warning - Shown prominently -->
        <div class="linkedin-warning" id="linkedinWarning">
            <div class="linkedin-warning-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>
                LinkedIn's browser can't open apps
            </div>
            <div class="linkedin-warning-steps">
                <ol>
                    <li>Tap <span class="menu-icon">⋮</span> in the <strong>top-right</strong></li>
                    <li>Select <strong>"Open in browser"</strong></li>
                    <li>WhatsApp will open automatically!</li>
                </ol>
            </div>
        </div>

        <a href="{wa_url}" class="cta-button" id="openBtn">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
            Open WhatsApp
        </a>

        <div class="secondary-buttons">
            <button class="secondary-btn" id="copyBtn">
                <svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
                <span id="copyText">Copy Link</span>
            </button>
            <button class="secondary-btn" id="shareBtn" style="display:none;">
                <svg viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92s2.92-1.31 2.92-2.92-1.31-2.92-2.92-2.92z"/></svg>
                Share
            </button>
        </div>

        <p class="status-msg" id="statusMsg"></p>

        <div class="divider"><span>still not working?</span></div>

        <div class="instructions" id="instructions">
            <p class="instructions-title">Open this page in your browser:</p>
            <ol>
                <li>Tap <strong>⋮</strong> menu (top-right corner)</li>
                <li>Select <strong>"Open in browser"</strong></li>
                <li>Then tap the green button</li>
            </ol>
        </div>

        <div class="footer">
            Powered by Tal
        </div>
    </div>

    <script>
        (function() {{
            'use strict';

            // Config
            var phone = "{phone}";
            var text = "{text}";
            var waUrl = "{wa_url}";

            // Build URLs
            var apiUrl = "https://api.whatsapp.com/send?phone=" + phone + (text ? "&text=" + encodeURIComponent(text) : "");
            var intentUrl = "intent://send?phone=" + phone + (text ? "&text=" + encodeURIComponent(text) : "") + "#Intent;scheme=whatsapp;package=com.whatsapp;end";
            var whatsappScheme = "whatsapp://send?phone=" + phone + (text ? "&text=" + encodeURIComponent(text) : "");

            // Detect environment
            var ua = navigator.userAgent.toLowerCase();
            var isAndroid = /android/i.test(ua);
            var isLinkedIn = /linkedin/i.test(ua);
            var isTwitter = /twitter/i.test(ua);
            var isFacebook = /fban|fbav/i.test(ua);
            var isInstagram = /instagram/i.test(ua);
            var isWebview = isLinkedIn || isTwitter || isFacebook || isInstagram;

            // Elements
            var card = document.getElementById('card');
            var subtitle = document.getElementById('subtitle');
            var linkedinWarning = document.getElementById('linkedinWarning');
            var openBtn = document.getElementById('openBtn');
            var copyBtn = document.getElementById('copyBtn');
            var copyText = document.getElementById('copyText');
            var shareBtn = document.getElementById('shareBtn');
            var statusMsg = document.getElementById('statusMsg');
            var instructions = document.getElementById('instructions');

            // Show LinkedIn-specific warning
            if (isAndroid && isLinkedIn) {{
                card.classList.add('linkedin-detected');
                linkedinWarning.classList.add('show');
                subtitle.textContent = "One more step needed...";
            }}

            // Show share button if Web Share API is available
            if (navigator.share) {{
                shareBtn.style.display = 'flex';
            }}

            // Try to open WhatsApp
            function openWhatsApp(e) {{
                if (e) e.preventDefault();

                if (isAndroid && isWebview) {{
                    // In Android webview, try multiple methods

                    // Method 1: Hidden iframe with intent
                    try {{
                        var iframe = document.createElement('iframe');
                        iframe.style.display = 'none';
                        iframe.src = intentUrl;
                        document.body.appendChild(iframe);
                        setTimeout(function() {{
                            if (iframe.parentNode) iframe.parentNode.removeChild(iframe);
                        }}, 2000);
                    }} catch(e) {{}}

                    // Method 2: Try whatsapp:// scheme
                    setTimeout(function() {{
                        try {{ window.location.href = whatsappScheme; }} catch(e) {{}}
                    }}, 100);

                    // Method 3: Try api.whatsapp.com
                    setTimeout(function() {{
                        try {{ window.location.href = apiUrl; }} catch(e) {{}}
                    }}, 250);

                    // Method 4: Try wa.me
                    setTimeout(function() {{
                        try {{ window.location.href = waUrl; }} catch(e) {{}}
                    }}, 400);

                }} else if (isAndroid) {{
                    // Android but not in webview - direct works
                    window.location.href = apiUrl;
                }} else {{
                    // iOS or Desktop - wa.me works fine
                    window.location.href = waUrl;
                }}
            }}

            // Copy link
            function copyLink() {{
                var linkToCopy = waUrl;

                if (navigator.clipboard && navigator.clipboard.writeText) {{
                    navigator.clipboard.writeText(linkToCopy).then(function() {{
                        showCopySuccess();
                    }}).catch(function() {{
                        fallbackCopy(linkToCopy);
                    }});
                }} else {{
                    fallbackCopy(linkToCopy);
                }}
            }}

            function fallbackCopy(text) {{
                var input = document.createElement('input');
                input.value = text;
                input.style.position = 'fixed';
                input.style.opacity = '0';
                document.body.appendChild(input);
                input.select();
                input.setSelectionRange(0, 99999);
                try {{
                    document.execCommand('copy');
                    showCopySuccess();
                }} catch(e) {{
                    statusMsg.textContent = 'Copy failed - please copy manually';
                }}
                document.body.removeChild(input);
            }}

            function showCopySuccess() {{
                copyText.textContent = 'Copied!';
                copyBtn.classList.add('copied');
                statusMsg.textContent = 'Link copied! Paste in Chrome or your browser.';

                setTimeout(function() {{
                    copyText.textContent = 'Copy Link';
                    copyBtn.classList.remove('copied');
                }}, 3000);
            }}

            // Share via Web Share API
            function sharePage() {{
                if (navigator.share) {{
                    navigator.share({{
                        title: 'Chat with Tal on WhatsApp',
                        text: 'Open this link to chat:',
                        url: waUrl
                    }}).then(function() {{
                        statusMsg.textContent = 'Shared! Open the link in a browser.';
                    }}).catch(function(e) {{
                        console.log('Share failed:', e);
                    }});
                }}
            }}

            // Event listeners
            openBtn.addEventListener('click', openWhatsApp);
            copyBtn.addEventListener('click', copyLink);
            shareBtn.addEventListener('click', sharePage);

            // Auto-attempt on load (but not for LinkedIn Android - it won't work)
            if (!(isAndroid && isLinkedIn)) {{
                setTimeout(function() {{
                    openWhatsApp(null);
                }}, 500);
            }}

        }})();
    </script>
</body>
</html>"""


CHROME_INTENT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="robots" content="noindex, nofollow">
    <meta name="theme-color" content="#1a1a2e">
    <title>Opening WhatsApp...</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #eee;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .card {{
            background: rgba(22, 33, 62, 0.95);
            border-radius: 20px;
            padding: 32px 24px;
            max-width: 400px;
            width: 100%;
            text-align: center;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
        }}
        .logo {{
            width: 56px;
            height: 56px;
            margin: 0 auto 16px;
            background: #25D366;
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .logo svg {{ width: 32px; height: 32px; fill: white; }}
        h1 {{ font-size: 1.3rem; margin-bottom: 8px; color: #fff; }}
        .subtitle {{ color: #9ca3af; font-size: 0.9rem; line-height: 1.5; margin-bottom: 20px; }}
        .spinner {{
            width: 40px;
            height: 40px;
            border: 3px solid rgba(37, 211, 102, 0.2);
            border-top-color: #25D366;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
        .status {{ color: #6b7280; font-size: 0.85rem; margin-bottom: 24px; min-height: 1.5em; }}
        .cta-button {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 16px 24px;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            color: #fff;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 12px;
            text-decoration: none;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        }}
        .cta-button svg {{ width: 22px; height: 22px; fill: white; }}
        .secondary-buttons {{ display: flex; gap: 10px; margin-top: 12px; }}
        .secondary-btn {{
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            padding: 12px 16px;
            background: #374151;
            color: #fff;
            font-size: 0.85rem;
            font-weight: 500;
            border: none;
            border-radius: 10px;
            cursor: pointer;
        }}
        .secondary-btn:hover {{ background: #4b5563; }}
        .secondary-btn.copied {{ background: #25D366; }}
        .secondary-btn svg {{ width: 18px; height: 18px; fill: currentColor; }}
        .fallback-info {{
            margin-top: 24px;
            padding-top: 20px;
            border-top: 1px solid rgba(255,255,255,0.1);
            text-align: left;
        }}
        .fallback-info p {{ color: #6b7280; font-size: 0.8rem; margin-bottom: 10px; }}
        .fallback-info ol {{ color: #9ca3af; font-size: 0.8rem; line-height: 1.8; padding-left: 18px; }}
        .fallback-info strong {{ color: #fff; }}
        .footer {{ margin-top: 20px; font-size: 0.7rem; color: #4b5563; }}
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        </div>

        <h1>Opening Chrome...</h1>
        <p class="subtitle">Chrome will open WhatsApp for you</p>

        <div class="spinner" id="spinner"></div>
        <p class="status" id="status">Launching Chrome browser...</p>

        <a href="{wa_url}" class="cta-button" id="openBtn" style="display:none;">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            Open WhatsApp
        </a>

        <div class="secondary-buttons" id="secondaryBtns" style="display:none;">
            <button class="secondary-btn" id="copyBtn">
                <svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
                <span id="copyText">Copy</span>
            </button>
            <button class="secondary-btn" id="shareBtn" style="display:none;">
                <svg viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92s2.92-1.31 2.92-2.92-1.31-2.92-2.92-2.92z"/></svg>
                Share
            </button>
        </div>

        <div class="fallback-info" id="fallbackInfo" style="display:none;">
            <p>If Chrome didn't open:</p>
            <ol>
                <li>Tap <strong>⋮</strong> menu (top-right)</li>
                <li>Select <strong>"Open in browser"</strong></li>
            </ol>
        </div>

        <div class="footer">Powered by Tal</div>
    </div>

    <script>
        (function() {{
            'use strict';

            var phone = "{phone}";
            var text = "{text}";
            var waUrl = "{wa_url}";

            // Chrome intent URL - opens Chrome with the WhatsApp URL
            var chromeIntentUrl = "intent://wa.me/" + phone + (text ? "?text=" + encodeURIComponent(text) : "") + "#Intent;scheme=https;package=com.android.chrome;S.browser_fallback_url=" + encodeURIComponent(waUrl) + ";end";

            // Alternative: open api.whatsapp.com in Chrome
            var chromeApiIntent = "intent://api.whatsapp.com/send?phone=" + phone + (text ? "&text=" + encodeURIComponent(text) : "") + "#Intent;scheme=https;package=com.android.chrome;S.browser_fallback_url=" + encodeURIComponent(waUrl) + ";end";

            // Elements
            var spinner = document.getElementById('spinner');
            var status = document.getElementById('status');
            var openBtn = document.getElementById('openBtn');
            var secondaryBtns = document.getElementById('secondaryBtns');
            var fallbackInfo = document.getElementById('fallbackInfo');
            var copyBtn = document.getElementById('copyBtn');
            var copyText = document.getElementById('copyText');
            var shareBtn = document.getElementById('shareBtn');

            var isAndroid = /android/i.test(navigator.userAgent);

            function showFallback() {{
                spinner.style.display = 'none';
                status.textContent = 'Tap the button to open WhatsApp';
                openBtn.style.display = 'flex';
                secondaryBtns.style.display = 'flex';
                fallbackInfo.style.display = 'block';
                if (navigator.share) shareBtn.style.display = 'flex';
            }}

            function tryChromeIntent() {{
                if (!isAndroid) {{
                    // Not Android, just redirect to wa.me
                    window.location.href = waUrl;
                    return;
                }}

                status.textContent = 'Opening Chrome...';

                // Method 1: Try Chrome intent with wa.me
                var iframe = document.createElement('iframe');
                iframe.style.display = 'none';
                iframe.src = chromeIntentUrl;
                document.body.appendChild(iframe);

                // Method 2: Try Chrome intent with api.whatsapp.com
                setTimeout(function() {{
                    var iframe2 = document.createElement('iframe');
                    iframe2.style.display = 'none';
                    iframe2.src = chromeApiIntent;
                    document.body.appendChild(iframe2);
                }}, 200);

                // Method 3: Direct location change to Chrome intent
                setTimeout(function() {{
                    try {{
                        window.location.href = chromeIntentUrl;
                    }} catch(e) {{}}
                }}, 400);

                // Show fallback UI after attempts
                setTimeout(function() {{
                    showFallback();
                }}, 2000);
            }}

            // Copy functionality
            copyBtn.addEventListener('click', function() {{
                if (navigator.clipboard) {{
                    navigator.clipboard.writeText(waUrl).then(function() {{
                        copyText.textContent = 'Copied!';
                        copyBtn.classList.add('copied');
                        setTimeout(function() {{
                            copyText.textContent = 'Copy';
                            copyBtn.classList.remove('copied');
                        }}, 2000);
                    }});
                }}
            }});

            // Share functionality
            shareBtn.addEventListener('click', function() {{
                if (navigator.share) {{
                    navigator.share({{ title: 'Chat with Tal', url: waUrl }});
                }}
            }});

            // Start immediately
            tryChromeIntent();
        }})();
    </script>
</body>
</html>"""


ULTIMATE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Chat with Tal</title>
    <style>
        *{{margin:0;padding:0;box-sizing:border-box}}
        body{{font-family:-apple-system,sans-serif;background:#0f172a;color:#fff;min-height:100vh;padding:20px;display:flex;align-items:center;justify-content:center}}
        .card{{background:#1e293b;border-radius:20px;padding:28px 24px;max-width:380px;width:100%;text-align:center}}
        .logo{{width:60px;height:60px;background:#25D366;border-radius:14px;margin:0 auto 20px;display:flex;align-items:center;justify-content:center}}
        .logo svg{{width:34px;height:34px;fill:#fff}}
        h1{{font-size:1.4rem;margin-bottom:8px}}
        .sub{{color:#94a3b8;font-size:0.9rem;margin-bottom:24px}}
        .status{{background:rgba(37,211,102,0.15);border:1px solid #25D366;border-radius:10px;padding:12px;margin-bottom:20px;font-size:0.85rem;color:#25D366}}
        .btn{{display:block;width:100%;padding:16px;font-size:1rem;font-weight:600;border:none;border-radius:12px;cursor:pointer;text-decoration:none;margin-bottom:10px;color:#fff}}
        .btn-green{{background:linear-gradient(135deg,#25D366,#128C7E)}}
        .btn-gray{{background:#334155;font-size:0.9rem}}
        .qr-section{{margin:24px 0;padding:20px;background:rgba(255,255,255,0.05);border-radius:12px}}
        .qr-section p{{color:#94a3b8;font-size:0.8rem;margin-bottom:12px}}
        .qr-code{{background:#fff;padding:12px;border-radius:8px;display:inline-block}}
        .qr-code img{{display:block}}
        .steps{{background:rgba(0,0,0,0.3);border-radius:12px;padding:16px;margin:20px 0;text-align:left}}
        .steps p{{color:#64748b;font-size:0.75rem;margin-bottom:10px}}
        .steps ol{{color:#94a3b8;font-size:0.8rem;padding-left:20px;line-height:1.8}}
        .steps strong{{color:#fff}}
        .divider{{color:#475569;font-size:0.7rem;margin:20px 0}}
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
        </div>

        <h1>Chat with Tal</h1>
        <p class="sub">on WhatsApp</p>

        <div class="status" id="status">Trying to open WhatsApp...</div>

        <a href="{wa_url}" class="btn btn-green" id="waBtn">Open WhatsApp</a>

        <button class="btn btn-gray" id="copyBtn">📋 Copy Link</button>

        <button class="btn btn-gray" id="shareBtn" style="display:none;">📤 Share Link</button>

        <div class="steps">
            <p>If WhatsApp doesn't open:</p>
            <ol>
                <li>Tap <strong>⋮</strong> menu (top-right)</li>
                <li>Select <strong>"Open in browser"</strong></li>
                <li>Or copy link → open Chrome → paste</li>
            </ol>
        </div>

        <div class="divider">— or scan QR code —</div>

        <div class="qr-section">
            <p>Scan with your camera app:</p>
            <div class="qr-code">
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=140x140&data={wa_url_encoded}" width="140" height="140" alt="QR Code">
            </div>
        </div>
    </div>

    <script>
    (function(){{
        var waUrl = "{wa_url}";
        var status = document.getElementById('status');
        var copyBtn = document.getElementById('copyBtn');
        var shareBtn = document.getElementById('shareBtn');

        // Try everything
        function tryAll() {{
            // 1. Auto-copy to clipboard
            if(navigator.clipboard){{
                navigator.clipboard.writeText(waUrl).then(function(){{
                    status.textContent = '✓ Link copied! Paste in Chrome';
                }}).catch(function(){{}});
            }}

            // 2. Try WhatsApp URL schemes
            var schemes = [
                'intent://send?phone={phone}&text={text_encoded}#Intent;scheme=whatsapp;package=com.whatsapp;end',
                'whatsapp://send?phone={phone}&text={text_encoded}',
                'https://api.whatsapp.com/send?phone={phone}&text={text_encoded}',
                waUrl
            ];

            schemes.forEach(function(url, i){{
                setTimeout(function(){{
                    try{{
                        if(i < 2){{
                            var iframe = document.createElement('iframe');
                            iframe.style.display = 'none';
                            iframe.src = url;
                            document.body.appendChild(iframe);
                        }} else {{
                            window.location.href = url;
                        }}
                    }}catch(e){{}}
                }}, i * 150);
            }});

            // Update status after attempts
            setTimeout(function(){{
                status.innerHTML = '✓ Link copied to clipboard<br><small>Open Chrome and paste to continue</small>';
            }}, 1000);
        }}

        // Copy button
        copyBtn.onclick = function(){{
            if(navigator.clipboard){{
                navigator.clipboard.writeText(waUrl).then(function(){{
                    copyBtn.textContent = '✓ Copied!';
                    copyBtn.style.background = '#25D366';
                    setTimeout(function(){{
                        copyBtn.textContent = '📋 Copy Link';
                        copyBtn.style.background = '';
                    }}, 2000);
                }});
            }}
        }};

        // Share button
        if(navigator.share){{
            shareBtn.style.display = 'block';
            shareBtn.onclick = function(){{
                navigator.share({{title:'Chat with Tal',url:waUrl}});
            }};
        }}

        // Run on load
        tryAll();
    }})();
    </script>
</body>
</html>"""


AUTO_COPY_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Link Copied!</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #fff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .card {{
            background: #1e293b;
            border-radius: 24px;
            padding: 40px 28px;
            max-width: 380px;
            width: 100%;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.1);
        }}
        .success-icon {{
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 24px;
            animation: pop 0.4s ease-out;
        }}
        @keyframes pop {{
            0% {{ transform: scale(0); }}
            80% {{ transform: scale(1.1); }}
            100% {{ transform: scale(1); }}
        }}
        .success-icon svg {{ width: 40px; height: 40px; fill: white; }}
        .checkmark {{ stroke-dasharray: 50; stroke-dashoffset: 50; animation: draw 0.5s 0.3s forwards; }}
        @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
        h1 {{
            font-size: 1.6rem;
            margin-bottom: 12px;
            color: #25D366;
        }}
        .subtitle {{
            color: #94a3b8;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 32px;
        }}
        .steps {{
            background: rgba(0,0,0,0.3);
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 24px;
            text-align: left;
        }}
        .step {{
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        .step:last-child {{ border-bottom: none; }}
        .step-num {{
            width: 32px;
            height: 32px;
            background: #25D366;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.9rem;
            flex-shrink: 0;
        }}
        .step-text {{
            color: #e2e8f0;
            font-size: 0.95rem;
        }}
        .step-text strong {{ color: #fff; }}
        .btn {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 16px 24px;
            font-size: 1rem;
            font-weight: 600;
            border: none;
            border-radius: 14px;
            cursor: pointer;
            text-decoration: none;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 12px;
        }}
        .btn:active {{ transform: scale(0.98); }}
        .btn-primary {{
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            color: #fff;
            box-shadow: 0 4px 20px rgba(37, 211, 102, 0.4);
        }}
        .btn-secondary {{
            background: #334155;
            color: #fff;
        }}
        .btn svg {{ width: 22px; height: 22px; fill: currentColor; }}
        .copied-text {{
            display: none;
            background: rgba(37, 211, 102, 0.2);
            border: 1px solid #25D366;
            border-radius: 10px;
            padding: 12px;
            margin-bottom: 20px;
            font-size: 0.85rem;
            color: #25D366;
        }}
        .copied-text.show {{ display: block; }}
        .link-box {{
            background: rgba(0,0,0,0.4);
            border-radius: 10px;
            padding: 14px;
            margin-bottom: 20px;
            word-break: break-all;
            font-size: 0.8rem;
            color: #64748b;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        .footer {{
            margin-top: 24px;
            font-size: 0.75rem;
            color: #475569;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="success-icon">
            <svg viewBox="0 0 24 24">
                <path class="checkmark" d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" fill="none" stroke="white" stroke-width="2"/>
            </svg>
        </div>

        <h1 id="title">Link Copied!</h1>
        <p class="subtitle" id="subtitle">Now just paste it in Chrome to chat with Tal on WhatsApp</p>

        <div class="copied-text show" id="copiedMsg">
            ✓ WhatsApp link is in your clipboard
        </div>

        <div class="steps">
            <div class="step">
                <div class="step-num">1</div>
                <div class="step-text">Open <strong>Chrome</strong> browser</div>
            </div>
            <div class="step">
                <div class="step-num">2</div>
                <div class="step-text">Tap the address bar and <strong>Paste</strong></div>
            </div>
            <div class="step">
                <div class="step-num">3</div>
                <div class="step-text">Press <strong>Go</strong> → WhatsApp opens!</div>
            </div>
        </div>

        <button class="btn btn-primary" id="copyBtn">
            <svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
            <span id="copyText">Copy Again</span>
        </button>

        <button class="btn btn-secondary" id="shareBtn" style="display:none;">
            <svg viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92s2.92-1.31 2.92-2.92-1.31-2.92-2.92-2.92z"/></svg>
            Share Link
        </button>

        <a href="{wa_url}" class="btn btn-secondary">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            Try Direct Link
        </a>

        <div class="footer">Powered by Tal</div>
    </div>

    <script>
        (function() {{
            var waUrl = "{wa_url}";
            var title = document.getElementById('title');
            var subtitle = document.getElementById('subtitle');
            var copiedMsg = document.getElementById('copiedMsg');
            var copyBtn = document.getElementById('copyBtn');
            var copyText = document.getElementById('copyText');
            var shareBtn = document.getElementById('shareBtn');

            // Auto-copy on page load
            function autoCopy() {{
                if (navigator.clipboard && navigator.clipboard.writeText) {{
                    navigator.clipboard.writeText(waUrl).then(function() {{
                        console.log('Auto-copied!');
                    }}).catch(function() {{
                        fallbackCopy();
                    }});
                }} else {{
                    fallbackCopy();
                }}
            }}

            function fallbackCopy() {{
                var input = document.createElement('textarea');
                input.value = waUrl;
                input.style.position = 'fixed';
                input.style.opacity = '0';
                document.body.appendChild(input);
                input.focus();
                input.select();
                try {{
                    document.execCommand('copy');
                }} catch(e) {{
                    title.textContent = 'Copy the Link';
                    subtitle.textContent = 'Tap "Copy" then paste in Chrome';
                    copiedMsg.classList.remove('show');
                }}
                document.body.removeChild(input);
            }}

            // Manual copy button
            copyBtn.addEventListener('click', function() {{
                if (navigator.clipboard && navigator.clipboard.writeText) {{
                    navigator.clipboard.writeText(waUrl).then(function() {{
                        copyText.textContent = 'Copied!';
                        copyBtn.style.background = '#25D366';
                        setTimeout(function() {{
                            copyText.textContent = 'Copy Again';
                            copyBtn.style.background = '';
                        }}, 2000);
                    }});
                }} else {{
                    fallbackCopy();
                    copyText.textContent = 'Copied!';
                }}
            }});

            // Share button
            if (navigator.share) {{
                shareBtn.style.display = 'flex';
                shareBtn.addEventListener('click', function() {{
                    navigator.share({{
                        title: 'Chat with Tal',
                        text: 'Open this link to chat on WhatsApp:',
                        url: waUrl
                    }});
                }});
            }}

            // Auto-copy on load
            autoCopy();
        }})();
    </script>
</body>
</html>"""


CHROME_OPEN_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="0;url={chrome_intent_url}">
    <title>Opening Chrome...</title>
    <style>
        body {{
            font-family: -apple-system, sans-serif;
            background: #1a1a2e;
            color: #fff;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
            padding: 20px;
            text-align: center;
        }}
        .container {{ max-width: 350px; }}
        h1 {{ font-size: 1.3rem; margin-bottom: 16px; }}
        p {{ color: #9ca3af; font-size: 0.9rem; margin-bottom: 24px; }}
        .spinner {{
            width: 40px;
            height: 40px;
            border: 3px solid rgba(37,211,102,0.2);
            border-top-color: #25D366;
            border-radius: 50%;
            animation: spin 1s linear infinite;
            margin: 0 auto 24px;
        }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
        a {{
            display: block;
            padding: 16px;
            background: #25D366;
            color: #fff;
            text-decoration: none;
            border-radius: 12px;
            font-weight: 600;
            margin-bottom: 12px;
        }}
        .secondary {{
            background: #374151;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="spinner"></div>
        <h1>Opening Chrome...</h1>
        <p>Chrome will open WhatsApp for you.</p>

        <a href="{chrome_intent_url}" id="chromeBtn">Open in Chrome</a>
        <a href="{wa_url}" class="secondary">Direct WhatsApp Link</a>
    </div>

    <script>
        (function() {{
            var chromeIntent = "{chrome_intent_url}";
            var waUrl = "{wa_url}";

            // Immediately try to open Chrome
            window.location.href = chromeIntent;

            // Fallback: try again after short delay
            setTimeout(function() {{
                window.location.href = chromeIntent;
            }}, 100);

            // If still here after 2 seconds, try iframe method
            setTimeout(function() {{
                var iframe = document.createElement('iframe');
                iframe.style.display = 'none';
                iframe.src = chromeIntent;
                document.body.appendChild(iframe);
            }}, 500);
        }})();
    </script>
</body>
</html>"""


LINKEDIN_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Open in Chrome</title>
    <style>
        *{{margin:0;padding:0;box-sizing:border-box}}
        body{{
            font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
            background:linear-gradient(180deg,#0077B5 0%,#004471 100%);
            color:#fff;
            min-height:100vh;
            padding:20px;
        }}
        .container{{max-width:400px;margin:0 auto}}

        /* Hero section */
        .hero{{
            background:#fff;
            border-radius:24px;
            padding:32px 24px;
            text-align:center;
            box-shadow:0 20px 60px rgba(0,0,0,0.3);
            margin-bottom:20px;
        }}
        .hero-icon{{
            width:72px;
            height:72px;
            background:#0077B5;
            border-radius:50%;
            display:flex;
            align-items:center;
            justify-content:center;
            margin:0 auto 20px;
        }}
        .hero-icon svg{{width:36px;height:36px;fill:#fff}}
        .hero h1{{
            color:#1a1a1a;
            font-size:1.4rem;
            margin-bottom:8px;
        }}
        .hero p{{
            color:#666;
            font-size:0.95rem;
            margin-bottom:24px;
        }}

        /* Steps */
        .steps{{
            background:#f8f9fa;
            border-radius:16px;
            padding:20px;
            text-align:left;
        }}
        .step{{
            display:flex;
            align-items:flex-start;
            gap:16px;
            padding:16px 0;
            border-bottom:1px solid #e5e7eb;
        }}
        .step:last-child{{border-bottom:none}}
        .step-num{{
            width:36px;
            height:36px;
            background:#0077B5;
            color:#fff;
            border-radius:50%;
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:700;
            font-size:1rem;
            flex-shrink:0;
        }}
        .step-content{{flex:1}}
        .step-title{{
            color:#1a1a1a;
            font-weight:600;
            font-size:1rem;
            margin-bottom:4px;
        }}
        .step-desc{{
            color:#666;
            font-size:0.85rem;
            line-height:1.4;
        }}
        .step-highlight{{
            display:inline-flex;
            align-items:center;
            gap:6px;
            background:#0077B5;
            color:#fff;
            padding:4px 10px;
            border-radius:6px;
            font-weight:600;
            font-size:0.85rem;
        }}
        .menu-dots{{
            font-size:1.2rem;
            font-weight:bold;
            background:#333;
            color:#fff;
            padding:2px 8px;
            border-radius:4px;
        }}

        /* Arrow animation */
        .arrow-hint{{
            position:fixed;
            top:12px;
            right:12px;
            background:#FFD700;
            color:#1a1a1a;
            padding:10px 14px;
            border-radius:12px;
            font-weight:600;
            font-size:0.85rem;
            animation:pulse 2s infinite;
            z-index:100;
            box-shadow:0 4px 20px rgba(0,0,0,0.3);
        }}
        .arrow-hint::after{{
            content:'↗';
            margin-left:6px;
            font-size:1.1rem;
        }}
        @keyframes pulse{{
            0%,100%{{transform:scale(1);opacity:1}}
            50%{{transform:scale(1.05);opacity:0.9}}
        }}

        /* Copy section */
        .copy-section{{
            background:rgba(255,255,255,0.15);
            backdrop-filter:blur(10px);
            border-radius:16px;
            padding:20px;
            text-align:center;
        }}
        .copy-section p{{
            font-size:0.9rem;
            margin-bottom:16px;
            opacity:0.9;
        }}
        .btn{{
            display:flex;
            align-items:center;
            justify-content:center;
            gap:10px;
            width:100%;
            padding:16px;
            font-size:1rem;
            font-weight:600;
            border:none;
            border-radius:12px;
            cursor:pointer;
            text-decoration:none;
            margin-bottom:10px;
            color:#fff;
            transition:transform 0.2s;
        }}
        .btn:active{{transform:scale(0.98)}}
        .btn-white{{background:#fff;color:#0077B5}}
        .btn-green{{background:#25D366}}
        .btn-outline{{background:transparent;border:2px solid rgba(255,255,255,0.5)}}
        .btn svg{{width:20px;height:20px;fill:currentColor}}

        /* Status */
        .status{{
            background:rgba(37,211,102,0.2);
            border:1px solid #25D366;
            border-radius:10px;
            padding:12px;
            font-size:0.9rem;
            color:#25D366;
            margin-bottom:16px;
            text-align:center;
        }}

        .footer{{
            text-align:center;
            margin-top:24px;
            font-size:0.75rem;
            opacity:0.7;
        }}
    </style>
</head>
<body>
    <div class="arrow-hint">Tap menu here</div>

    <div class="container">
        <div class="hero">
            <div class="hero-icon">
                <svg viewBox="0 0 24 24"><path d="M19 19H5V5h7V3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2v-7h-2v7zM14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3h-7z"/></svg>
            </div>
            <h1>Open in Chrome to Continue</h1>
            <p>LinkedIn's browser can't open WhatsApp directly. Follow these quick steps:</p>

            <div class="steps">
                <div class="step">
                    <div class="step-num">1</div>
                    <div class="step-content">
                        <div class="step-title">Tap the menu <span class="menu-dots">⋮</span></div>
                        <div class="step-desc">Look for 3 dots in the top-right corner</div>
                    </div>
                </div>
                <div class="step">
                    <div class="step-num">2</div>
                    <div class="step-content">
                        <div class="step-title">Select <span class="step-highlight">Open in browser</span></div>
                        <div class="step-desc">This opens Chrome (or your default browser)</div>
                    </div>
                </div>
                <div class="step">
                    <div class="step-num">3</div>
                    <div class="step-content">
                        <div class="step-title">WhatsApp opens automatically!</div>
                        <div class="step-desc">You'll be chatting with Tal in seconds</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="copy-section">
            <div class="status" id="status">✓ Link copied to clipboard</div>
            <p>Alternative: Paste this link in Chrome</p>

            <button class="btn btn-white" id="copyBtn">
                <svg viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>
                <span id="copyText">Copy Link Again</span>
            </button>

            <button class="btn btn-outline" id="shareBtn" style="display:none;">
                <svg viewBox="0 0 24 24"><path d="M18 16.08c-.76 0-1.44.3-1.96.77L8.91 12.7c.05-.23.09-.46.09-.7s-.04-.47-.09-.7l7.05-4.11c.54.5 1.25.81 2.04.81 1.66 0 3-1.34 3-3s-1.34-3-3-3-3 1.34-3 3c0 .24.04.47.09.7L8.04 9.81C7.5 9.31 6.79 9 6 9c-1.66 0-3 1.34-3 3s1.34 3 3 3c.79 0 1.5-.31 2.04-.81l7.12 4.16c-.05.21-.08.43-.08.65 0 1.61 1.31 2.92 2.92 2.92s2.92-1.31 2.92-2.92-1.31-2.92-2.92-2.92z"/></svg>
                Share to Chrome
            </button>

            <a href="{wa_url}" class="btn btn-green">
                <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                Try WhatsApp Anyway
            </a>
        </div>

        <div class="footer">
            Chat with Tal on WhatsApp • Powered by Tal
        </div>
    </div>

    <script>
    (function(){{
        var waUrl = "{wa_url}";
        var status = document.getElementById('status');
        var copyBtn = document.getElementById('copyBtn');
        var copyText = document.getElementById('copyText');
        var shareBtn = document.getElementById('shareBtn');

        // Auto-copy on load
        function autoCopy() {{
            if (navigator.clipboard && navigator.clipboard.writeText) {{
                navigator.clipboard.writeText(waUrl).then(function() {{
                    status.textContent = '✓ Link copied to clipboard';
                    status.style.display = 'block';
                }}).catch(function() {{
                    status.style.display = 'none';
                }});
            }} else {{
                // Fallback
                var input = document.createElement('textarea');
                input.value = waUrl;
                input.style.cssText = 'position:fixed;opacity:0';
                document.body.appendChild(input);
                input.select();
                try {{
                    document.execCommand('copy');
                    status.textContent = '✓ Link copied to clipboard';
                }} catch(e) {{
                    status.style.display = 'none';
                }}
                document.body.removeChild(input);
            }}
        }}

        // Copy button
        copyBtn.onclick = function() {{
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(waUrl).then(function() {{
                    copyText.textContent = 'Copied!';
                    copyBtn.style.background = '#25D366';
                    copyBtn.style.color = '#fff';
                    setTimeout(function() {{
                        copyText.textContent = 'Copy Link Again';
                        copyBtn.style.background = '#fff';
                        copyBtn.style.color = '#0077B5';
                    }}, 2000);
                }});
            }}
        }};

        // Share button (share to Chrome specifically)
        if (navigator.share) {{
            shareBtn.style.display = 'flex';
            shareBtn.onclick = function() {{
                navigator.share({{
                    title: 'Chat with Tal on WhatsApp',
                    text: 'Open this link in Chrome:',
                    url: waUrl
                }});
            }};
        }}

        // Run auto-copy
        autoCopy();

        // Hide arrow after 5 seconds
        setTimeout(function() {{
            document.querySelector('.arrow-hint').style.opacity = '0.5';
        }}, 5000);
    }})();
    </script>
</body>
</html>"""


ERROR_PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>Error - Tal Redirector</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #1a1a2e;
            color: #eee;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .card {{
            background: #16213e;
            border-radius: 16px;
            padding: 32px;
            max-width: 400px;
            text-align: center;
        }}
        h1 {{ color: #ef4444; margin-bottom: 16px; font-size: 1.5rem; }}
        p {{ color: #9ca3af; line-height: 1.6; }}
        .code {{ color: #6b7280; font-size: 0.8rem; margin-top: 20px; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>Something went wrong</h1>
        <p>{error_message}</p>
        <p class="code">Error: {error_code}</p>
    </div>
</body>
</html>"""
