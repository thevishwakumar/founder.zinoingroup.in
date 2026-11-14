with open("founder.zinoingroup.in/index.html", encoding="utf-8") as f:
    text = f.read()

import re
scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.DOTALL)
print(f"Found {len(scripts)} JSON-LD blocks:")
for i, s in enumerate(scripts):
    print(f"--- Block {i+1} ---")
    print(s[:1000])
