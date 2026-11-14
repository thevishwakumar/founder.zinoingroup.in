with open("founder.zinoingroup.in/index.html.bak", encoding="utf-8", errors="ignore") as f:
    text = f.read()

import re
matches = re.findall(r'<section[^>]*id=[\'"][^\'"]*cert[^\'"]*[\'"][^>]*>.*?</section>', text, re.DOTALL | re.IGNORECASE)
for m in matches:
    print("Found section:")
    for line in m.split('\n')[:30]:
        print(" ", line)

