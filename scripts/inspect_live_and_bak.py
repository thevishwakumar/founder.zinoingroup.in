import re, os

def inspect_file(filename):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist")
        return
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"\n==================== {filename} ({len(text)} bytes) ====================")
    
    # Sections
    sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', text)
    print("Sections found:", sections)
    
    # Project titles
    proj_titles = re.findall(r'<h3[^>]*class="[^"]*project__title[^"]*"[^>]*>([^<]+)</h3>', text)
    if not proj_titles:
        proj_titles = re.findall(r'<h[234][^>]*>([^<]*(?:Project|Platform|AI|Zinoin|TNT|Docu|Fashion|Medi)[^<]*)</h[234]>', text)
    print("Projects:", proj_titles)
    
    # Certification titles
    cert_titles = re.findall(r'<h[34][^>]*class="[^"]*certificate__title[^"]*"[^>]*>([^<]+)</h[34]>', text)
    if not cert_titles:
        cert_matches = re.findall(r'<div[^>]*class="[^"]*certificate__card[^"]*"[^>]*>[\s\S]*?<h[34][^>]*>([^<]+)</h[34]>', text)
        cert_titles = cert_matches
    print(f"Certificates count: {len(cert_titles)}")
    for c in cert_titles[:10]:
        print("  -", c.strip())
        
    # Skills
    skills = re.findall(r'<span[^>]*class="[^"]*skills__name[^"]*"[^>]*>([^<]+)</span>', text)
    if not skills:
        skills = re.findall(r'<span[^>]*class="[^"]*tech-pill[^"]*"[^>]*>([^<]+)</span>', text)
    print(f"Skills count: {len(skills)}")
    print("Skills sample:", list(set(skills))[:15])

inspect_file('live_production_snapshot.html')
inspect_file('founder.zinoingroup.in/index.html.bak')
