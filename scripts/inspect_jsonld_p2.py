with open("founder.zinoingroup.in/index.html", encoding="utf-8") as f:
    text = f.read()

import re
scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.DOTALL)
if scripts:
    print(scripts[0][1000:3000])
