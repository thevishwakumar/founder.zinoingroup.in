import re

with open('live_production_snapshot.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>([\s\S]*?)</section>', text)
for sec_id, content in sections:
    print(f"Section ID: #{sec_id} ({len(content)} chars)")
    h = re.findall(r'<h[23][^>]*>([^<]+)</h[23]>', content)
    print("  Headings:", h[:8])

