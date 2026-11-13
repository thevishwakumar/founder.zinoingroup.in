# DEPLOYMENT & VERSION RELEASE HISTORY

**Website:** https://founder.zinoingroup.in/  
**Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Maintained by:** Senior DevOps Engineer & Frontend Release Manager  
**Repository Branch:** `master`

---

## 1. Release Milestone Ledger

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        FOUNDER WEBSITE VERSION HISTORY LEDGER                          │
├─────────┬──────────────────────┬─────────────┬─────────────────────────────────────────┤
│ Version │ Milestone Stage      │ Date        │ Summary of Significant Changes          │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ v1.0.0  │ Legacy Baseline      │ Pre-Audit   │ Initial junior student site baseline    │
│ v1.1.0  │ Content Alignment    │ Nov 2026    │ Founder positioning, CGPA 8.5/10 added  │
│ v1.2.0  │ Corporate UI/UX      │ Nov 2026    │ Dark navy brand palette, mobile drawer  │
│ v1.3.0  │ SEO & Performance    │ Nov 2026    │ JSON-LD schema, inlined CSS, GA4 events │
│ v1.4.0  │ Social Sync & GitHub │ Nov 2026    │ @thevishwakumar synced, GitHub audited  │
│ v1.5.0  │ Security & Health    │ Nov 2026    │ XSS audit, WebP quick win identified    │
│ v2.0.0  │ Production Candidate │ Nov 2026    │ Projects elevated, DocuMind AI added,   │
│         │                      │             │ XSS fixed, WebP logo active, 404 added  │
└─────────┴──────────────────────┴─────────────┴─────────────────────────────────────────┘
```

---

## 2. Granular Release Changelogs

### Version 2.0.0 (Production Release Candidate) — *November 2026 [CURRENT]*
* **Status:** Staged on Local Working Copy (`master` commit `e83214e`) — **Awaiting Owner Deployment Authorization**.
* **Major Enhancements:**
  - **Security Hardening [SEC-01]:** Eliminated DOM-based XSS surface in contact form error handler using `document.createTextNode()`.
  - **Asset Optimization [PERF-01]:** Swapped header navbar logo from `zinoin-logo.png` (115.8 KB) to `zinoin-logo.webp` (35.9 KB), saving **~80 KB (-69%)** on initial paint.
  - **Information Architecture:** Reordered sections so that `Projects & Ventures` (`#projects`) immediately follows `Areas of Expertise` (`#expertise`), preceding Education and Certifications.
  - **Featured Projects Expansion:**
    - Added **DocuMind AI** (Full-Stack RAG Knowledge Assistant with FastAPI, React, ChromaDB, Gemini AI, and RBAC security) with custom architectural vector `project-documind.svg`.
    - Upgraded **TNT Commercial Platforms** showcasing the commercial order management software built for client Shree Taste N Taste Catering alongside the TNT Calendar.
    - Added individual `View Code` action buttons linking directly to GitHub repositories.
  - **Cloudflare Edge Infrastructure:** Created production-ready `_headers` (HSTS, CSP, X-Content-Type-Options), `_redirects` (URL normalization), and a custom dark navy `404.html` error page.
  - **Safety Checkpoint:** Created master safety zip `founder_zinoingroup_backup_final_step16.zip` (1.70 MB).
  - **Lighthouse Scores:** Accessibility **100/100**, SEO **100/100**, Best Practices **96/100**, CLS **0.000**.

---

### Version 1.4.0 (Social Identity & Portfolio Discovery) — *November 2026*
* **Changes:**
  - Synchronized social links across the site to exact owner URLs (`https://www.linkedin.com/in/thevishwakumar`, `https://github.com/thevishwakumar`, `https://www.instagram.com/thevishwakumar/`).
  - Purged legacy Instagram handle `thevishwa._`.
  - Conducted deep unauthenticated public GitHub audit across 6 public repositories, identifying `documind` and `tntdiwaliordermanagement` as star deliverables.
  - Formulated Instagram brand blueprint for tech founders.

---

### Version 1.3.0 (SEO, Accessibility & Performance Hardening) — *November 2026*
* **Changes:**
  - Implemented complete Open Graph metadata, Twitter summary cards, and canonical URL directives.
  - Embedded rich Schema.org JSON-LD structured data (`Person`, `Organization`, `EducationalOrganization`).
  - Configured privacy-conscious Google Analytics 4 event tracking pushing to `window.dataLayer`.
  - Inlined all 1,332 lines of CSS within `<style>`, eliminating external render-blocking stylesheet roundtrips.
  - Increased button color contrast from 3.67:1 to 4.63:1 to achieve **100/100 Lighthouse Accessibility**.

---

### Version 1.2.0 (UI/UX Refinement) — *November 2026*
* **Changes:**
  - Redesigned visual layout to match the Zinoin Group corporate palette (Dark Navy `#0b1120`, Card Surface `#131f37`, Royal Blue `#2563eb`, Sky Blue `#38bdf8`).
  - Replaced legacy fonts with modern geometric typography: `Outfit` for headings and `Inter` for body copy.
  - Built responsive mobile navigation drawer with backdrop blur and touch targets $\ge 48\text{ px}$.
  - Verified 0px horizontal overflow across all device viewports (320px to 1920px).

---

### Version 1.1.0 (Content Rebuild & Accuracy Alignment) — *November 2026*
* **Changes:**
  - Replaced junior student copy with authoritative corporate founder voice: *"Founder & Developer at Zinoin Group"*.
  - Corrected academic details: B.E. Cyber Security Engineering at Sri Sai Ranganathan Engineering College (2024–2028 | Currently Pursuing, 2nd Year | CGPA: 8.5 / 10).
  - Corrected Higher Secondary details: Krishnagiri District Model School (Completed 2024 | 72.83%).
  - Curated 40 redundant and duplicate certificates down to 8 verified high-value technical credentials.

---

### Version 1.0.0 (Legacy Baseline) — *Pre-Audit State*
* **Initial State:**
  - Student portfolio with missing projects section.
  - Incomplete degree nomenclature and omitted CGPA.
  - 18 redundant or duplicate certificate entries.
  - Non-existent `apple-touch-icon.png` 404 error.
  - Outdated contact information and unoptimized image payloads.
