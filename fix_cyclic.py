import os
import re

templates_dir = r"c:\Users\Hp\OneDrive\Desktop\New folder\expense_tracker\app\templates"

for root, dirs, files in os.walk(templates_dir):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace cyclic mesh-opacity definition in .dark block
            updated_content = re.sub(
                r'--mesh-opacity:\s*var\(--mesh-opacity\);',
                '--mesh-opacity: 0.7;',
                content
            )
            
            if updated_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                print(f"Fixed cyclic opacity in: {file}")
