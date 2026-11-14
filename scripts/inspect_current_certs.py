import json

with open('founder.zinoingroup.in/data/certifications.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

certs = data['certifications']
print(f"Total certifications in data/certifications.json: {len(certs)}")
for i, c in enumerate(certs, 1):
    print(f"{i:2d}. {c['title']} | {c['issuer']} | {c.get('date', '')}")

