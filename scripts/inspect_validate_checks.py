with open("scripts/validate_site.py", encoding="utf-8") as f:
    text = f.read()

import re
checks = re.findall(r'def validate_([a-zA-Z0-9_]+)', text)
print("Validation functions:", checks)
for line in text.split('\n'):
    if "count" in line.lower() or "projects" in line.lower() or "certifications" in line.lower():
        print(" ", line.strip())

