with open("founder.zinoingroup.in/index.html.bak", encoding="utf-8", errors="ignore") as f:
    text = f.read()

import re
skills_section = re.search(r'<section[^>]*id=[\'"]skills[\'"][^>]*>.*?</section>', text, re.DOTALL)
if skills_section:
    items = re.findall(r'<div class="skill-item[^"]*">\s*<i class=[\'"]([^\'"]+)[\'"][^>]*></i>\s*<span>(.*?)</span>', skills_section.group(0))
    for icon, name in items:
        print(f"Skill: {name} (Icon: {icon})")

