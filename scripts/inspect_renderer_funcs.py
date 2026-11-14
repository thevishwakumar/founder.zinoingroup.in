with open("founder.zinoingroup.in/assets/js/content-renderer.js", encoding="utf-8") as f:
    text = f.read()

import re
funcs = re.findall(r'function\s+render([A-Za-z0-9_]+)', text)
print("Render functions in content-renderer.js:", funcs)

