import re

with open('founder.zinoingroup.in/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<[a-z0-9]+[^>]*class="[^"]*scroll-animate[^"]*"[^>]*>', text)
print(f'Total elements with scroll-animate in HTML: {len(matches)}')
for m in matches[:15]:
    print(' ', m[:110])
