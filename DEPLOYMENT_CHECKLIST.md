# Production Deployment Checklist & Step-by-Step Guide
**Project:** Vishwa K – Founder Website  
**Production Domain:** [https://founder.zinoingroup.in/](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date:** November 13, 2026  
**Status:** ⏸️ **PAUSED AWAITING OWNER AUTHORIZATION**  

---

> [!IMPORTANT]
> **SAFETY HOLD NOTICE**  
> In accordance with project instructions, **automatic deployment has been halted**. No files have been uploaded to external remote servers or hosting infrastructure. The website is fully prepared, tested, backed up, and staged locally in `c:\Users\Vishw\Downloads\founder.zinoingroup.in\founder.zinoingroup.in`. Deployment should only proceed upon your explicit confirmation.

---

## 1. Pre-Deployment Verification Checklist

Before publishing, verify that all quality assurance gates have passed:

- [x] **Content Accuracy:**
  - [x] Name: **Vishwa K**
  - [x] Title: **Founder & Developer at Zinoin Group**
  - [x] Degree: **B.E. Cyber Security Engineering** (Sri Sai Ranganathan Engineering College, 2024–2028, CGPA 8.5/10, Currently pursuing)
  - [x] Higher Secondary: **Krishnagiri District Model School** (72.83%)
  - [x] Outdated Bangalore address completely removed.
  - [x] Outdated second-year claims completely removed.
  - [x] Duplicate certifications purged (clean 9 verified credentials).
- [x] **Routing & Navigation:**
  - [x] All 7 section anchors (`#home`, `#about`, `#expertise`, `#education`, `#certifications`, `#projects`, `#contact`) tested and operational.
  - [x] Zero broken internal links.
  - [x] Header sticky behavior and active section highlighting functional.
  - [x] Mobile slide-out drawer navigation works seamlessly on small touchscreens.
- [x] **Accessibility & Visual Quality:**
  - [x] **100/100** Google Lighthouse Accessibility score.
  - [x] High-contrast `:focus-visible` ring across all interactive controls.
  - [x] Skip-to-content bypass link (`.skip-link`).
  - [x] Full support for `@media (prefers-reduced-motion: reduce)`.
- [x] **Search Engine Optimization (SEO):**
  - [x] **100/100** Google Lighthouse SEO score.
  - [x] Canonical URL (`https://founder.zinoingroup.in/`).
  - [x] Open Graph & Twitter Cards configured.
  - [x] Syntactically valid JSON-LD structured data (`WebSite` + `Person`).
  - [x] `robots.txt` and `sitemap.xml` generated and validated.
- [x] **Backups & Safety:**
  - [x] Complete ZIP backup created: `founder_zinoingroup_backup_predeploy.zip` (1.68 MB).
  - [x] Git repository initialized with master commit `d0e2a84`.
  - [x] Original unedited code preserved as `index.html.bak`.
  - [x] Zero sensitive secrets, passwords, or private API keys exposed.

---

## 2. Directory Inventory: What to Deploy

The production-ready site is located in the local directory:  
`c:\Users\Vishw\Downloads\founder.zinoingroup.in\founder.zinoingroup.in\`

### Deployment File Tree:
```text
founder.zinoingroup.in/
├── index.html                    <-- Modernized production HTML5 entrypoint
├── robots.txt                    <-- Search engine crawling directives
├── sitemap.xml                   <-- Canonical XML sitemap for Google Search Console
├── favicon.ico                   <-- Browser tab icon
├── assets/
│   └── img/
│       ├── zinoin-logo.webp      <-- Optimized corporate logo (35.9 KB)
│       ├── zinoin-logo.png       <-- Fallback PNG logo
│       ├── about.webp            <-- Optimized portrait (4.4 KB)
│       ├── about.jpg             <-- Fallback JPEG portrait
│       ├── project-zinoin.webp   <-- Project card media
│       ├── project-campusbridge.svg <-- Architecture diagram media
│       └── project-tnt.webp      <-- Application UI media
└── cdn-cgi/                      <-- Cloudflare static helper scripts (if applicable)
```

*(Note: Documentation `.md` files and `.bak` backup files reside in the parent directory and should NOT be uploaded to your public web server).*

---

## 3. Step-by-Step Deployment Options

Depending on your production hosting setup for `founder.zinoingroup.in`, select the appropriate method below:

### Option A: Cloudflare Pages (Direct Upload / Git)
If the subdomain is hosted via Cloudflare Pages:
1. Log in to the [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Navigate to **Workers & Pages** -> **founder-zinoingroup** (or your designated Pages project).
3. If using **Direct Upload**:
   - Click **Create a new deployment**.
   - Drag and drop the folder `c:\Users\Vishw\Downloads\founder.zinoingroup.in\founder.zinoingroup.in`.
   - Click **Deploy Site**.
4. If connected to a **GitHub Repository**:
   - Push the master commit to your remote repo:
     ```bash
     git remote add origin <your-github-repo-url>
     git branch -M main
     git push -u origin main
     ```
   - Cloudflare Pages will build and deploy automatically within 30 seconds.

### Option B: cPanel / Traditional Web Host (File Manager / SFTP)
If hosted on standard cPanel or shared hosting:
1. Connect via SFTP or open the **cPanel File Manager**.
2. Navigate to the root directory for `founder.zinoingroup.in` (typically `public_html/founder/` or similar).
3. Upload the following files from `founder.zinoingroup.in/`:
   - `index.html`
   - `robots.txt`
   - `sitemap.xml`
   - `favicon.ico`
   - `assets/` directory (including the `img/` folder with `.webp` files).
4. Verify file permissions: `644` for files, `755` for directories.

---

## 4. Post-Deployment Verification Steps

Immediately after deployment:

1. **Purge Cloudflare Cache:**
   - In Cloudflare Dashboard -> **Caching** -> **Configuration** -> Click **Purge Everything**.
   - Ensures global edge nodes serve the new `index.html` and WebP assets immediately.
2. **Verify Live HTTPS URL:**
   - Visit `https://founder.zinoingroup.in/` in an Incognito / Private browser window.
   - Verify that the browser padlock is active and that the site title reads:  
     `Vishwa K | Founder & Developer at Zinoin Group`.
3. **Test Contact Form Submission:**
   - Submit one genuine inquiry through the live contact form.
   - Confirm that the success alert appears:  
     `Thank you! Your message has been sent successfully.`
   - Confirm receipt of the inquiry email in your mailbox (`thevishwaofficial@gmail.com`).
4. **Submit Sitemap to Google Search Console:**
   - Open [Google Search Console](https://search.google.com/search-console).
   - Select property `founder.zinoingroup.in`.
   - Navigate to **Sitemaps** -> Enter `sitemap.xml` -> Click **Submit**.
5. **Inspect Social Share Previews:**
   - Test `https://founder.zinoingroup.in/` on the [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/) to ensure the rich thumbnail, title, and description render properly.

---

## 5. Emergency Rollback Plan

If unexpected issues arise after publication:

* **Instant File Rollback:**
  - Replace the live `index.html` with `index.html.bak`.
* **Full ZIP Archive Restoration:**
  - Extract `c:\Users\Vishw\Downloads\founder.zinoingroup.in\founder_zinoingroup_backup_predeploy.zip` to restore the pre-deployment state.
* **Purge Cache:**
  - Trigger a Cloudflare **Purge Everything** after rolling back files.

