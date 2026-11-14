with open("live_production_snapshot.html", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

import re
m_jotform = re.findall(r'jotform', text, re.I)
m_web3 = re.findall(r'web3forms', text, re.I)
print(f"Jotform occurrences on live site: {len(m_jotform)}")
print(f"Web3Forms occurrences on live site: {len(m_web3)}")

form_match = re.search(r'<form[^>]*>.*?</form>', text, re.DOTALL)
if form_match:
    print("Live Form tag:")
    print(form_match.group(0)[:500])
