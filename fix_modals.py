import glob
import re

for filepath in glob.glob('app/templates/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # Fix glass-modal
    if '.glass-modal {' in content:
        content = re.sub(
            r'\.glass-modal\s*\{.*?\}',
            '.glass-modal {\n            background: rgba(255, 255, 255, 0.95);\n            backdrop-filter: blur(12px);\n            -webkit-backdrop-filter: blur(12px);\n            border: 1px solid rgba(0, 0, 0, 0.1);\n            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);\n        }',
            content, flags=re.DOTALL
        )
        modified = True

    # Check for any inline bg-black/60 (modal background overlay)
    if 'bg-black/60' in content:
        content = content.replace('bg-black/60', 'bg-slate-900/40')
        modified = True

    # In dashboard, change SVG chart colors to be lighter if there are any hardcoded colors
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filepath}')
