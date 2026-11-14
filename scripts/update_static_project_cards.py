import re

with open("founder.zinoingroup.in/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Generate new static project cards from data/projects.json
import json
with open("founder.zinoingroup.in/data/projects.json", "r", encoding="utf-8") as f:
    projects_data = json.load(f)["projects"]

cards_html = []
for p in projects_data:
    badge_html = f'<span class="project__badge-pill" style="{p.get("badgeStyle", "")}">{p.get("badge", "")}</span>' if p.get("badge") else ''
    
    tags_html = ""
    for t in p.get("technologies", []):
        tags_html += f'<span class="tech-pill">{t}</span>\n                            '

    actions_html = ""
    for a in p.get("actions", []):
        if a.get("type") == "link":
            actions_html += f"""<a href="{a.get('url')}" target="_blank" rel="noopener noreferrer" class="button button--small {a.get('buttonClass', 'button--secondary')}" aria-label="{a.get('ariaLabel', a.get('label'))}">
                                <i class='{a.get('icon', 'bx bx-link')}' aria-hidden="true"></i> {a.get('label')}
                            </a>\n                            """
        elif a.get("type") == "pill":
            actions_html += f"""<span class="tech-pill" style="{a.get('pillStyle', '')}">
                                <i class='{a.get('icon', 'bx bx-time')}' aria-hidden="true"></i> {a.get('label')}
                            </span>\n                            """

    tagline_html = f'<p class="project__tagline">{p.get("tagline")}</p>' if p.get("tagline") else ''

    card = f"""                <!-- Project: {p['title']} -->
                <div class="project__card scroll-animate">
                    <div class="project__icon-wrapper">
                        <div class="project__icon-box">
                            <i class='{p.get("icon", "bx bx-code-alt")}' aria-hidden="true"></i>
                        </div>
                        {badge_html}
                    </div>
                    <div class="project__content">
                        <h3 class="project__title">{p['title']}</h3>
                        {tagline_html}
                        <p class="project__desc">
                            {p['description']}
                        </p>
                        <div class="project__tech-tags">
                            {tags_html.strip()}
                        </div>
                        <div class="project__actions">
                            {actions_html.strip()}
                        </div>
                    </div>
                </div>"""
    cards_html.append(card)

new_projects_grid = '\n\n'.join(cards_html)

# Replace the inner grid of #projects
old_grid_pattern = r'(<section class="projects section" id="projects"[^>]*>[\s\S]*?<div class="projects__grid bd-grid">)([\s\S]*?)(</div>\s*</section>)'
match = re.search(old_grid_pattern, html)
if match:
    updated_section = match.group(1) + '\n' + new_projects_grid + '\n            ' + match.group(3)
    html = html[:match.start()] + updated_section + html[match.end():]
    with open("founder.zinoingroup.in/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully replaced static project cards in index.html with icon-based cards!")
else:
    print("Could not find projects grid pattern!")

