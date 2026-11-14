import re

with open('founder.zinoingroup.in/assets/js/content-renderer.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'className:\s*[\'"][^\'"]*scroll-animate[^\'"]*[\'"]', text)
print(f'scroll-animate instances in content-renderer: {len(matches)}')
for m in matches:
    print(' ', m)

