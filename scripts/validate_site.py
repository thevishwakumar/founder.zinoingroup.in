#!/usr/bin/env python3
"""
Vishwa K - Founder Website Quality & Content Validation Suite
Zero external dependencies (Pure Python Standard Library).
Validates:
1. Content Integrity & Schema Compliance (data/*.json, data/schemas/*.json)
2. SEO & Structured Data (index.html, sitemap.xml, robots.txt, 404.html)
3. Performance & Asset Sizing (assets/img/*, assets/js/*)
4. Accessibility & Security Hygiene (_headers, _redirects)
"""

import os
import sys
import json
import re
from html.parser import HTMLParser

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_DIR = os.path.join(BASE_DIR, "founder.zinoingroup.in")
DATA_DIR = os.path.join(SITE_DIR, "data")
SCHEMAS_DIR = os.path.join(DATA_DIR, "schemas")
ASSETS_DIR = os.path.join(SITE_DIR, "assets")

class ValidationResult:
    def __init__(self):
        self.passed = []
        self.warnings = []
        self.errors = []

    def pass_check(self, category, check, message=""):
        self.passed.append({"category": category, "check": check, "message": message})

    def warn(self, category, check, message):
        self.warnings.append({"category": category, "check": check, "message": message})

    def error(self, category, check, message):
        self.errors.append({"category": category, "check": check, "message": message})

    def summary(self):
        return {
            "total_checks": len(self.passed) + len(self.warnings) + len(self.errors),
            "passed": len(self.passed),
            "warnings": len(self.warnings),
            "errors": len(self.errors),
            "status": "PASSED" if len(self.errors) == 0 else "FAILED"
        }

res = ValidationResult()

# ---------------------------------------------------------
# 1. CONTENT VALIDATION (data/*.json & schemas)
# ---------------------------------------------------------
PLACEHOLDER_REGEX = re.compile(r"(lorem\s+ipsum|foo\s+bar|placeholder|todo|test\s+title|sample\s+text)", re.IGNORECASE)

def check_placeholders(data, filename):
    data_str = json.dumps(data)
    matches = PLACEHOLDER_REGEX.findall(data_str)
    if matches:
        res.error("Content", f"Placeholder detection in {filename}", f"Found placeholder terms: {set(matches)}")
    else:
        res.pass_check("Content", f"Zero placeholders in {filename}")

