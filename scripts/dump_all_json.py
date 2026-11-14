import json, glob, os

files = ['profile.json', 'projects.json', 'experience.json', 'education.json', 'certifications.json', 'social-links.json']

for fname in files:
    fpath = os.path.join("founder.zinoingroup.in", "data", fname)
    with open(fpath, encoding="utf-8") as f:
        d = json.load(f)
    print(f"******************** {fname} ********************")
    print(json.dumps(d, indent=2))
