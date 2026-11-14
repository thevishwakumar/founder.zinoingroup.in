# REMAINING ISSUES & OWNER ACTION REGISTRY

**Project:** Vishwa K – Founder Website  
**Production Domain:** https://founder.zinoingroup.in/  
**Document Status:** Post-Implementation Outstanding Items & Next Steps  
**Date:** November 2026

---

## 1. Summary of Current Status

Following the successful execution of Step 14, **all approved code changes, section reordering, security patches, and project upgrades have been implemented and verified locally**. 

There are **zero critical or high-severity blockers** remaining in the codebase. The items listed below represent owner action items, optional future enhancements, and deployment sign-off prerequisites.

---

## 2. Action Items Requiring Owner Input

### Item 1: Resume PDF Asset Delivery
* **Status:** Master resume content is verified and prepared in `RESUME_CONTENT.md`.
* **Action Required:** When Vishwa K compiles and exports the official PDF (`Vishwa_K_Resume.pdf`), it should be placed in `assets/docs/Vishwa_K_Resume.pdf`.
* **Follow-up:** Once the file is present, the accessible Hero action button documented in `WEBSITE_RESUME_INTEGRATION_PLAN.md` will be enabled.

---

### Item 2: Web3Forms Domain Whitelisting
* **Status:** Contact form is configured with public access key and honeypot protection.
* **Action Required:** Log into the [Web3Forms Dashboard](https://web3forms.com/) and lock the active access key strictly to:  
  `founder.zinoingroup.in`
* **Benefit:** Prevents unauthorized third parties from submitting requests using this key on external origins.

---

### Item 3: Secondary Certification Credential IDs
* **Status:** The website currently features the 8 verified technical and cybersecurity credentials (CappricioSec, SkillFront ISO 27001, IBM SkillsBuild, Simplilearn, Cisco Academy, HubSpot).
* **Action Required:** If the owner wishes to feature secondary business/marketing certificates (Google Ads, LetsUpgrade, Semrush, MTF Institute), provide the verification IDs or public credential URLs. Otherwise, keeping the section focused on the 8 technical credentials remains the recommended approach.

---

## 3. Optional Future Enhancements (Non-Blocking)

### Enhancement 1: Self-Host Boxicons Web Font [SEC-02]
* **Current:** Loaded from `https://cdn.jsdelivr.net/npm/boxicons@2.0.5/css/boxicons.min.css`.
* **Proposed Enhancement:** Download Boxicons WOFF2 binary and CSS to `assets/fonts/boxicons/` to eliminate external CDN dependencies and third-party DNS lookups.

### Enhancement 2: Cloudflare Edge Security Response Headers [SEC-03]
* **Proposed Enhancement:** When publishing to production through Cloudflare Pages or Edge Proxy, configure HTTP response headers via Cloudflare Transform Rules (`Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`).

---

## 4. Production Deployment Prerequisite

* **Status:** **Ready for Production Deployment.**
* **Protocol:** In accordance with project instructions, **zero automated deployments have been triggered**. The website is serving on local preview (`http://localhost:8080/`) awaiting the owner's explicit deployment sign-off.