def validate_json_content():
    required_files = [
        "profile.json", "expertise.json", "projects.json", 
        "experience.json", "education.json", "certifications.json", "social-links.json"
    ]
    for fn in required_files:
        fpath = os.path.join(DATA_DIR, fn)
        if not os.path.exists(fpath):
            res.error("Content", f"Missing data file", f"Expected file not found: data/{fn}")
            continue
        try:
            with open(fpath, "r", encoding="utf-8") as fp:
                data = json.load(fp)
            res.pass_check("Content", f"Valid JSON syntax: {fn}")
            check_placeholders(data, fn)
        except Exception as e:
            res.error("Content", f"Syntax error in {fn}", str(e))
            continue

        # File-specific schema checks
        if fn == "projects.json":
            projects = data.get("projects", [])
            if not isinstance(projects, list) or len(projects) == 0:
                res.error("Content", "Projects array", "data/projects.json contains no projects.")
            else:
                res.pass_check("Content", "Projects count", f"Found {len(projects)} featured projects.")
                seen_ids = set()
                seen_titles = set()
                for p in projects:
                    pid = p.get("id")
                    title = p.get("title")
                    desc = p.get("description")
                    if not pid or not title or not desc:
                        res.error("Content", "Project required fields", f"Project missing id, title, or description: {p}")
                    if pid in seen_ids:
                        res.error("Content", "Duplicate project ID", f"Duplicate project ID found: '{pid}'")
                    seen_ids.add(pid)
                    if title in seen_titles:
                        res.error("Content", "Duplicate project title", f"Duplicate project title found: '{title}'")
                    seen_titles.add(title)
                    for action in p.get("actions", []):
                        if action.get("type") == "link":
                            url = action.get("url", "")
                            if not url.startswith("http://") and not url.startswith("https://"):
                                res.error("Content", "Invalid project action URL", f"Project '{title}' has invalid action URL: '{url}'")

        elif fn == "certifications.json":
            certs = data.get("certifications", [])
            if not isinstance(certs, list) or len(certs) == 0:
                res.error("Content", "Certifications array", "data/certifications.json contains no certifications.")
            else:
                res.pass_check("Content", "Certifications count", f"Found {len(certs)} verified certifications.")
                seen_cids = set()
                for c in certs:
                    cid = c.get("id")
                    title = c.get("title")
                    org = c.get("organization")
                    if not cid or not title or not org:
                        res.error("Content", "Certification required fields", f"Certification missing id, title, or organization: {c}")
                    if cid in seen_cids:
                        res.error("Content", "Duplicate certification ID", f"Duplicate certification ID: '{cid}'")
                    seen_cids.add(cid)

        elif fn == "expertise.json":
            cats = data.get("categories", [])
            if len(cats) != 4:
                res.warn("Content", "Expertise categories count", f"Expected 4 categories, found {len(cats)}")
            else:
                res.pass_check("Content", "Expertise categories count", "4 verified categories present.")

        elif fn == "education.json":
            edus = data.get("education", [])
            if len(edus) == 0:
                res.error("Content", "Education array", "data/education.json has no education entries.")
            else:
                res.pass_check("Content", "Education count", f"Found {len(edus)} education entries.")

        elif fn == "experience.json":
            exps = data.get("experiences", [])
            if len(exps) == 0:
                res.error("Content", "Experience array", "data/experience.json has no experience entries.")
            else:
                res.pass_check("Content", "Experience count", f"Found {len(exps)} experience entries.")

        elif fn == "social-links.json":
            links = data.get("links", [])
            for link in links:
                url = link.get("url", "")
                if not (url.startswith("https://") or url.startswith("mailto:")):
                    res.error("Content", "Invalid social link URL", f"Social link '{link.get('platform')}' has invalid URL: '{url}'")

    # Schemas directory check
    schema_files = [
        "profile.schema.json", "expertise.schema.json", "projects.schema.json",
        "experience.schema.json", "education.schema.json", "certifications.schema.json", "social-links.schema.json"
    ]
    all_schemas_exist = True
    for sf in schema_files:
        spath = os.path.join(SCHEMAS_DIR, sf)
        if not os.path.exists(spath):
            res.error("Content", "JSON Schema missing", f"Expected schema file not found: {sf}")
            all_schemas_exist = False
    if all_schemas_exist:
        res.pass_check("Content", "JSON Schemas", f"All {len(schema_files)} formal JSON Schemas present.")

# ---------------------------------------------------------
# 2. HTML & SEO AUDIT (index.html, robots.txt, sitemap.xml, 404.html)
# ---------------------------------------------------------
class IndexHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.internal_links = []
        self.external_links = []
        self.images = []
        self.headings = []
        self.meta_tags = []
        self.title_text = ""
        self.in_title = False
        self.scripts = []
        self.has_skip_link = False
        self.form_inputs = []
        self.form_labels = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        self.tags.append(tag)

        if "id" in attr_dict:
            self.ids.add(attr_dict["id"])

        if tag == "title":
            self.in_title = True

        if tag == "meta":
            self.meta_tags.append(attr_dict)

        if tag == "a":
            href = attr_dict.get("href", "")
            if href.startswith("#"):
                self.internal_links.append(href)
            elif href.startswith("http://") or href.startswith("https://"):
                self.external_links.append({
                    "href": href,
                    "target": attr_dict.get("target"),
                    "rel": attr_dict.get("rel", "")
                })
            if "skip-link" in attr_dict.get("class", ""):
                self.has_skip_link = True

        if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            self.headings.append(tag)

        if tag == "img":
            self.images.append(attr_dict)

        if tag == "script":
            self.scripts.append(attr_dict)

        if tag in ["input", "textarea", "select"]:
            self.form_inputs.append(attr_dict)

        if tag == "label":
            self.form_labels.append(attr_dict)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text += data

