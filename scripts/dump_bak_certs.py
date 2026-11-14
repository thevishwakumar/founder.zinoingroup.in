import re

with open("founder.zinoingroup.in/index.html.bak", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Certificates
cert_section = re.search(r'<section[^>]*id=[\'"]certificates[\'"][^>]*>.*?</section>', text, re.DOTALL)
if cert_section:
    items = re.findall(r'<div class="certificate__item[^"]*">(.*?)</div>\s*(?=<div class="certificate__item|</div>\s*</section>|$)', cert_section.group(0), re.DOTALL)
    print(f"Total certificate items found: {len(items)}")
    for i, it in enumerate(items):
        t = re.search(r'<h3[^>]*>(.*?)</h3>', it)
        o = re.search(r'<p class="certificate__org">(.*?)</p>', it)
        title = t.group(1).strip() if t else ""
        org = o.group(1).strip() if o else ""
        print(f"{i+1}. {title} | {org}")

# Skills
skills_section = re.search(r'<section[^>]*id=[\'"]skills[\'"][^>]*>.*?</section>', text, re.DOTALL)
if skills_section:
    skills = re.findall(r'<span class="skills__name">(.*?)</span>', skills_section.group(0))
    print(f"\nTotal skills found: {len(skills)}")
    print(skills)

