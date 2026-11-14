# ANALYTICS SETUP & CONFIGURATION CHECKLIST

**Website:** [founder.zinoingroup.in](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date of Assessment:** November 14, 2026  
**Role:** Senior Web Analytics Engineer & Privacy-Focused Frontend Developer  
**Status:** **READY FOR OWNER REVIEW & SIGN-OFF**

---

## 1. Overview & Instructions

This checklist guides **Vishwa K** through the practical setup, verification, and long-term maintenance of the privacy-friendly visitor analytics system for `https://founder.zinoingroup.in/`.

Follow the checklist sections corresponding to your preferred analytics strategy.

---

## 2. Pre-Setup Validation Checklist

- [x] **No Fake Credentials:** Verify that no mock, fabricated, or unverified Google Analytics or Cloudflare tokens are committed to source code.
- [x] **Theme Safety:** Confirm that analytics code does not touch or conflict with `localStorage.getItem('theme-preference')`.
- [x] **Zero PII Leakage:** Confirm that `#contact-name`, `#contact-email`, `#contact-phone`, and `#contact-message` are never passed into any analytics dataLayer or beacon.
- [x] **Zero Framework Overhead:** Confirm all tracking runs in native Vanilla JavaScript without React, jQuery, or bloated SDKs.
- [x] **Core Web Vitals Safety:** Confirm that scripts load asynchronously before `</body>` to prevent LCP or INP regressions.

---

## 3. Configuration by Strategy

### Option A: Cloudflare Web Analytics (Recommended Default — 100% Free & Cookieless)
```
[ ] Step 1. Log in to your Cloudflare Dashboard (https://dash.cloudflare.com/).
[ ] Step 2. Navigate to 'Web Analytics' from the left sidebar.
[ ] Step 3. Select your domain: 'founder.zinoingroup.in'.
[ ] Step 4. Under 'Settings', verify that Web Analytics is enabled for your Cloudflare Pages project.
[ ] Step 5. No cookie banner required! Cloudflare Web Analytics is 100% cookieless and GDPR compliant.
[ ] Step 6. Open the Web Analytics tab to view real-time traffic, pageviews, referrers, and Core Web Vitals.
```

### Option B: Plausible Analytics (Optional Premium Cookieless Dashboard)
```
[ ] Step 1. Register an account at https://plausible.io/ (or deploy a self-hosted instance).
[ ] Step 2. Add 'founder.zinoingroup.in' as a new site.
[ ] Step 3. Copy your script snippet (typically: <script defer data-domain="founder.zinoingroup.in" src="https://plausible.io/js/script.js"></script>).
[ ] Step 4. Place the snippet in <head> of index.html.
[ ] Step 5. In Plausible dashboard, create Custom Event Goals:
       - 'social_click'
       - 'project_click'
       - 'contact_section_view'
       - 'contact_form_interaction'
[ ] Step 6. Verify incoming custom events in Plausible real-time dashboard.
```

### Option C: Google Tag Manager (GTM-N4T5ZSJJ) + GA4 (If Required for Google Ecosystem)
```
[ ] Step 1. Log in to Google Tag Manager (https://tagmanager.google.com/).
[ ] Step 2. Open Container 'GTM-N4T5ZSJJ'.
[ ] Step 3. Create a Google Tag:
       - Tag Type: Google Tag
       - Tag ID: Enter your real GA4 Measurement ID (e.g. G-XXXXXXXXXX).
       - Trigger: All Pages.
[ ] Step 4. Configure Consent Settings in GTM:
       - Set default ad_storage='denied' and analytics_storage='denied' if serving EU visitors without a consent banner.
[ ] Step 5. Create Custom Event Triggers for:
       - 'social_click'
       - 'project_click'
       - 'contact_section_view'
       - 'contact_form_interaction'
[ ] Step 6. Create GA4 Event Tags mapped to each custom event trigger.
[ ] Step 7. Test in GTM Preview Mode, verify events, and click 'Submit' -> 'Publish'.
```

---

## 4. Realtime Verification & Quality Assurance Protocol

Perform these verification steps to ensure analytics telemetry operates reliably:

```
[ ] 1. Open http://localhost:8080/ (or production URL) in Google Chrome.
[ ] 2. Press F12 -> Console.
[ ] 3. Type: window.dataLayer and press Enter.
       - Verify: dataLayer array exists and contains 'gtm.js'.
[ ] 4. Scroll down to the Contact section (#contact).
       - Verify: 'contact_section_view' event is pushed to dataLayer.
[ ] 5. Click on the LinkedIn icon in the Hero section.
       - Verify: 'social_click' event is pushed with platform: 'linkedin'.
[ ] 6. Click on the 'View Code' link on DocuMind AI project card.
       - Verify: 'project_click' event is pushed with project_name: 'DocuMind AI'.
[ ] 7. Click into the 'Your Name' field on the Contact Form.
       - Verify: 'contact_form_interaction' event is pushed with action: 'form_start'.
       - Verify: No personal name or text is present in dataLayer.
[ ] 8. Check Network Tab (Filter: 'beacon' or 'collect' or 'rum').
       - Verify: Outgoing pings succeed with HTTP 200 or 204.
```

---

## 5. Ad-Blocker Resilience Check

```
[ ] 1. Install uBlock Origin or enable Brave Shields in browser.
[ ] 2. Reload website.
[ ] 3. Verify:
       - Website loads instantly with zero JavaScript errors.
       - Navigation menu opens and closes cleanly.
       - Theme toggle (System / Light / Dark) switches smoothly.
       - Contact form submits properly.
       - Result: Total resilience; ad-blockers do not impair website functionality.
```

---

## 6. Maintenance & Governance Schedule

| Frequency | Action Item | Responsible Party |
|---|---|---|
| **Monthly** | Review top traffic referral sources (LinkedIn vs GitHub vs direct) in Cloudflare Dashboard. | Website Owner (Vishwa K) |
| **Quarterly** | Check Core Web Vitals telemetry in Cloudflare to ensure real-user LCP remains $\le 2.5\text{s}$. | DevOps / Developer |
| **Semi-Annually** | Review privacy regulations (DPDP Act updates, GDPR guidelines) to verify continued compliance. | QA / Legal Review |
| **Annual** | Verify external project URLs and social link integrity. | Website Owner |

---

## 7. Sign-Off & Approval Record

- [x] **Analytics Engineering Review:** Complete.
- [x] **Privacy & Compliance Audit:** Complete.
- [ ] **Owner Approval:** Pending owner decision on Strategy A, B, or C.

*Refer to [ANALYTICS_PROVIDER_COMPARISON.md](file:///c:/Users/Vishw/Downloads/founder.zinoingroup.in/ANALYTICS_PROVIDER_COMPARISON.md) for the strategic provider evaluation.*
