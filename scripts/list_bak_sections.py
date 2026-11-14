import re

with open('founder.zinoingroup.in/index.html.bak', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all section tags in index.html.bak
sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>([\s\S]*?)</section>', text)
for sec_id, content in sections:
    print(f"Section ID: #{sec_id} ({len(content)} chars)")
    # Print h2 or h3
    h = re.findall(r'<h[23][^>]*>([^<]+)</h[23]>', content)
    print("  Headings:", h[:8])

