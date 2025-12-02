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
            -moz-osx-font-smoothing: grayscale;
        }}

        .card {{
            background: rgba(22, 33, 62, 0.95);
            border-radius: 20px;
            padding: 36px 28px;
            max-width: 420px;
            width: 100%;
            text-align: center;
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }}

        .logo {{
            width: 64px;
            height: 64px;
            margin: 0 auto 20px;
            background: #25D366;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .logo svg {{
            width: 36px;
            height: 36px;
            fill: white;
        }}

        h1 {{
            font-size: 1.6rem;
            margin-bottom: 12px;
            color: #fff;
            font-weight: 600;
        }}

        .subtitle {{
            color: #9ca3af;
            font-size: 0.95rem;
            line-height: 1.6;
            margin-bottom: 28px;
        }}

        .cta-button {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 18px 28px;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            color: #fff;
            font-size: 1.1rem;
            font-weight: 600;
            border: none;
            border-radius: 14px;
            text-decoration: none;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        }}

        .cta-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
        }}

        .cta-button:active {{
            transform: translateY(0);
        }}

        .cta-button svg {{
            width: 24px;
            height: 24px;
            fill: white;
        }}

        .loading {{
            display: none;
            margin-top: 16px;
            color: #9ca3af;
            font-size: 0.85rem;
        }}

        .loading.show {{
            display: block;
        }}

        .spinner {{
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid rgba(255,255,255,0.3);
            border-radius: 50%;
            border-top-color: #25D366;
            animation: spin 1s linear infinite;
            vertical-align: middle;
            margin-right: 8px;
        }}

        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}

        .divider {{
            display: flex;
            align-items: center;
            margin: 28px 0;
            color: #4b5563;
            font-size: 0.8rem;
        }}

        .divider::before,
        .divider::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: #2a2a4a;
        }}

        .divider span {{
            padding: 0 16px;
        }}

        .instructions {{
            text-align: left;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 12px;
            padding: 16px 20px;
        }}

        .instructions-title {{
            font-size: 0.85rem;
            color: #9ca3af;
            margin-bottom: 12px;
            font-weight: 500;
        }}

        .instructions ol {{
            color: #d1d5db;
            font-size: 0.85rem;
            line-height: 1.9;
            padding-left: 20px;
        }}

        .instructions li {{
            margin-bottom: 4px;
        }}

        .instructions strong {{
            color: #fff;
        }}

        .copy-section {{
            margin-top: 24px;
        }}

        .copy-label {{
            font-size: 0.8rem;
            color: #6b7280;
            margin-bottom: 10px;
        }}

        .copy-wrapper {{
            display: flex;
            gap: 8px;
        }}

        .copy-input {{
            flex: 1;
            padding: 12px 14px;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid #2a2a4a;
            border-radius: 10px;
            color: #9ca3af;
            font-size: 0.8rem;
            outline: none;
            transition: border-color 0.2s;
        }}

        .copy-input:focus {{
            border-color: #25D366;
        }}

        .copy-button {{
            padding: 12px 20px;
            background: #374151;
            color: #fff;
            border: none;
            border-radius: 10px;
            font-size: 0.85rem;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s;
            white-space: nowrap;
        }}

        .copy-button:hover {{
            background: #4b5563;
        }}

        .copy-button.copied {{
            background: #25D366;
        }}

        .copy-success {{
            font-size: 0.75rem;
            color: #25D366;
            margin-top: 10px;
            min-height: 1.2em;
            transition: opacity 0.2s;
        }}

        .footer {{
            margin-top: 28px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            font-size: 0.75rem;
            color: #4b5563;
        }}

        @media (max-width: 380px) {{
            .card {{
                padding: 28px 20px;
            }}

            h1 {{
                font-size: 1.4rem;
            }}

            .cta-button {{
                padding: 16px 24px;
                font-size: 1rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="logo">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
        </div>

        <h1>Open Tal on WhatsApp</h1>
        <p class="subtitle">
            We're trying to open WhatsApp for you. If it doesn't happen automatically, tap the button below.
        </p>

        <a href="{wa_url}" class="cta-button" id="openBtn">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
            Open WhatsApp
        </a>

        <p class="loading" id="loading">
            <span class="spinner"></span>
            Opening WhatsApp...
        </p>

        <div class="divider"><span>having trouble?</span></div>

        <div class="instructions">
            <p class="instructions-title">If WhatsApp doesn't open:</p>
            <ol>
                <li>Tap the <strong>&#8942;</strong> menu (top-right corner)</li>
                <li>Select <strong>"Open in browser"</strong></li>
                <li>Tap the green button again</li>
            </ol>
        </div>

        <div class="copy-section">
            <p class="copy-label">Or copy this link:</p>
            <div class="copy-wrapper">
                <input type="text" class="copy-input" id="copyInput" value="{wa_url}" readonly>
                <button class="copy-button" id="copyBtn">Copy</button>
            </div>
            <p class="copy-success" id="copySuccess"></p>
        </div>

        <div class="footer">
            Powered by Tal
        </div>
    </div>

    <script>
        (function() {{
            'use strict';

            var waUrl = "{wa_url}";
            var loading = document.getElementById('loading');
            var copyBtn = document.getElementById('copyBtn');
            var copyInput = document.getElementById('copyInput');
            var copySuccess = document.getElementById('copySuccess');

            // Auto-attempt to open WhatsApp on load
            function attemptRedirect() {{
                loading.classList.add('show');
                try {{
                    window.location.href = waUrl;
                }} catch (e) {{
                    console.log('[Tal] Auto-redirect failed:', e);
                }}

                // Hide loading after delay
                setTimeout(function() {{
                    loading.classList.remove('show');
                }}, 3000);
            }}

            // Copy functionality
            function copyToClipboard() {{
                try {{
                    copyInput.select();
                    copyInput.setSelectionRange(0, 99999);

                    if (navigator.clipboard && navigator.clipboard.writeText) {{
                        navigator.clipboard.writeText(copyInput.value)
                            .then(showCopySuccess)
                            .catch(fallbackCopy);
                    }} else {{
                        fallbackCopy();
                    }}
                }} catch (e) {{
                    console.log('[Tal] Copy failed:', e);
                    copySuccess.textContent = 'Please copy the link manually';
                }}
            }}

            function fallbackCopy() {{
                try {{
                    document.execCommand('copy');
                    showCopySuccess();
                }} catch (e) {{
                    copySuccess.textContent = 'Please copy the link manually';
                }}
            }}

            function showCopySuccess() {{
                copyBtn.textContent = 'Copied!';
                copyBtn.classList.add('copied');
                copySuccess.textContent = 'Link copied! Paste in your browser.';

                setTimeout(function() {{
                    copyBtn.textContent = 'Copy';
                    copyBtn.classList.remove('copied');
                    copySuccess.textContent = '';
                }}, 4000);
            }}

            // Event listeners
            document.addEventListener('DOMContentLoaded', function() {{
                attemptRedirect();
            }});

            copyBtn.addEventListener('click', copyToClipboard);

            // Also try on visibility change (when user returns to tab)
            document.addEventListener('visibilitychange', function() {{
                if (document.visibilityState === 'visible') {{
                    // User came back, they might need to try again
                    loading.classList.remove('show');
                }}
            }});
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
