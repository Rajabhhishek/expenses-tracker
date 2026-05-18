import glob
import re

css_addition = '''
        /* Animated Mesh Background */
        .mesh-bg {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background-color: #040914;
            background-image: 
                radial-gradient(at 0% 0%, rgba(37, 99, 235, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(124, 58, 237, 0.15) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(14, 165, 233, 0.15) 0px, transparent 50%),
                radial-gradient(at 0% 100%, rgba(139, 92, 246, 0.15) 0px, transparent 50%);
            z-index: -2;
            animation: mesh-pulse 15s ease-in-out infinite alternate;
        }
        @keyframes mesh-pulse {
            0% { opacity: 0.7; transform: scale(1); }
            100% { opacity: 1; transform: scale(1.05); }
        }
        
        /* Premium Glassmorphism */
        .glass-panel {
            background: rgba(17, 24, 39, 0.65) !important;
            backdrop-filter: blur(16px) saturate(120%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(120%) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3) !important;
        }
        .bento-card {
            background: rgba(17, 24, 39, 0.65) !important;
            backdrop-filter: blur(16px) saturate(120%) !important;
            -webkit-backdrop-filter: blur(16px) saturate(120%) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3) !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }
        .bento-card:hover {
            border-color: rgba(255, 255, 255, 0.2) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(59, 130, 246, 0.15) !important;
        }
        
        /* Sidebar styling */
        aside {
            background: rgba(11, 15, 25, 0.85) !important;
            backdrop-filter: blur(20px) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
        }
        
        /* Header styling */
        header {
            background: rgba(11, 15, 25, 0.8) !important;
            backdrop-filter: blur(20px) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
        }
'''

for filepath in glob.glob('app/templates/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. Update primary colors in tailwind config to be more vibrant
    if '"primary": "#b8c4ff"' in content:
        content = content.replace('"primary": "#b8c4ff"', '"primary": "#60A5FA"')
        content = content.replace('"primary-container": "#1e40af"', '"primary-container": "#2563EB"')
        content = content.replace('"on-primary": "#002584"', '"on-primary": "#ffffff"')
        content = content.replace('"secondary": "#7bd0ff"', '"secondary": "#2DD4BF"')
        modified = True
        
    # 2. Add mesh-bg div right after body
    if '<body ' in content and 'mesh-bg' not in content:
        content = re.sub(r'(<body[^>]*>)', r'\1\n<div class="mesh-bg"></div>', content, count=1)
        modified = True
        
    # 3. Add CSS
    if 'mesh-bg' not in content or modified:
        if '/* Animated Mesh Background */' not in content:
            content = content.replace('</style>', css_addition + '\n</style>', 1)
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {filepath}')
