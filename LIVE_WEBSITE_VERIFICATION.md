# LIVE WEBSITE VERIFICATION & POST-DEPLOYMENT QA PROTOCOL

**Website:** [founder.zinoingroup.in](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date:** November 14, 2026  
**Document Version:** 1.0.0  
**Status:** Comparative Live Audit & Post-Deployment Checklist

---

## 1. Live vs. Release Candidate Comparison

Prior to pushing changes live, an automated baseline comparison between the current live production website and the release candidate was performed:

| Inspection Dimension | Live Production Baseline (`https://founder.zinoingroup.in/`) | Production Release Candidate (`http://localhost:8080/`) | Evolution / Enhancement |
|---|---|---|---|
| **HTTP Status** | 200 OK (Cloudflare Edge) | 200 OK (Local Pre-Deployment) | High-availability edge delivery |
| **Page Title** | `Vishwa K - Cybersecurity & Marketing Professional` | `Vishwa K \| Founder & Developer at Zinoin Group` | Elevated founder brand positioning |
| **Meta Description** | Outdated legacy description | Optimized 159-character keyword-targeted description | Perfect Google SERP length |
| **Payload Size** | ~73.6 KB (Uncompressed HTML) | ~140.1 KB HTML + ~40 KB decoupled JSON | Fully modularized progressive architecture |
| **Theme System** | Legacy two-way toggle with potential flash | Tri-state (System / Light / Dark) with **0ms FOUC** | Complete OS-responsive theming |
| **Content System** | Hard-coded single HTML file | Progressive Static Hydration via 7 `data/*.json` files | Easy editing without touching HTML |
| **Featured Projects** | 2 legacy projects | 4 verified projects (Zinoin, DocuMind AI, TNT, CampusBridge) | Applied AI & commercial proof |
| **Asset Formats** | Legacy PNG/JPG | Modern WebP & optimized SVGs | 69% image size reduction |
| **Structured Data** | Basic schema markup | Comprehensive Schema.org `@graph` (`WebSite`, `ProfilePage`, `Person`) | Google Rich Snippet compliance |
| **Contact Form** | Web3Forms (`eb8f26d7-359a-4d92-a252-7851ef76b341`) | Web3Forms (`eb8f26d7-359a-4d92-a252-7851ef76b341`) + Honeypot + AJAX Toast | Hardened against bots; 16px iOS zoom fix |

---

## 2. Post-Deployment Verification Checklist

Execute these 14 verification steps immediately upon completing live deployment:

### 1. HTTP Status & SSL
- [ ] Open `https://founder.zinoingroup.in/` in Chrome/Edge.
- [ ] Confirm the browser address bar displays the secure lock icon (valid Cloudflare Universal SSL certificate).
- [ ] Verify `http://founder.zinoingroup.in/` automatically redirects to `https://`.

### 2. Header & Branding
- [ ] Verify the official Zinoin logo renders crisply without pixelation or layout jump.
- [ ] Verify brand name `Vishwa K` and `Founder` badge appear prominently.
- [ ] Confirm all navigation links (`Home`, `About`, `Expertise`, `Projects`, `Experience`, `Education`, `Certifications`, `Contact`) scroll smoothly to target sections.

### 3. Theme Switching & Persistence
- [ ] Click the theme toggle icon in the header.
- [ ] Switch to **Light Mode**: Confirm crisp white background, navy text, high contrast.
- [ ] Switch to **Dark Mode**: Confirm deep navy canvas (`#0B132B`), cyan highlights, clean card borders.
- [ ] Switch to **System Mode**: Confirm the site automatically synchronizes with your OS setting.
- [ ] Refresh the page (`F5`): Confirm **0ms visual flash (0ms FOUC)** and preference persistence.

### 4. Hero Section
- [ ] Verify title `Vishwa K` renders as the primary `<h1>`.
- [ ] Confirm dynamic typing rotation cycles through the 4 verified roles.
- [ ] Click `Explore My Work`: Confirm smooth scroll to `#projects`.
- [ ] Click `Connect on LinkedIn`: Confirm new tab opens to `https://www.linkedin.com/in/thevishwakumar`.

### 5. Projects & Ventures Section
- [ ] Verify all 4 project cards render cleanly:
  - **Zinoin Group**: Link opens `https://zinoingroup.in/`.
  - **DocuMind AI**: Link opens `https://github.com/thevishwakumar/documind`.
  - **TNT Commercial Platforms**: Link opens `https://github.com/thevishwakumar/tntdiwaliordermanagement`.
  - **CampusBridge / SkillTrack**: Tagged as `In Development`.
- [ ] Click `View Technical Projects on GitHub`: Confirms `https://github.com/thevishwakumar`.

### 6. About, Education & Certifications
- [ ] Verify founder portrait (`assets/img/about.jpg`) displays crisply.
- [ ] Verify academic enrollment: *Sri Sai Ranganathan Engineering College (B.E. Cyber Security, CGPA: 8.5/10)*.
- [ ] Verify Class 12 performance: *Krishnagiri District Model School (72.83%)*.
- [ ] Verify 9 certifications: CappricioSec (Credential ID `b093c0aab1b34503a711`), Cisco, Google, HubSpot, Semrush, HP LIFE, LinkedIn Learning.

### 7. Mobile Navigation & Responsiveness
- [ ] Open the site on a smartphone (or Chrome DevTools mobile view `Ctrl + Shift + M`).
- [ ] Tap the hamburger menu: Verify navigation drawer slides smoothly into view.
- [ ] Tap any navigation link: Verify menu closes automatically and scrolls to target.
- [ ] Verify horizontal scrolling: Drag screen left/right to confirm **zero horizontal overflow (0px)**.

### 8. Outbound Social Links
- [ ] **LinkedIn**: `https://www.linkedin.com/in/thevishwakumar` (Target: `_blank`, `rel="noopener noreferrer"`).
- [ ] **GitHub**: `https://github.com/thevishwakumar` (Target: `_blank`, `rel="noopener noreferrer"`).
- [ ] **Instagram**: `https://www.instagram.com/thevishwakumar/` (Target: `_blank`, `rel="noopener noreferrer"`).
- [ ] **Email**: `mailto:thevishwaofficial@gmail.com`.

### 9. Contact Form Usability & Submission
- [ ] Confirm inputs enforce 16px minimum font size (no unwanted auto-zoom on iPhone).
- [ ] Send a test inquiry through the form:
  - Enter test Name, Email, and Message.
  - Click `Send Message`.
  - Confirm inline status toast appears (`Message sent successfully!`).
  - Confirm notification email arrives at `thevishwaofficial@gmail.com`.

### 10. Assets & Media Loading
- [ ] Open Chrome DevTools (`F12`) ➔ **Network** tab ➔ Filter by **Img**.
- [ ] Confirm all images return `200 OK` (WebP and SVG format).
- [ ] Filter by **Fetch/XHR**: Confirm all 7 JSON files in `/data/` return `200 OK`.

### 11. SEO & Discoverability
- [ ] Verify `https://founder.zinoingroup.in/robots.txt` returns `200 OK` and references sitemap.
- [ ] Verify `https://founder.zinoingroup.in/sitemap.xml` returns `200 OK` with canonical URL.
- [ ] Inspect source (`Ctrl + U`): Verify Schema.org JSON-LD `@graph` is present and valid.

### 12. Custom 404 Error Page
- [ ] Navigate to an invalid URL: `https://founder.zinoingroup.in/non-existent-page`.
- [ ] Confirm the branded custom `404.html` appears with a `Back to Home` button and `noindex` directive.

### 13. Console Cleanliness
- [ ] Open DevTools **Console** tab.
- [ ] Verify there are **0 unhandled JavaScript exceptions** or resource 404 errors.

### 14. Edge Cache Invalidation
- [ ] If old content persists, execute Cloudflare Cache Purge (**Cloudflare Dashboard** ➔ **Caching** ➔ **Purge Everything**).
