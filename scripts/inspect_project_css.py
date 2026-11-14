with open("founder.zinoingroup.in/index.html", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'\.project__[a-zA-Z0-9_-]+\s*\{[^}]+\}', text)
for m in matches[:10]:
    print(m)
    print("-" * 40)

