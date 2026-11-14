import re

with open('founder.zinoingroup.in/index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract skills
skills = re.findall(r'<div[^>]*class="[^"]*skill-item[^"]*"[^>]*>\s*<i[^>]*class=[\'"]([^\'"]*)[\'"][^>]*></i>\s*<span>([^<]+)</span>', text)
print(f"--- All Skills in index.html.bak ({len(skills)}) ---")
for icon, name in skills:
    print(f"  - {name.strip()} (icon: {icon})")

# Extract certificates
certs_sec = re.search(r'<section[^>]*id="certificates"[^>]*>([\s\S]*?)</section>', text)
if certs_sec:
    certs = re.findall(r'<div[^>]*class="[^"]*certificate-item[^"]*"[^>]*>([\s\S]*?)</div>\s*</div>', certs_sec.group(1))
    if not certs:
        # Check raw HTML in certificates section
        print("Certificates section snippet:\n", certs_sec.group(1)[:1200])

# Extract projects/works section
works_sec = re.search(r'<section[^>]*id="work"[^>]*>([\s\S]*?)</section>', text)
if not works_sec:
    works_sec = re.search(r'<section[^>]*id="projects"[^>]*>([\s\S]*?)</section>', text)
if works_sec:
    print("\n--- Work/Projects Section Snippet in index.html.bak ---")
    print(works_sec.group(1)[:1500])

