import re
import json

with open("founder.zinoingroup.in/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update #expertise section
with open("founder.zinoingroup.in/data/expertise.json", "r", encoding="utf-8") as f:
    expertise_data = json.load(f)["categories"]

exp_cards = []
for cat in expertise_data:
    skills_li = "\n".join([f'                        <li class="expertise__item"><i class="bx bx-check" aria-hidden="true"></i> {s}</li>' for s in cat["skills"]])
    card = f"""                <!-- Category: {cat['title']} -->
                <div class="expertise__card scroll-animate">
                    <div class="expertise__icon" aria-hidden="true">
                        <i class='{cat.get("icon", "bx bx-code-alt")}'></i>
                    </div>
                    <h3 class="expertise__card-title">{cat['title']}</h3>
                    <ul class="expertise__list">
{skills_li}
                    </ul>
                </div>"""
    exp_cards.append(card)

new_exp_grid = "\n\n".join(exp_cards)

old_exp_pattern = r'(<section class="expertise section" id="expertise"[^>]*>[\s\S]*?<div class="expertise__grid bd-grid">)([\s\S]*?)(</div>\s*</section>)'
match_exp = re.search(old_exp_pattern, html)
if match_exp:
    updated_exp = match_exp.group(1) + '\n' + new_exp_grid + '\n            ' + match_exp.group(3)
    html = html[:match_exp.start()] + updated_exp + html[match_exp.end():]
    print("Updated static expertise grid in index.html")
else:
    print("Could not match expertise grid!")

# 2. Update #certifications section
with open("founder.zinoingroup.in/data/certifications.json", "r", encoding="utf-8") as f:
    certs_data = json.load(f)["certifications"]

cert_cards = []
for c in certs_data:
    link_html = ""
    if c.get("link"):
        link_html = f"""<a href="{c['link']['url']}" target="_blank" rel="noopener noreferrer" class="certificate__link" title="{c['link'].get('title', c['title'])}">
                                {c['link'].get('text', 'Verify Certificate')} <i class='bx bx-external-link'></i>
                            </a>"""
    elif c.get("footerLabel"):
        link_html = f"<span>{c['footerLabel']}</span>"

    status_html = f"""<span class="certificate__status-verified">
                            <i class='bx bx-check-circle'></i> {c.get('status', 'Verified')}
                        </span>""" if c.get("status") else ""

    card = f"""                <!-- Certificate: {c['title']} -->
                <div class="certificate__card scroll-animate">
                    <div>
                        <div class="certificate__org-badge">
                            <i class='{c.get("orgIcon", "bx bx-award")}'></i> {c['organization']}
                        </div>
                        <h3 class="certificate__card-title">{c['title']}</h3>
                    </div>
                    <div class="certificate__footer">
                        {link_html}
                        {status_html}
                    </div>
                </div>"""
    cert_cards.append(card)

new_certs_grid = "\n\n".join(cert_cards)

old_cert_pattern = r'(<section class="certifications section" id="certifications"[^>]*>[\s\S]*?<div class="certifications__grid bd-grid">)([\s\S]*?)(</div>\s*</section>)'
match_cert = re.search(old_cert_pattern, html)
if match_cert:
    updated_cert = match_cert.group(1) + '\n' + new_certs_grid + '\n            ' + match_cert.group(3)
    html = html[:match_cert.start()] + updated_cert + html[match_cert.end():]
    print("Updated static certifications grid in index.html")
else:
    print("Could not match certifications grid!")

with open("founder.zinoingroup.in/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Saved index.html successfully!")

