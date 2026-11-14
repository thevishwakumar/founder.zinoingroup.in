import json, re

# Load JSONs
with open('founder.zinoingroup.in/data/projects.json', 'r', encoding='utf-8') as f:
    projects_data = json.load(f)['projects']

with open('founder.zinoingroup.in/data/expertise.json', 'r', encoding='utf-8') as f:
    expertise_data = json.load(f)['categories']

with open('founder.zinoingroup.in/data/certifications.json', 'r', encoding='utf-8') as f:
    certifications_data = json.load(f)['certifications']

with open('founder.zinoingroup.in/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Build Static Projects HTML
proj_html_cards = []
for p in projects_data:
    tags_html = "".join([f'<span class="tech-pill">{t}</span>' for t in p.get('technologies', [])])
    
    actions_html = []
    for a in p.get('actions', []):
        if a.get('type') == 'link' and a.get('url'):
            actions_html.append(
                f'<a href="{a["url"]}" target="_blank" rel="noopener noreferrer" class="button button--small {a.get("buttonClass", "")}" aria-label="{a.get("ariaLabel", a["label"])}">'
                f'{a["label"]} <i class="{a.get("icon", "bx bx-right-arrow-alt")}" aria-hidden="true"></i></a>'
            )
        elif a.get('type') == 'pill':
            actions_html.append(
                f'<span class="button--small" style="{a.get("pillStyle", "")}">'
                f'<i class="{a.get("icon", "bx bx-time")}" aria-hidden="true"></i> {a["label"]}</span>'
            )
    actions_str = "\n                            ".join(actions_html)
    
    card = f"""                    <div class="project__card scroll-animate">
                        <div class="project__icon-wrapper">
                            <div class="project__icon-box">
                                <i class='{p.get("icon", "bx bx-folder")}' aria-hidden="true"></i>
                            </div>
                            <span class="project__badge-pill" style="{p.get("badgeStyle", "")}">{p.get("badge", "")}</span>
                        </div>
                        <div class="project__content">
                            <h3 class="project__title">{p["title"]}</h3>
                            <span class="project__tagline">{p.get("tagline", "")}</span>
                            <p class="project__desc">{p.get("description", "")}</p>
                            <div class="project__tech-tags">
                                {tags_html}
                            </div>
                            <div class="project__actions">
                                {actions_str}
                            </div>
                        </div>
                    </div>"""
    proj_html_cards.append(card)

new_projects_grid_inner = "\n" + "\n\n".join(proj_html_cards) + "\n                "

# Replace in index.html
proj_pattern = r'(<div class="projects__grid bd-grid">)([\s\S]*?)(</div>\s*</section>)'
match_proj = re.search(proj_pattern, html)
assert match_proj, "Could not find projects__grid in index.html"
html = re.sub(proj_pattern, r'\g<1>' + new_projects_grid_inner.replace('\\', '\\\\') + r'\g<3>', html, count=1)
print(f"Rendered {len(projects_data)} static project cards into index.html!")

# 2. Build Static Expertise HTML
exp_html_cards = []
for c in expertise_data:
    items_html = "\n".join([f'                        <li class="expertise__item"><i class="bx bx-check-circle" aria-hidden="true"></i> <span>{s}</span></li>' for s in c.get('skills', [])])
    card = f"""                <div class="expertise__card scroll-animate">
                    <div class="expertise__icon" aria-hidden="true">
                        <i class='{c.get("icon", "bx bx-check")}'></i>
                    </div>
                    <h3 class="expertise__title">{c["title"]}</h3>
                    <ul class="expertise__list">
{items_html}
                    </ul>
                </div>"""
    exp_html_cards.append(card)

new_exp_grid_inner = "\n" + "\n".join(exp_html_cards) + "\n            "
exp_pattern = r'(<div class="expertise__grid bd-grid">)([\s\S]*?)(</div>\s*</section>)'
match_exp = re.search(exp_pattern, html)
assert match_exp, "Could not find expertise__grid in index.html"
html = re.sub(exp_pattern, r'\g<1>' + new_exp_grid_inner.replace('\\', '\\\\') + r'\g<3>', html, count=1)
print(f"Rendered {len(expertise_data)} static expertise categories into index.html!")

# 3. Build Static Certifications HTML
cert_html_cards = []
for c in certifications_data:
    link_html = ""
    if c.get('link') and c['link'].get('url'):
        link_html = f'<a href="{c["link"]["url"]}" target="_blank" rel="noopener noreferrer" class="certificate__link" title="{c["link"].get("title", "")}">{c["link"].get("text", "Verify")} <i class="bx bx-link-external" aria-hidden="true"></i></a>'
    elif c.get('footerLabel'):
        link_html = f'<span class="certificate__status">{c["footerLabel"]}</span>'
    else:
        link_html = f'<span class="certificate__status">{c.get("status", "Verified")}</span>'
        
    card = f"""                <div class="certificate__card scroll-animate">
                    <div>
                        <div class="certificate__header">
                            <i class='{c.get("orgIcon", "bx bx-award")} certificate__icon' aria-hidden="true"></i>
                            <span class="certificate__verified"><i class="bx bx-check" aria-hidden="true"></i> {c.get("status", "Verified")}</span>
                        </div>
                        <h3 class="certificate__title">{c["title"]}</h3>
                        <span class="certificate__org">{c["organization"]}</span>
                    </div>
                    <div class="certificate__footer">
                        {link_html}
                    </div>
                </div>"""
    cert_html_cards.append(card)

new_cert_grid_inner = "\n" + "\n".join(cert_html_cards) + "\n            "
cert_pattern = r'(<div class="certifications__grid bd-grid">)([\s\S]*?)(</div>\s*</section>)'
match_cert = re.search(cert_pattern, html)
assert match_cert, "Could not find certifications__grid in index.html"
html = re.sub(cert_pattern, r'\g<1>' + new_cert_grid_inner.replace('\\', '\\\\') + r'\g<3>', html, count=1)
print(f"Rendered {len(certifications_data)} static certification cards into index.html!")

with open('founder.zinoingroup.in/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html static fallbacks successfully synchronized!")
