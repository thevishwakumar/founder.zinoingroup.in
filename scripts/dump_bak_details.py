import re

with open('founder.zinoingroup.in/index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract all certificate cards
cert_cards = re.findall(r'<div[^>]*class="[^"]*certificate__card[^"]*"[^>]*>([\s\S]*?)</div>\s*</div>', text)
print(f"Total certificate cards matched: {len(cert_cards)}")

certs = []
for c in cert_cards:
    title_m = re.search(r'<h[34][^>]*class="[^"]*certificate__title[^"]*"[^>]*>([^<]+)</h[34]>', c)
    org_m = re.search(r'<span[^>]*class="[^"]*certificate__issuer[^"]*"[^>]*>([^<]+)</span>', c)
    date_m = re.search(r'<span[^>]*class="[^"]*certificate__date[^"]*"[^>]*>([^<]+)</span>', c)
    title = title_m.group(1).strip() if title_m else ""
    org = org_m.group(1).strip() if org_m else ""
    date = date_m.group(1).strip() if date_m else ""
    certs.append({'title': title, 'issuer': org, 'date': date})

print("\n--- All Certificates in index.html.bak ---")
for i, c in enumerate(certs, 1):
    print(f"{i}. {c['title']} | Issuer: {c['issuer']} | Date: {c['date']}")

# Check skills section in bak
skills_section = re.search(r'<section[^>]*id="skills"[^>]*>([\s\S]*?)</section>', text)
if skills_section:
    print("\n--- Skills Section Content in index.html.bak ---")
    skill_names = re.findall(r'<span[^>]*class="[^"]*skills__name[^"]*"[^>]*>([^<]+)</span>', skills_section.group(1))
    if not skill_names:
        skill_names = re.findall(r'<[^>]*class="[^"]*skill[^"]*"[^>]*>([^<]+)<', skills_section.group(1))
    print("Skills extracted:", skill_names)
    print("Snippet:", skills_section.group(1)[:1000])

# Check projects in bak
print("\n--- Projects in index.html.bak ---")
proj_cards = re.findall(r'<div[^>]*class="[^"]*(?:project__card|work__card|work__img)[^"]*"[^>]*>([\s\S]*?)</div>\s*</div>', text)
for i, p in enumerate(proj_cards, 1):
    t = re.search(r'<h[234][^>]*>([^<]+)</h[234]>', p)
    desc = re.search(r'<p[^>]*>([^<]+)</p>', p)
    print(f"{i}. Title: {t.group(1) if t else 'N/A'} | Desc: {desc.group(1) if desc else 'N/A'}")

