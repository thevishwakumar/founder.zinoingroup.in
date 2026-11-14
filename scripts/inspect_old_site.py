import os, re

files = [
    "founder.zinoingroup.in/index.html.bak",
    "founder.zinoingroup.in/index.html.pre-step14",
    "founder.zinoingroup.in/index.html.pre-step17",
    "founder.zinoingroup.in/index.html.pre-step18",
    "live_production_snapshot.html"
]

for fpath in files:
    if os.path.exists(fpath):
        print(f"==================== {fpath} ====================")
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        # Search for certificates
        certs = re.findall(r'<div[^>]*class=[\'"][^\'"]*certificate[^\'"]*[\'"][^>]*>.*?(?=</div>\s*</div>|</div>\s*<div class=[\'"][^\'"]*certificate|$)', content, re.DOTALL | re.IGNORECASE)
        print(f"Certificates found: {len(certs)}")
        for c in certs[:5]:
            title = re.search(r'<h[2-4][^>]*>(.*?)</h[2-4]>', c)
            if title:
                print(f"  Cert: {title.group(1).strip()}")
        
        # Search for skills
        skills = re.findall(r'<div[^>]*class=[\'"][^\'"]*skills__[^\'"]*[\'"][^>]*>.*?(?=</div>\s*</div>|$)', content, re.DOTALL | re.IGNORECASE)
        print(f"Skills blocks: {len(skills)}")

        # Search for projects
        projs = re.findall(r'<div[^>]*class=[\'"][^\'"]*project[^\'"]*[\'"][^>]*>.*?(?=</div>\s*</div>|$)', content, re.DOTALL | re.IGNORECASE)
        print(f"Projects found: {len(projs)}")
        for p in projs[:5]:
            title = re.search(r'<h[2-4][^>]*>(.*?)</h[2-4]>', p)
            if title:
                print(f"  Project: {title.group(1).strip()}")

