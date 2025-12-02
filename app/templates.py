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