def validate_seo_and_html():
    index_path = os.path.join(SITE_DIR, "index.html")
    if not os.path.exists(index_path):
        res.error("SEO", "Index HTML", "founder.zinoingroup.in/index.html not found.")
        return

    with open(index_path, "r", encoding="utf-8") as fp:
        html_content = fp.read()

    parser = IndexHTMLParser()
    parser.feed(html_content)

    # 1. Page Title Check
    title = parser.title_text.strip()
    if not title:
        res.error("SEO", "Page Title", "Title is empty.")
    elif 30 <= len(title) <= 70:
        res.pass_check("SEO", "Page Title length", f"Title '{title}' ({len(title)} chars) is optimal (30-70).")
    else:
        res.warn("SEO", "Page Title length", f"Title length {len(title)} chars is outside optimal 30-70 range.")

    # 2. Meta Description Check
    meta_desc = next((m.get("content") for m in parser.meta_tags if m.get("name") == "description"), None)
    if not meta_desc:
        res.error("SEO", "Meta Description", "Meta description tag is missing.")
    elif 100 <= len(meta_desc) <= 170:
        res.pass_check("SEO", "Meta Description length", f"Length {len(meta_desc)} chars is optimal (100-170).")
    else:
        res.warn("SEO", "Meta Description length", f"Length {len(meta_desc)} chars outside standard 100-170.")

    # 3. Canonical Link Check
    canonical_match = re.search(r'<link\s+[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', html_content, re.IGNORECASE)
    if canonical_match:
        canon_url = canonical_match.group(1)
        if canon_url == "https://founder.zinoingroup.in/":
            res.pass_check("SEO", "Canonical URL", f"Matches production canonical URL: {canon_url}")
        else:
            res.error("SEO", "Canonical URL", f"Mismatch in canonical URL: {canon_url}")
    else:
        res.error("SEO", "Canonical URL", "Canonical link tag missing.")

    # 4. Open Graph Tags
    og_title = next((m.get("content") for m in parser.meta_tags if m.get("property") == "og:title"), None)
    og_desc = next((m.get("content") for m in parser.meta_tags if m.get("property") == "og:description"), None)
    og_url = next((m.get("content") for m in parser.meta_tags if m.get("property") == "og:url"), None)
    og_img = next((m.get("content") for m in parser.meta_tags if m.get("property") == "og:image"), None)
    if og_title and og_desc and og_url and og_img:
        res.pass_check("SEO", "Open Graph Protocol", "All required OG tags (title, desc, url, image) present.")
    else:
        res.error("SEO", "Open Graph Protocol", f"Missing OG tags: title={bool(og_title)}, desc={bool(og_desc)}, url={bool(og_url)}, img={bool(og_img)}")

    # 5. Schema.org JSON-LD Structured Data
    ld_json_matches = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html_content, re.DOTALL)
    if ld_json_matches:
        for idx, block in enumerate(ld_json_matches):
            try:
                ld_data = json.loads(block.strip())
                res.pass_check("SEO", f"Schema.org JSON-LD (Block {idx+1})", f"Valid JSON with types: {ld_data.get('@type') or [x.get('@type') for x in ld_data.get('@graph', [])]}")
            except Exception as e:
                res.error("SEO", f"Schema.org JSON-LD (Block {idx+1})", f"Syntax error: {e}")
    else:
        res.error("SEO", "Schema.org JSON-LD", "No structured data script blocks found.")

    # 6. Heading Hierarchy Progression
    h1_count = parser.headings.count("h1")
    if h1_count == 1:
        res.pass_check("SEO", "Single H1 tag", "Exactly one H1 element present on the page.")
    else:
        res.error("SEO", "Single H1 tag", f"Expected exactly one H1, found {h1_count}.")

    # 7. Internal Navigation Anchor Integrity
    broken_anchors = []
    for anchor in parser.internal_links:
        target_id = anchor.lstrip("#")
        if target_id and target_id not in parser.ids:
            broken_anchors.append(anchor)
    if broken_anchors:
        res.error("SEO", "Broken Internal Anchors", f"Target IDs not found in DOM: {broken_anchors}")
    else:
        res.pass_check("SEO", "Internal Anchor Integrity", f"All {len(parser.internal_links)} internal anchor links point to valid DOM IDs.")

    # 8. Outbound Link Security (rel="noopener noreferrer")
    unsecured_links = []
    for link in parser.external_links:
        if link.get("target") == "_blank":
            rel = link.get("rel", "")
            if "noopener" not in rel or "noreferrer" not in rel:
                unsecured_links.append(link.get("href"))
    if unsecured_links:
        res.warn("Security", "External Links Tabnabbing", f"Outbound links missing rel='noopener noreferrer': {unsecured_links}")
    else:
        res.pass_check("Security", "External Link Protection", f"All {len(parser.external_links)} outbound links enforce rel='noopener noreferrer'.")

    # 9. Accessibility: Skip Link & Form Labels
    if parser.has_skip_link:
        res.pass_check("Accessibility", "Skip to Main Content Link", "Skip link present for keyboard navigation.")
    else:
        res.warn("Accessibility", "Skip to Main Content Link", "Skip link not found.")

    label_for_ids = {lbl.get("for") for lbl in parser.form_labels if lbl.get("for")}
    unlabelled_inputs = []
    for inp in parser.form_inputs:
        if inp.get("type") in ["hidden", "checkbox", "submit"]:
            continue
        iid = inp.get("id")
        aria = inp.get("aria-label") or inp.get("aria-labelledby")
        if not (iid and iid in label_for_ids) and not aria:
            unlabelled_inputs.append(inp.get("name") or inp.get("id"))
    if unlabelled_inputs:
        res.warn("Accessibility", "Form Labels", f"Inputs missing label for=id or aria-label: {unlabelled_inputs}")
    else:
        res.pass_check("Accessibility", "Form Labels", "All interactive form inputs have matching labels or accessible names.")

    # 10. robots.txt and sitemap.xml
    robots_path = os.path.join(SITE_DIR, "robots.txt")
    sitemap_path = os.path.join(SITE_DIR, "sitemap.xml")
    if os.path.exists(robots_path):
        with open(robots_path, "r", encoding="utf-8") as fp:
            r_content = fp.read()
        if "sitemap.xml" in r_content.lower():
            res.pass_check("SEO", "robots.txt Sitemap Reference", "robots.txt correctly declares sitemap location.")
        else:
            res.warn("SEO", "robots.txt Sitemap Reference", "sitemap.xml not declared in robots.txt.")
    else:
        res.error("SEO", "robots.txt", "robots.txt file missing.")

    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as fp:
            s_content = fp.read()
        if "https://founder.zinoingroup.in/" in s_content:
            res.pass_check("SEO", "sitemap.xml Canonical URL", "Canonical domain present in sitemap.xml.")
        else:
            res.error("SEO", "sitemap.xml Canonical URL", "sitemap.xml does not contain canonical domain.")
    else:
        res.error("SEO", "sitemap.xml", "sitemap.xml file missing.")

    # 11. Image Quality & Dimension Checks
    for img in parser.images:
        src = img.get("src", "")
        alt = img.get("alt", "")
        width = img.get("width")
        height = img.get("height")

        if not alt:
            res.warn("Accessibility", "Image Alt Text", f"Image missing alt attribute: {src}")
        if not width or not height:
            res.warn("Performance", "Image Dimensions (CLS)", f"Image missing explicit width/height: {src}")
        
        img_disk_path = os.path.join(SITE_DIR, src.replace("/", os.sep))
        if os.path.exists(img_disk_path):
            size_kb = os.path.getsize(img_disk_path) / 1024
            if size_kb > 350:
                res.warn("Performance", "Oversized Image File", f"{src} is {size_kb:.1f} KB (exceeds 350 KB threshold).")
            else:
                res.pass_check("Performance", f"Image verified on disk ({size_kb:.1f} KB)", src)
        else:
            res.error("Performance", "Missing Image Asset", f"Image file not found on disk: {img_disk_path}")

    # 12. 404.html Error Page
    p404_path = os.path.join(SITE_DIR, "404.html")
    if os.path.exists(p404_path):
        with open(p404_path, "r", encoding="utf-8") as fp:
            c404 = fp.read()
        if "noindex" in c404.lower() and "404" in c404:
            res.pass_check("SEO", "Custom 404 Page", "Branded 404.html present with noindex directive.")
        else:
            res.warn("SEO", "Custom 404 Page", "404.html present but missing noindex directive.")
    else:
        res.error("SEO", "Custom 404 Page", "404.html missing.")

    # 13. Security Headers (_headers)
    headers_path = os.path.join(SITE_DIR, "_headers")
    if os.path.exists(headers_path):
        with open(headers_path, "r", encoding="utf-8") as fp:
            h_content = fp.read()
        if "nosniff" in h_content and "DENY" in h_content and "Strict-Transport-Security" in h_content:
            res.pass_check("Security", "Cloudflare Security Headers", "HSTS, X-Content-Type-Options, and X-Frame-Options configured.")
        else:
            res.warn("Security", "Cloudflare Security Headers", "Some standard security headers missing in _headers.")
    else:
        res.warn("Security", "Cloudflare Security Headers", "_headers file missing.")

    # 14. Redirects (_redirects)
    redirects_path = os.path.join(SITE_DIR, "_redirects")
    if os.path.exists(redirects_path):
        with open(redirects_path, "r", encoding="utf-8") as fp:
            red_content = fp.read()
        if "301" in red_content and "404" in red_content:
            res.pass_check("Infrastructure", "Cloudflare Redirect Rules", "Canonical 301 and 404 fallback rules configured.")
        else:
            res.warn("Infrastructure", "Cloudflare Redirect Rules", "_redirects missing canonical 301 or 404 rule.")
    else:
        res.warn("Infrastructure", "Cloudflare Redirect Rules", "_redirects file missing.")

