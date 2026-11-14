import re

with open('founder.zinoingroup.in/index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

certs_sec = re.search(r'<section[^>]*id="certificates"[^>]*>([\s\S]*?)</section>', text)
if certs_sec:
    items = re.findall(r'<div[^>]*class="[^"]*certificate__item[^"]*"[^>]*>([\s\S]*?)</div>', certs_sec.group(1))
    print(f"Total certificate__item matches: {len(items)}")
    for i, it in enumerate(items, 1):
        t = re.search(r'<h3[^>]*class="[^"]*certificate__title[^"]*"[^>]*>([^<]+)</h3>', it)
        org = re.search(r'<p[^>]*class="[^"]*certificate__org[^"]*"[^>]*>([^<]+)</p>', it)
        date = re.search(r'<p[^>]*class="[^"]*certificate__date[^"]*"[^>]*>([^<]*)</p>', it)
        title_str = t.group(1).strip() if t else ""
        org_str = org.group(1).strip() if org else ""
        date_str = date.group(1).strip() if date else ""
        print(f"{i:2d}. {title_str} | {org_str} | {date_str}")

