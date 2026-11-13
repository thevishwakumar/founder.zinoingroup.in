# Social Profile URL Update & Validation Report
**Project:** Vishwa K – Founder Website  
**Domain:** [https://founder.zinoingroup.in/](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date:** November 13, 2026  
**Status:** 📋 **CHANGES STAGED LOCALLY — AWAITING OWNER APPROVAL**  

---

## 1. Executive Summary

This report documents the verification and synchronization of social profile links across `founder.zinoingroup.in` using the **exact owner-provided URLs**:
* **LinkedIn:** `https://www.linkedin.com/in/thevishwakumar`
* **Instagram:** `https://www.instagram.com/thevishwakumar/`
* **GitHub:** `https://github.com/thevishwakumar`

All instances of outdated handles (specifically the legacy `@thevishwa._` Instagram handle and old query parameters) have been flagged, isolated, and updated across the HTML DOM, Schema.org structured data, and meta tags.

---

## 2. Outdated & Duplicate Links Audit (Flagged Items)

During the audit, the following legacy discrepancies were identified and resolved:

| Flag ID | Channel | Legacy / Outdated Value in Code | Owner-Provided Correct Value | Resolution Status |
| :---: | :--- | :--- | :--- | :---: |
| **FLG-01** | **Instagram URL** | `https://www.instagram.com/thevishwa._`<br>*(also legacy query `?igsh=MWx4ZGQydHQxYTE4bw==`)* | `https://www.instagram.com/thevishwakumar/` | ✅ UPDATED to authoritative URL across all sections |
| **FLG-02** | **Instagram Text Handle** | `@thevishwa._` (visible text in Contact section) | `@thevishwakumar` | ✅ UPDATED to match active account handle |
| **FLG-03** | **Twitter/X Creator Meta** | `<meta name="twitter:creator" content="@thevishwa._">` | `<meta name="twitter:creator" content="@thevishwakumar">` | ✅ SYNCHRONIZED with owner username |
| **FLG-04** | **LinkedIn URL** | `https://www.linkedin.com/in/thevishwakumar` | `https://www.linkedin.com/in/thevishwakumar` | ✅ VERIFIED 100% consistent across all components |
| **FLG-05** | **GitHub URL** | `https://github.com/thevishwakumar` | `https://github.com/thevishwakumar` | ✅ VERIFIED 100% consistent across all components |

---

## 3. Granular Code Location Mapping (`index.html`)

Every social touchpoint is cataloged below with its DOM location, current URL, and validation status:

| Location in Code | HTML Element / Context | Configured URL | Display Text / ARIA Label | Rel Attribute | Validation |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Line 54** | `<meta name="twitter:creator">` | `@thevishwakumar` | N/A (Meta Tag) | N/A | ✅ Valid |
| **Lines 109–111** | `<script type="application/ld+json">` (`sameAs`) | `https://www.linkedin.com/in/thevishwakumar`<br>`https://github.com/thevishwakumar`<br>`https://www.instagram.com/thevishwakumar/` | Semantic Schema Entities | N/A | ✅ Valid |
| **Line 1561** | Hero Secondary Button CTA | `https://www.linkedin.com/in/thevishwakumar` | `Connect on LinkedIn` | `noopener noreferrer` | ✅ Valid |
| **Line 1567** | Hero Social Bar — LinkedIn | `https://www.linkedin.com/in/thevishwakumar` | `aria-label="Vishwa K LinkedIn Profile"` | `noopener noreferrer` | ✅ Valid |
| **Line 1570** | Hero Social Bar — GitHub | `https://github.com/thevishwakumar` | `aria-label="Vishwa K GitHub Profile"` | `noopener noreferrer` | ✅ Valid |
| **Line 1576** | Hero Social Bar — Instagram | `https://www.instagram.com/thevishwakumar/` | `aria-label="Vishwa K Instagram Profile"` | `noopener noreferrer` | ✅ Valid |
| **Line 1950** | Projects Section Dedicated CTA Button | `https://github.com/thevishwakumar` | `View Technical Projects on GitHub` | `noopener noreferrer` | ✅ Valid |
| **Line 1968** | Contact Section Directory — LinkedIn | `https://www.linkedin.com/in/thevishwakumar` | `linkedin.com/in/thevishwakumar` | `noopener noreferrer` | ✅ Valid |
| **Line 1976** | Contact Section Directory — GitHub | `https://github.com/thevishwakumar` | `github.com/thevishwakumar` | `noopener noreferrer` | ✅ Valid |
| **Line 1992** | Contact Section Directory — Instagram | `https://www.instagram.com/thevishwakumar/` | `@thevishwakumar` | `noopener noreferrer` | ✅ Valid |
| **Line 2067** | Footer Social Dock — LinkedIn | `https://www.linkedin.com/in/thevishwakumar` | `aria-label="LinkedIn Profile"` | `noopener noreferrer` | ✅ Valid |
| **Line 2068** | Footer Social Dock — GitHub | `https://github.com/thevishwakumar` | `aria-label="GitHub Profile"` | `noopener noreferrer` | ✅ Valid |
| **Line 2070** | Footer Social Dock — Instagram | `https://www.instagram.com/thevishwakumar/` | `aria-label="Instagram Profile"` | `noopener noreferrer` | ✅ Valid |

---

## 4. Security & Accessibility Verification

1. **Tabnabbing Protection:** 100% of external social links use `target="_blank" rel="noopener noreferrer"`. No external window can manipulate `window.opener`.
2. **Accessible Labeling:** Every interactive icon link includes an explicit descriptive `aria-label`, and the embedded vector icons (`<i class="bx ...">`) declare `aria-hidden="true"` to prevent redundant screen reader announcements.
3. **Recognizable Visual Icons:** Employs industry-standard Boxicons vector glyphs:
   * LinkedIn: `bx bxl-linkedin` / `bx bxl-linkedin-square`
   * GitHub: `bx bxl-github`
   * Instagram: `bx bxl-instagram`
4. **Touch Target Sizing:** All social buttons and icons feature minimum bounding dimensions of **40 × 40px** up to **44 × 44px**, satisfying WCAG 2.2 AA target size requirements.
5. **Form & Brand Integrity:**
   * Jotform / Web3Forms contact integration: **Preserved and untouched.**
   * Corporate palette & layout: **Maintained without alteration.**
   * Zero fake statistics, follower metrics, or unearned repo counts.

---

## 5. Before & After Code Changes for Owner Review

### A. Head Metadata & JSON-LD Structured Data
```diff
- <meta name="twitter:creator" content="@thevishwa._">
+ <meta name="twitter:creator" content="@thevishwakumar">

  "sameAs": [
    "https://www.linkedin.com/in/thevishwakumar",
    "https://github.com/thevishwakumar",
-   "https://www.instagram.com/thevishwa._"
+   "https://www.instagram.com/thevishwakumar/"
  ]
```

### B. Hero Social Bar
```diff
- <a href="https://www.instagram.com/thevishwa._" class="home__social-icon" target="_blank" rel="noopener noreferrer" aria-label="Vishwa K Instagram Profile">
+ <a href="https://www.instagram.com/thevishwakumar/" class="home__social-icon" target="_blank" rel="noopener noreferrer" aria-label="Vishwa K Instagram Profile">
      <i class="bx bxl-instagram" aria-hidden="true"></i>
  </a>
```

### C. Contact Section Directory
```diff
- <a href="https://www.instagram.com/thevishwa._" class="contact__link-item" target="_blank" rel="noopener noreferrer" aria-label="Follow Vishwa K on Instagram">
+ <a href="https://www.instagram.com/thevishwakumar/" class="contact__link-item" target="_blank" rel="noopener noreferrer" aria-label="Follow Vishwa K on Instagram">
      <div class="contact__link-icon" aria-hidden="true"><i class='bx bxl-instagram'></i></div>
      <div>
          <span class="contact__link-label">Instagram</span>
-         <span class="contact__link-value">@thevishwa._</span>
+         <span class="contact__link-value">@thevishwakumar</span>
      </div>
  </a>
```

### D. Footer Social Dock
```diff
- <a href="https://www.instagram.com/thevishwa._" class="footer__icon" target="_blank" rel="noopener noreferrer" aria-label="Instagram Profile"><i class="bx bxl-instagram" aria-hidden="true"></i></a>
+ <a href="https://www.instagram.com/thevishwakumar/" class="footer__icon" target="_blank" rel="noopener noreferrer" aria-label="Instagram Profile"><i class="bx bxl-instagram" aria-hidden="true"></i></a>
```

---

## 6. Deployment Hold Notice

> [!IMPORTANT]
> **AWAITING OWNER APPROVAL**  
> These updates have been applied and tested locally in `founder.zinoingroup.in/index.html`. In accordance with your instructions, **no files have been deployed to production**. Please review the changes above and confirm your approval.
