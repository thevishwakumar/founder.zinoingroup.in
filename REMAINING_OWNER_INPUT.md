# REMAINING OWNER INPUT & DECISION REGISTRY

**Target Website:** https://founder.zinoingroup.in/  
**Owner:** Vishwa K  
**Lead Roles:** Senior Web Project Manager & Quality Reviewer  
**Date:** November 2026  
**Document Purpose:** Clear, consolidated inventory of all decisions and inputs required from Vishwa K before final code implementation.

---

> [!IMPORTANT]
> **NO ASSUMPTIONS PROTOCOL**
> In strict accordance with project rules, the AI engineering team has **not silently resolved** any ambiguous or uncertain items. Every item below requires explicit owner sign-off.

---

## 1. Project Showcase Decisions

### Decision 1.1: Feature `DocuMind AI` on the Live Website
* **Context:** The GitHub audit discovered `documind` (FastAPI, React, ChromaDB, Google Gemini AI, PostgreSQL, JWT auth, multi-tenant RBAC security test suites). It is currently omitted from `founder.zinoingroup.in`.
* **Proposed Action:** Add `DocuMind AI` as a primary featured card under `Projects & Ventures`, establishing immediate technical authority in Applied AI and Access Governance.
* **Owner Input Required:**
  - [ ] **APPROVE:** Add DocuMind AI to the featured projects grid.
  - [ ] **REVISE:** Keep DocuMind AI exclusive to GitHub; do not display on website.

---

### Decision 1.2: Upgrade the TNT Project Card
* **Context:** The current site only lists "TNT Tamil Calendar" as a mobile utility. The GitHub audit discovered `tntdiwaliordermanagement`, an authentic commercial order management platform engineered for *Shree Taste N Taste Catering* with anti-enumeration security and Supabase database architecture.
* **Proposed Action:** Upgrade the card to represent **TNT Commercial Platforms**, showcasing both the Diwali ordering software and the mobile calendar.
* **Owner Input Required:**
  - [ ] **APPROVE:** Upgrade the TNT card to feature the commercial order management system + calendar.
  - [ ] **REVISE:** Keep the card restricted to "TNT Tamil Calendar" only.

---

### Decision 1.3: Direct GitHub Repository Links on Project Cards
* **Context:** Currently, the site only has one global button at the bottom: *"View Technical Projects on GitHub"*.
* **Proposed Action:** Add a clean, secondary `Code` button linking directly to the respective GitHub repositories (`github.com/thevishwakumar/documind` and `github.com/thevishwakumar/tntdiwaliordermanagement`).
* **Owner Input Required:**
  - [ ] **APPROVE:** Add direct GitHub buttons to individual project cards.
  - [ ] **REVISE:** Keep only the global GitHub CTA button at the bottom.

---

## 2. Information Architecture & Navigation

### Decision 2.1: Navigation Ordering & "Experience" Section
* **Context:** The prompt requests the following sequence: *Home ➔ About ➔ Expertise ➔ Projects ➔ Experience ➔ Education ➔ Certifications ➔ Contact*.
* **Proposed Options:**
  - **Option A (Recommended — Streamlined Hybrid):**  
    Move `Projects & Ventures` up immediately after `Expertise`. Maintain 7 clean navbar links (`Home`, `About`, `Expertise`, `Projects & Ventures`, `Education`, `Certifications`, `Contact`). Experience is represented via Zinoin Group leadership and client software delivery within the projects grid.
  - **Option B (Separate Dedicated Experience Section):**  
    Create an independent `<section id="experience">` between Projects and Education, and expand the navbar to 8 links.
* **Owner Input Required:**
  - [ ] **SELECT OPTION A:** Streamlined 7-link navbar (Projects & Ventures immediately after Expertise).
  - [ ] **SELECT OPTION B:** Dedicated 8-link navbar with standalone Experience section.

---

## 3. Resume PDF Compilation

### Decision 3.1: Resume PDF Asset Status
* **Context:** A complete ATS-optimized master resume text has been compiled in `RESUME_CONTENT.md`. No PDF currently exists in the repository.
* **Proposed Action:**
  - If Vishwa K has exported `Vishwa_K_Resume.pdf`, it can be placed into `assets/docs/Vishwa_K_Resume.pdf` and enabled via the Hero download button.
  - If the PDF is not yet compiled, the site will continue to withhold the "Download Resume" button to prevent broken 404 links.
* **Owner Input Required:**
  - [ ] **Option 1:** I have compiled the PDF / will provide `Vishwa_K_Resume.pdf` for integration now.
  - [ ] **Option 2:** Hold the download button until I compile the PDF in a future milestone.

---

## 4. Secondary Certifications Verification

### Decision 4.1: Streamlined Technical Certs vs. Full Catalog
* **Context:** 8 technical credentials are fully verified (CappricioSec, SkillFront ISO 27001, IBM SkillsBuild, Simplilearn, Cisco Academy, HubSpot). 8 secondary marketing/business certificates (Google Ads, LetsUpgrade, Semrush, MTF) lack credential IDs or public URLs.
* **Proposed Action:**
  - Display the 8 verified technical credentials on the live site.
  - Keep secondary certificates in reserve until verification IDs are provided.
* **Owner Input Required:**
  - [ ] **APPROVE:** Display the 8 verified technical credentials; hold unverified items.
  - [ ] **PROVIDE IDS:** I will provide the credential IDs for the secondary certificates now.

---

## 5. Security & Domain Protection

### Decision 5.1: Web3Forms Domain Whitelisting
* **Context:** The contact form uses a public Web3Forms access key. To prevent unauthorized third parties from submitting spam using this key on external sites, Web3Forms provides a domain lock feature.
* **Action Required by Owner:**
  - Log in to [web3forms.com](https://web3forms.com/) and lock the active access key strictly to:  
    `founder.zinoingroup.in`
