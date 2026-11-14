with open('founder.zinoingroup.in/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find header HTML
nav_match = re.search(r'<header[^>]*class="[^"]*l-header[^"]*"[^>]*>([\s\S]*?)</header>', text)
if nav_match:
    print("=== HEADER HTML ===")
    print(nav_match.group(0)[:1500])

# Find nav CSS
print("\n=== NAV CSS SNIPPETS ===")
for m in re.finditer(r'(\.nav[^{]*\{[^}]+\})', text):
    print(m.group(0)[:120])
