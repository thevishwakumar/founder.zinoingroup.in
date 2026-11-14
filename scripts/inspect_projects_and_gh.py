import re

with open('founder.zinoingroup.in/index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see what is inside the work section of index.html.bak
work_match = re.search(r'<section[^>]*id="work"[^>]*>([\s\S]*?)</section>', text)
if work_match:
    print("=== WORK SECTION IN INDEX.HTML.BAK ===")
    print(work_match.group(1))

# Also check GITHUB_PORTFOLIO_AUDIT.md
if True:
    with open('GITHUB_PORTFOLIO_AUDIT.md', 'r', encoding='utf-8') as f:
        gh_text = f.read()
    print("\n=== GITHUB_PORTFOLIO_AUDIT.MD SUMMARY ===")
    print(gh_text[:2000])

