import glob
import re

tailwind_config_template = """<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        primary: 'var(--color-primary)',
                        surface: 'var(--color-surface)',
                        'surface-container': 'var(--color-surface-container)',
                        'surface-container-lowest': 'var(--color-surface-container-lowest)',
                        'surface-container-low': 'var(--color-surface-container-low)',
                        'surface-container-high': 'var(--color-surface-container-high)',
                        'surface-container-highest': 'var(--color-surface-container-highest)',
                        'on-surface': 'var(--color-on-surface)',
                        'on-surface-variant': 'var(--color-on-surface-variant)',
                        'outline-variant': 'var(--color-outline-variant)',
                        secondary: 'var(--color-secondary)',
                        error: 'var(--color-error)',
                        background: 'var(--color-background)',
                        'primary-container': 'var(--color-primary-container)',
                        'on-primary': 'var(--color-on-primary)',
                        'on-secondary': 'var(--color-on-secondary)'
                    },
                    borderRadius: {
                        DEFAULT: "0.25rem",
                        lg: "0.5rem",
                        xl: "0.75rem",
                        full: "9999px"
                    },
                    spacing: {
                        gutter: "16px",
                        lg: "24px",
                        md: "16px",
                        xs: "4px",
                        base: "4px",
                        sm: "8px",
                        xl: "40px",
                        'margin-mobile': "16px",
                        'margin-desktop': "32px"
                    },
                    fontFamily: {
                        'headline-lg': ["Inter"],
                        'display-lg': ["Inter"],
                        'title-md': ["Inter"],
                        'label-md': ["Inter"],
                        'body-lg': ["Inter"],
                        'mono-data': ["JetBrains Mono"],
                        'body-md': ["Inter"],
                        'headline-lg-mobile': ["Inter"]
                    }
                }
            }
        }
    </script>"""

css_variables = """<style>
        :root {
            --color-primary: #2563EB;
            --color-surface: #ffffff;
            --color-surface-container: #f8fafc;
            --color-surface-container-lowest: #ffffff;
            --color-surface-container-low: #f8fafc;
            --color-surface-container-high: #e2e8f0;
            --color-surface-container-highest: #e2e8f0;
            --color-on-surface: #0f172a;
            --color-on-surface-variant: #475569;
            --color-outline-variant: #cbd5e1;
            --color-secondary: #10B981;
            --color-error: #ef4444;
            --color-background: #f8fafc;
            --color-primary-container: #dbeafe;
            --color-on-primary: #ffffff;
            --color-on-secondary: #ffffff;
            
            --bento-bg: #ffffff;
            --bento-border: #cbd5e1;
            --bento-hover-border: #94a3b8;
            --glass-bg: rgba(255, 255, 255, 0.95);
            --glass-border: rgba(0, 0, 0, 0.1);
        }
        
        .dark {
            --color-primary: #60A5FA;
            --color-surface: #0b1326;
            --color-surface-container: #171f33;
            --color-surface-container-lowest: #060e20;
            --color-surface-container-low: #131b2e;
            --color-surface-container-high: #222a3d;
            --color-surface-container-highest: #2d3449;
            --color-on-surface: #dae2fd;
            --color-on-surface-variant: #c4c5d5;
            --color-outline-variant: #444653;
            --color-secondary: #2DD4BF;
            --color-error: #ffb4ab;
            --color-background: #0b1326;
            --color-primary-container: #1e40af;
            --color-on-primary: #002584;
            --color-on-secondary: #00354a;
            
            --bento-bg: #171f33;
            --bento-border: #2d3449;
            --bento-hover-border: #60A5FA;
            --glass-bg: rgba(23, 31, 51, 0.9);
            --glass-border: rgba(255, 255, 255, 0.1);
        }

        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            background-color: var(--color-background);
            color: var(--color-on-surface);
        }
        .bento-card {
            border: 1px solid var(--bento-border);
            background: var(--bento-bg);
            box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
            transition: all 0.2s ease-in-out;
        }
        .bento-card:hover {
            border-color: var(--bento-hover-border);
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        }
        .glass-modal {
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--glass-border);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
</style>
<script>
    // Theme Init Script
    (function() {
        var savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    })();
</script>"""

for filepath in glob.glob('app/templates/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace tailwind.config completely
    content = re.sub(r'<script id="tailwind-config">.*?</script>', tailwind_config_template, content, flags=re.DOTALL)
    
    # 2. Replace the style block completely (and any existing theme script)
    # Be careful not to remove all scripts, just the ones related to style or theme
    content = re.sub(r'<style>.*?</style>', css_variables, content, flags=re.DOTALL)
    
    # If the script didn't have <style> for some reason, inject it before </head>
    if '<style>' not in content:
        content = content.replace('</head>', css_variables + '\n</head>')

    # 3. Clean up any remaining <script> block that we just added if it gets duplicated
    # Remove older theme init script if present (we just added it in css_variables)
    content = re.sub(r'<script>\s*// Theme Init Script.*?</script>', '', content, flags=re.DOTALL)
    # Add it right after css_variables
    content = content.replace('</style>', '</style>\n<script>\n    // Theme Init Script\n    (function() {\n        var savedTheme = localStorage.getItem("theme");\n        if (savedTheme === "dark" || (!savedTheme && window.matchMedia("(prefers-color-scheme: dark)").matches)) {\n            document.documentElement.classList.add("dark");\n        } else {\n            document.documentElement.classList.remove("dark");\n        }\n    })();\n</script>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Themes applied successfully!")
