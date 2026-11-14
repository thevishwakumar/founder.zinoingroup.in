import re

with open("founder.zinoingroup.in/index.html.bak", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Let's find the certificates section
cert_match = re.search(r'<section[^>]*id=[\'"]certifications[\'"][^>]*>.*?</section>', content, re.DOTALL)
if cert_match:
    print("=== CERTIFICATES SECTION IN INDEX.HTML.BAK ===")
    certs = re.findall(r'<div[^>]*class=[\'"][^\'"]*certificate__box[^\'"]*[\'"][^>]*>.*?(?=</div>\s*</div>|</div>\s*<div class=[\'"][^\'"]*certificate__box|$)', cert_match.group(0), re.DOTALL)
    print(f"Total certificate boxes: {len(certs)}")
    for i, c in enumerate(certs):
        # Extract h3/h4 and text
        lines = [re.sub(r'<[^>]+>', '', l).strip() for l in c.split('\n') if re.sub(r'<[^>]+>', '', l).strip()]
        print(f"{i+1}: {' | '.join(lines)}")

# Let's find the skills section
skills_match = re.search(r'<section[^>]*id=[\'"]skills[\'"][^>]*>.*?</section>', content, re.DOTALL)
if skills_match:
    print("\n=== SKILLS SECTION IN INDEX.HTML.BAK ===")
    print(re.sub(r'<[^>]+>', '\n', skills_match.group(0))[:2000])

