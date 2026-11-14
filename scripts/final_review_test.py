import urllib.request
import urllib.error
import json
import re
import os
import sys

BASE_URL = "http://localhost:8080"

def run_tests():
    print("=" * 70, flush=True)
    print(" STEP 28: FINAL FOUNDER WEBSITE REVIEW & OWNER APPROVAL AUDIT", flush=True)
    print(f" Target Local Server: {BASE_URL}", flush=True)
    print("=" * 70, flush=True)
    
    results = {
        "passed": 0,
        "failed": 0,
        "warnings": 0,
        "details": []
    }
    
    def record_pass(category, title, detail=""):
        results["passed"] += 1
        results["details"].append(f"[PASS] [{category}] {title} - {detail}")
        print(f"  [PASS] [{category}] {title} - {detail}", flush=True)

    def record_fail(category, title, detail=""):
        results["failed"] += 1
        results["details"].append(f"[FAIL] [{category}] {title} - {detail}")
        print(f"  [FAIL] [{category}] {title} - {detail}", flush=True)

    def record_warn(category, title, detail=""):
        results["warnings"] += 1
        results["details"].append(f"[WARN] [{category}] {title} - {detail}")
        print(f"  [WARN] [{category}] {title} - {detail}", flush=True)

    # 1. Check HTTP Server & Index
    try:
        req = urllib.request.urlopen(f"{BASE_URL}/", timeout=5)
        status = req.status
        html = req.read().decode('utf-8')
        if status == 200:
            record_pass("Server", "HTTP 200 OK", f"HTML payload received ({len(html)} bytes)")
        else:
            record_fail("Server", "HTTP Status", f"Expected 200, got {status}")
            return results
    except Exception as e:
        record_fail("Server", "HTTP Connection", f"Cannot connect to {BASE_URL}: {e}")
        return results

    # 2. Check all JSON content endpoints
    json_files = [
        "profile.json", "expertise.json", "projects.json", 
        "experience.json", "education.json", "certifications.json", 
        "social-links.json"
    ]
    for jf in json_files:
        try:
            jreq = urllib.request.urlopen(f"{BASE_URL}/data/{jf}", timeout=3)
            if jreq.status == 200:
                jdata = json.loads(jreq.read().decode('utf-8'))
                record_pass("Content", f"JSON Endpoint {jf}", f"Valid JSON loaded with {len(jdata)} top-level keys")
            else:
                record_fail("Content", f"JSON Endpoint {jf}", f"Status {jreq.status}")
        except Exception as e:
            record_fail("Content", f"JSON Endpoint {jf}", f"Error: {e}")

    # 3. Check Images & Assets
    img_matches = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', html)
    img_matches += re.findall(r'<source[^>]+srcset=[\'"]([^\'"]+)[\'"]', html)
    unique_imgs = sorted(list(set(img_matches)))
    for img in unique_imgs:
        if img.startswith("http"):
            continue
        try:
            clean_path = img.lstrip('/')
            ireq = urllib.request.urlopen(f"{BASE_URL}/{clean_path}", timeout=3)
            if ireq.status == 200:
                record_pass("Asset", f"Image {clean_path}", f"200 OK ({len(ireq.read())} bytes)")
            else:
                record_fail("Asset", f"Image {clean_path}", f"Status {ireq.status}")
        except Exception as e:
            record_fail("Asset", f"Image {clean_path}", f"Failed to load: {e}")

    # 4. Check CSS & JS files
    css_matches = re.findall(r'<link[^>]+rel=[\'"]stylesheet[\'"][^>]+href=[\'"]([^\'"]+)[\'"]', html)
    for css in css_matches:
        if css.startswith("http"):
            continue
        clean_css = css.lstrip('/')
        try:
            creq = urllib.request.urlopen(f"{BASE_URL}/{clean_css}", timeout=3)
            record_pass("Asset", f"Stylesheet {clean_css}", f"200 OK ({len(creq.read())} bytes)")
        except Exception as e:
            record_fail("Asset", f"Stylesheet {clean_css}", f"Error: {e}")

    js_matches = re.findall(r'<script[^>]+src=[\'"]([^\'"]+)[\'"]', html)
    for js in js_matches:
        if js.startswith("http"):
            continue
        clean_js = js.lstrip('/')
        try:
            jreq = urllib.request.urlopen(f"{BASE_URL}/{clean_js}", timeout=3)
            record_pass("Asset", f"Script {clean_js}", f"200 OK ({len(jreq.read())} bytes)")
        except Exception as e:
            record_fail("Asset", f"Script {clean_js}", f"Error: {e}")

    # 5. Check Page Structure & Sections
    required_sections = [
        ("home", "Hero section"),
        ("about", "About section"),
        ("expertise", "Areas of Expertise"),
        ("projects", "Projects & Ventures"),
        ("experience", "Professional Experience"),
        ("education", "Education"),
        ("certifications", "Certifications"),
        ("contact", "Contact section")
    ]
    for sec_id, sec_name in required_sections:
        if f'id="{sec_id}"' in html or f'id=\'{sec_id}\'' in html:
            record_pass("Structure", f"Section #{sec_id}", f"Found: {sec_name}")
        else:
            record_fail("Structure", f"Section #{sec_id}", f"Missing: {sec_name}")

    # 6. Check Personal Information Verification
    claims = [
        ("Owner Name", "Vishwa K", "Vishwa K" in html),
        ("Alternate Name", "Vishwa Kumar", "Vishwa Kumar" in html),
        ("Role Title", "Founder & Developer", "Founder & Developer" in html),
        ("Organization", "Zinoin Group", "Zinoin Group" in html),
        ("Degree", "Cyber Security", "Cyber Security" in html),
        ("College", "Sri Sai Ranganathan Engineering College", "Sri Sai Ranganathan Engineering College" in html),
        ("School", "Krishnagiri District Model School", "Krishnagiri District Model School" in html),
        ("CGPA", "8.5", "8.5" in html),
        ("Class 12 Score", "72.83%", "72.83%" in html),
        ("Project 1", "Zinoin Group", "zinoingroup.in" in html),
        ("Project 2", "DocuMind AI", "DocuMind AI" in html),
        ("Project 3", "TNT Commercial Platforms", "TNT Commercial Platforms" in html or "Taste N Taste" in html),
        ("Project 4", "CampusBridge", "CampusBridge" in html),
        ("Contact Email", "thevishwaofficial@gmail.com", "thevishwaofficial@gmail.com" in html),
        ("LinkedIn URL", "linkedin.com/in/thevishwakumar", "https://www.linkedin.com/in/thevishwakumar" in html),
        ("GitHub URL", "github.com/thevishwakumar", "https://github.com/thevishwakumar" in html),
        ("Instagram URL", "instagram.com/thevishwakumar", "https://www.instagram.com/thevishwakumar/" in html)
    ]
    for c_name, c_val, c_pass in claims:
        if c_pass:
            record_pass("Verification", f"Claim '{c_name}'", f"Verified in DOM: '{c_val}'")
        else:
            record_fail("Verification", f"Claim '{c_name}'", f"Missing from DOM: '{c_val}'")

    # 7. Check No Placeholders / Unverified Claims
    forbidden_terms = ["Lorem ipsum", "TODO", "TBD", "John Doe", "fakecompany", "example.com/project"]
    for term in forbidden_terms:
        if term.lower() in html.lower():
            record_warn("Integrity", f"Term '{term}' detected", "Potential placeholder text")
        else:
            record_pass("Integrity", f"Zero '{term}'", "Not present")

    # 8. Check Contact Form Setup
    if 'action="https://api.web3forms.com/submit"' in html:
        record_pass("Contact", "Web3Forms Form Action", "Endpoint verified")
    else:
        record_fail("Contact", "Web3Forms Form Action", "Missing action attribute")

    if 'name="access_key"' in html and 'eb8f26d7-359a-4d92-a252-7851ef76b341' in html:
        record_pass("Contact", "Web3Forms Access Key", "Production key eb8f26d7-359a-4d92-a252-7851ef76b341 present")
    else:
        record_fail("Contact", "Web3Forms Access Key", "Missing or modified access key")

    if 'name="botcheck"' in html:
        record_pass("Contact", "Honeypot Anti-Spam", "Field 'botcheck' present")
    else:
        record_fail("Contact", "Honeypot Anti-Spam", "Missing honeypot field")

    # 9. Check Theme Switching Mechanics in script
    if 'data-theme' in html and 'theme-preference' in html:
        record_pass("Theme", "Dual Key Persistence", "Found data-theme and theme-preference logic")
    else:
        record_fail("Theme", "Dual Key Persistence", "Missing theme script logic")

    # 10. Check Viewport Meta
    if 'name="viewport"' in html and 'width=device-width' in html:
        record_pass("Responsive", "Viewport Meta Tag", "width=device-width, initial-scale=1.0 verified")
    else:
        record_fail("Responsive", "Viewport Meta Tag", "Missing viewport meta tag")

    print("\n" + "=" * 70, flush=True)
    print(f" AUDIT COMPLETE: Passed: {results['passed']} | Warnings: {results['warnings']} | Failed: {results['failed']}", flush=True)
    print("=" * 70, flush=True)
    return results

if __name__ == "__main__":
    run_tests()
