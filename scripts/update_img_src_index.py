import re

with open("founder.zinoingroup.in/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Vishwaimg/Screenshot_...png with vishwa-...jpg
replacements = {
    'assets/img/Vishwaimg/Screenshot_2026_1114_091424.png': 'assets/img/vishwa-ceo-full.jpg',
    'assets/img/Vishwaimg/Screenshot_2026_1114_085830.png': 'assets/img/vishwa-executive-standing.jpg',
    'assets/img/Vishwaimg/Screenshot_2026_1114_085759.png': 'assets/img/vishwa-executive-seated.jpg',
    'assets/img/Vishwaimg/Screenshot_2026_1114_090009.png': 'assets/img/vishwa-business-strategy.jpg',
    'assets/img/Vishwaimg/Screenshot_2026_1114_085900.png': 'assets/img/vishwa-window-skyline.jpg'
}

for old, new in replacements.items():
    if old in html:
        html = html.replace(old, new)
        print(f"Replaced {old} -> {new}")

# Update #contact in static project cards to https://founder.zinoingroup.in/#contact
html = html.replace('href="#contact"', 'href="https://founder.zinoingroup.in/#contact"')
# but restore the internal nav link to #contact
html = html.replace('<li><a href="https://founder.zinoingroup.in/#contact" class="footer__nav-link">Contact</a></li>', '<li><a href="#contact" class="footer__nav-link">Contact</a></li>')
html = html.replace('<a href="https://founder.zinoingroup.in/#contact" class="nav__link">Contact</a>', '<a href="#contact" class="nav__link">Contact</a>')

with open("founder.zinoingroup.in/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated image src and contact links in index.html")