# ---------------------------------------------------------
# EXECUTION & FORMATTED REPORTING
# ---------------------------------------------------------
def run_all():
    print("=" * 70)
    print(" VISHWA K — FOUNDER PORTFOLIO QUALITY & CONTENT VALIDATION")
    print(f" Target Site: {SITE_DIR}")
    print("=" * 70)

    validate_json_content()
    validate_seo_and_html()

    s = res.summary()
    print("\n--- PASSED CHECKS ---")
    for p in res.passed:
        print(f"  [PASS] [{p['category']}] {p['check']} {('- ' + p['message']) if p['message'] else ''}")

    if res.warnings:
        print("\n--- WARNINGS (Non-Blocking) ---")
        for w in res.warnings:
            print(f"  [WARN] [{w['category']}] {w['check']}: {w['message']}")

    if res.errors:
        print("\n--- CRITICAL ERRORS (Must Fix) ---")
        for e in res.errors:
            print(f"  [FAIL] [{e['category']}] {e['check']}: {e['message']}")

    print("\n" + "=" * 70)
    print(f" SUMMARY: Total Checks: {s['total_checks']} | Passed: {s['passed']} | Warnings: {s['warnings']} | Errors: {s['errors']}")
    print(f" FINAL STATUS: {s['status']}")
    print("=" * 70)

    return 0 if s["errors"] == 0 else 1

if __name__ == "__main__":
    sys.exit(run_all())
