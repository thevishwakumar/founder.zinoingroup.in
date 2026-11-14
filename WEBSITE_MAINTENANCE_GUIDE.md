# WEBSITE MAINTENANCE & OPERATIONS GUIDE

**Website:** [founder.zinoingroup.in](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date:** November 14, 2026  
**Audience:** Site Owner, Frontend Engineers & Release Managers  
**Status:** **ACTIVE OPERATIONAL HANDBOOK**

---

## 1. Quick Start: Local Testing & Validation

### 1.1 Running the Quality Validation Suite
Before publishing any changes or committing to Git, run the automated quality validation script in PowerShell:

```powershell
python scripts/validate_site.py
```

**Expected Output:**
```
======================================================================
 VISHWA K — FOUNDER PORTFOLIO QUALITY & CONTENT VALIDATION
 Target Site: ...\founder.zinoingroup.in
======================================================================
--- PASSED CHECKS ---
  [PASS] [Content] Valid JSON syntax: profile.json
  [PASS] [Content] Zero placeholders in profile.json
  ...
======================================================================
 SUMMARY: Total Checks: 37 | Passed: 37 | Warnings: 0 | Errors: 0
 FINAL STATUS: PASSED
======================================================================
```
- If the script outputs `FINAL STATUS: PASSED` (Exit Code 0), the site is safe to commit.
- If any `[FAIL]` items appear, resolve them before committing.

---

### 1.2 Running the Local Preview Server
To preview the website locally on your computer:
```powershell
python -m http.server 8080 --directory "founder.zinoingroup.in"
```
Open your browser and navigate to:
```
http://localhost:8080/
```

---

## 2. Content Maintenance Workflows

All editable website content is located in the `founder.zinoingroup.in/data/` folder:

| Content Area | Target File | What You Can Edit |
|---|---|---|
| **Personal Bio & Headlines** | `data/profile.json` | Name, role, organization, typing headline titles, bio paragraphs, contact email. |
| **Technical Skills** | `data/expertise.json` | 4 expertise categories, icons, and individual skill items. |
| **Featured Projects** | `data/projects.json` | Project titles, taglines, descriptions, badges, tech stack pills, and GitHub / demo links. |
| **Professional Experience** | `data/experience.json` | Roles, company names, dates, status badges, bullet achievements, and technologies. |
| **Academic Milestones** | `data/education.json` | Degree name, college/school, graduation years, CGPA/marks, and pursuit status. |
| **Certifications** | `data/certifications.json` | Certificate titles, issuing bodies, credential IDs, and verification URLs. |
| **Social Links** | `data/social-links.json` | LinkedIn, GitHub, Instagram, Email, and Website URLs. |

*Detailed step-by-step editing instructions with code samples are documented in [CONTENT_UPDATE_GUIDE.md](file:///c:/Users/Vishw/Downloads/founder.zinoingroup.in/CONTENT_UPDATE_GUIDE.md).*

---

## 3. Asset Management Guidelines

To preserve fast page loads and avoid layout shifts:

1. **Photographs & Screenshots:**
   - Always convert images to modern **WebP** format.
   - Recommended dimensions for project card previews: **760 × 420 px** (2x Retina for 380 × 210 display).
   - Target file size: **$\le 50\text{ KB}$**.
2. **Architecture Diagrams & Logos:**
   - Use clean, vector **SVG** format (`project-documind.svg`, `project-campusbridge.svg`).
   - Clean up inline styles and ensure `viewBox` is declared.
3. **Asset Directory:**
   - Place all images in `founder.zinoingroup.in/assets/img/`.
   - Never reference external image hosting URLs (Imgur, Cloudinary) to avoid third-party DNS lookups and broken links.

---

## 4. Security & Privacy Hygiene

1. **Web3Forms Access Key Protection:**
   - The public access key (`eb8f26d7-359a-4d92-a252-7851ef76b341`) is locked via client-side honeypot (`name="botcheck"`).
   - Log into the [Web3Forms Dashboard](https://web3forms.com/) and verify domain whitelisting is locked strictly to `founder.zinoingroup.in`.
2. **Zero Form Data Telemetry:**
   - The contact form transmits directly to Web3Forms over TLS 1.3 encryption.
   - **Never** add form input values to analytics or logs.
3. **Cookieless Analytics:**
   - The site uses cookieless Cloudflare Web Analytics. No cookie consent banner is needed.

---

## 5. Cloudflare Pages Deployment & Release Hygiene

### 5.1 Pre-Deployment Routine
```powershell
# 1. Run automated quality validation
python scripts/validate_site.py

# 2. Check git status
git status

# 3. Stage verified changes
git add founder.zinoingroup.in/ data/

# 4. Commit with descriptive message
git commit -m "feat(content): update featured project details and skills"

# 5. Push to GitHub master branch (triggers Cloudflare Pages build)
git push origin master
```

### 5.2 Rollback Protocol
If an unintended change is published to production:
1. Log into the Cloudflare Dashboard $\rightarrow$ Pages $\rightarrow$ `founder-zinoingroup`.
2. Navigate to **Deployments**.
3. Select the previous stable deployment and click **Rollback to this deployment**.
4. The previous version is restored globally within seconds.

---

## 6. Troubleshooting Common Issues

### Issue 1: Website shows old content after updating JSON
- **Cause:** Browser HTTP cache or Cloudflare edge cache.
- **Solution:** Press `Ctrl + F5` (hard reload) in browser. In Cloudflare Dashboard, click **Purge Everything** under Caching if needed.

### Issue 2: `python scripts/validate_site.py` reports JSON Syntax Error
- **Cause:** Missing comma, trailing comma, or unescaped quote in JSON file.
- **Solution:** Open the reported JSON file in VS Code. Red squiggly lines will indicate the exact line number. Remove the trailing comma or wrap quotes in `\"`.

### Issue 3: Local preview server reports 501 on `/cdn-cgi/rum`
- **Cause:** Cloudflare's Web Analytics beacon script attempts to POST performance telemetry to `/cdn-cgi/rum`, which the simple Python dev server does not handle.
- **Solution:** Completely normal for local dev. On production Cloudflare Pages, the edge handles this automatically.

---

*Refer to [QUALITY_CHECKLIST.md](file:///c:/Users/Vishw/Downloads/founder.zinoingroup.in/QUALITY_CHECKLIST.md) for the pre-publish quality checklist.*
