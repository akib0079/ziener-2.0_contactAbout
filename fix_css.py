import re

with open('sections/page-teamwear.liquid', 'r') as f:
    content = f.read()

# 1. Update .tw-tabs-nav margin-bottom
content = re.sub(r'\.tw-tabs-nav \{[^}]*?margin-bottom:\s*40px;[^}]*?\}', 
                 '.tw-tabs-nav { display: flex; align-items: center; gap: 10px; margin-bottom: 50px; }', 
                 content)

# 2. Update .tw-page padding-bottom
content = re.sub(r'\.tw-page \{[^}]*?padding-bottom:\s*80px;[^}]*?\}', 
                 '.tw-page { width: 100%; overflow-x: hidden; color: #000; padding-bottom: 100px; }', 
                 content)

# 3. Fix icon box title alignment
# Find .tw-imp-step and replace justify-content
content = content.replace('justify-content: space-between;', 'justify-content: flex-start;')
# Find .tw-imp-step-content and add margin-top
content = content.replace('.tw-imp-step-content {\n  margin-top: auto;\n}', '.tw-imp-step-content {\n  margin-top: 70px;\n}')

with open('sections/page-teamwear.liquid', 'w') as f:
    f.write(content)
