import glob
import re

new_colors = '''"colors": {
                        "primary": "#2563EB",
                        "surface-dim": "#f1f5f9",
                        "surface": "#ffffff",
                        "surface-container": "#f8fafc",
                        "on-surface-variant": "#475569",
                        "inverse-primary": "#bfdbfe",
                        "on-background": "#0f172a",
                        "on-tertiary-fixed-variant": "#334155",
                        "on-secondary": "#ffffff",
                        "tertiary-container": "#e2e8f0",
                        "outline-variant": "#cbd5e1",
                        "surface-container-lowest": "#ffffff",
                        "on-tertiary-container": "#0f172a",
                        "inverse-on-surface": "#f1f5f9",
                        "secondary-fixed-dim": "#d1fae5",
                        "on-error": "#ffffff",
                        "inverse-surface": "#1e293b",
                        "on-primary-fixed-variant": "#1e3a8a",
                        "surface-container-low": "#f8fafc",
                        "tertiary": "#64748b",
                        "secondary": "#10B981",
                        "primary-container": "#dbeafe",
                        "on-secondary-fixed": "#064e3b",
                        "secondary-fixed": "#a7f3d0",
                        "secondary-container": "#d1fae5",
                        "on-tertiary": "#ffffff",
                        "on-error-container": "#450a0a",
                        "surface-container-highest": "#e2e8f0",
                        "error-container": "#fee2e2",
                        "on-primary-fixed": "#1e3a8a",
                        "on-tertiary-fixed": "#0f172a",
                        "surface-variant": "#f1f5f9",
                        "outline": "#94a3b8",
                        "surface-tint": "#3b82f6",
                        "primary-fixed-dim": "#93c5fd",
                        "tertiary-fixed": "#f1f5f9",
                        "background": "#f8fafc",
                        "on-primary-container": "#1e3a8a",
                        "on-surface": "#0f172a",
                        "tertiary-fixed-dim": "#cbd5e1",
                        "surface-bright": "#ffffff",
                        "on-secondary-fixed-variant": "#047857",
                        "on-secondary-container": "#065f46",
                        "primary-fixed": "#bfdbfe",
                        "on-primary": "#ffffff",
                        "surface-container-high": "#e2e8f0",
                        "error": "#ef4444"
                    }'''

for filepath in glob.glob('app/templates/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Remove dark class
    if '<html class="dark"' in content:
        content = content.replace('<html class="dark"', '<html')
        modified = True

    # 2. Replace body background colors
    if 'background-color: #0b1326;' in content:
        content = content.replace('background-color: #0b1326;', 'background-color: #f8fafc;')
        content = content.replace('color: #dae2fd;', 'color: #0f172a;')
        modified = True

    # 3. Replace colors dictionary
    if '"colors": {' in content:
        content = re.sub(r'"colors":\s*\{.*?\}(?=\s*,\s*"borderRadius")', new_colors, content, flags=re.DOTALL)
        modified = True
        
    # 4. Remove mesh background div
    if '<div class="mesh-bg"></div>' in content:
        content = content.replace('<div class="mesh-bg"></div>', '')
        modified = True

    # 5. Replace card styling to be clean
    if '.bento-card {' in content:
        # replace the static CSS for bento cards
        content = re.sub(
            r'\.bento-card\s*\{\s*border:\s*1px\s+solid\s+#[0-9a-fA-F]+;\s*background:\s*#[0-9a-fA-F]+;\s*transition:.*?\n\s*\}',
            '.bento-card {\n            border: 1px solid #cbd5e1;\n            background: #ffffff;\n            box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);\n            transition: all 0.2s ease-in-out;\n        }',
            content, flags=re.DOTALL
        )
        content = re.sub(
            r'\.bento-card:hover\s*\{\s*border-color:.*?\n\s*\}',
            '.bento-card:hover {\n            border-color: #94a3b8;\n            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);\n        }',
            content, flags=re.DOTALL
        )
        modified = True

    # 6. Remove the heavy mesh and glassmorphism CSS
    if '/* Animated Mesh Background */' in content:
        # This will remove everything from "/* Animated Mesh Background */" to "/* Header styling */" and the block after it
        content = re.sub(r'/\* Animated Mesh Background \*/.*?</style>', '</style>', content, flags=re.DOTALL)
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filepath}')
