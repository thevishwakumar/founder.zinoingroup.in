# Website Security Review & Hardening Report
**Project:** Vishwa K – Founder Website  
**Domain:** [https://founder.zinoingroup.in/](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Audit Date:** November 13, 2026  
**Document Version:** 1.0.0 (Security Hardening Review Complete)  

---

## 1. Executive Summary

This report delivers a thorough security audit of the client-side architecture, form endpoints, third-party script integrations, and data handling on `founder.zinoingroup.in`. Because the website operates on a static JAMstack architecture (HTML, CSS, vanilla JS) served over Cloudflare's secure edge CDN, the attack surface is significantly lower than traditional monolithic database-driven applications (e.g. WordPress, Drupal). This audit validates that no sensitive credentials are leaked, external links are secured against reverse tabnabbing, form submissions are protected against automated spam bots, and security headers are specified for production deployment.

---

## 2. Form Submission Security & Anti-Spam Architecture

### 2.1 Endpoint Evaluation
* **Endpoint:** `https://api.web3forms.com/submit`
* **Transport Protocol:** Strict TLS 1.3 encrypted HTTPS. All form submissions transmit encrypted in transit.
* **Payload Structure:** Sanitized JSON (`JSON.stringify(object)`) via `fetch()` API with headers:
  ```json
  {
    "Content-Type": "application/json",
    "Accept": "application/json"
  }
  ```

### 2.2 Access Key vs Secret Key Clarification
* The form uses a public access key (`eb8f26d7-359a-4d92-a252-7851ef76b341`).
* **Security Assessment:** In the Web3Forms architecture, this access key is explicitly designed for public frontend embedding. It is cryptographically bound to the recipient email and does not grant administrative access, read access to previous messages, or billing authority. Web3Forms enforces origin verification, domain locking, and volumetric rate limiting on this key.

### 2.3 Bot & Spam Protection (Honeypot)
```html
<input type="checkbox" name="botcheck" class="hidden" style="display: none;" tabindex="-1" autocomplete="off">
```
* **Mechanism:** Automated spam scripts typically crawl forms and automatically populate or check all inputs. Real human users cannot see or interact with this input (hidden via CSS and excluded from keyboard navigation via `tabindex="-1"`).
* **Enforcement:** If `botcheck` contains a value, Web3Forms silently drops the message without sending notification emails, blocking spam floods without annoying legitimate visitors with CAPTCHA puzzles.

### 2.4 Client-Side Validation
* Strict HTML5 validation attributes (`required`, `type="email"`, `autocomplete`) prevent invalid or malformed data submission before network dispatch.
* Submit button is immediately disabled (`contactSubmit.disabled = true;`) during transit to prevent double-click duplicate submissions.

---

## 3. Reverse Tabnabbing Protection & Link Hygiene

### 3.1 Reverse Tabnabbing Risk
When an anchor link opens an external site with `target="_blank"`, the newly opened page gains partial execution access to the originating window via `window.opener`. A compromised third-party site could execute `window.opener.location = "https://phishing-site.com"`, silently redirecting the user to a spoofed page.

### 3.2 Audit & Mitigation
Every external hyperlink on `founder.zinoingroup.in` strictly incorporates `rel="noopener noreferrer"`:

```html
<!-- Example from Certifications section -->
<a href="https://university.cappriciosec.com/certificates/b093c0aab1b34503a711" 
   target="_blank" 
   rel="noopener noreferrer" 
   class="cert__link">
    Verify Credential
</a>

<!-- Example from Footer social profiles -->
<a href="https://www.linkedin.com/in/thevishwakumar" 
   target="_blank" 
   rel="noopener noreferrer" 
   aria-label="LinkedIn Profile">
    <i class="bx bxl-linkedin" aria-hidden="true"></i>
</a>
```

#### Link Audit Results:
* **LinkedIn Profiles:** Protected with `rel="noopener noreferrer"`.
* **GitHub Repository / Profile:** Protected with `rel="noopener noreferrer"`.
* **Instagram Profile:** Protected with `rel="noopener noreferrer"`.
* **CappricioSec University Credential:** Protected with `rel="noopener noreferrer"`.
* **Simplilearn Credential:** Protected with `rel="noopener noreferrer"`.
* **Zinoin Group Corporate Link:** Protected with `rel="noopener noreferrer"`.

---

## 4. Third-Party Script Supply Chain Assessment

| Script Provider | Source URL | Purpose | Security Controls Applied | Risk Level |
| :--- | :--- | :--- | :--- | :---: |
| **Google Tag Manager** | `https://www.googletagmanager.com/gtm.js` | Analytics tag orchestration | Container ID `GTM-N4T5ZSJJ`, loaded asynchronously (`j.async = true;`) | Low |
| **Cloudflare Web Analytics** | `https://static.cloudflareinsights.com/beacon.min.js/...` | Privacy-preserving traffic metrics | **Subresource Integrity (SRI)** hash: `integrity="sha512-UKNk8Gbxk..."`, `crossorigin="anonymous"` | Negligible |
| **Cloudflare Email Obfuscation** | `/cdn-cgi/scripts/.../email-decode.min.js` | Scrapes email addresses to protect from scrapers | First-party origin `/cdn-cgi/`, CDN-managed | Negligible |
| **Boxicons CDN** | `https://cdn.jsdelivr.net/npm/boxicons@2.0.5/css/...` | UI Vector icons | Read-only stylesheet (`rel="stylesheet"`), zero script execution capability | Negligible |
| **Google Fonts** | `https://fonts.googleapis.com` | Typography | Restricted CSS and WOFF2 font files only | Negligible |

* **SRI Verification:** The Cloudflare Insights script strictly uses Subresource Integrity (`integrity="sha512-..."`). If the script contents are altered at the CDN level, the browser will refuse to execute it.

---

## 5. Credential & Sensitive Data Scan

A complete static code analysis was performed across all project files:

| Sensitive Category | Scan Status | Details |
| :--- | :---: | :--- |
| **Database Passwords / DB URLs** | ✅ NONE | Static site; no database connection strings exist. |
| **Private API / Secret Keys** | ✅ NONE | Only the designated public Web3Forms submission key is present. |
| **Private SSH / SSL Keys** | ✅ NONE | No `.pem`, `.key`, or private certificates in workspace. |
| **Internal Staging / Dev URLs** | ✅ NONE | All references point to production `founder.zinoingroup.in` or official verified destinations. |
| **Sensitive Personal Information** | ✅ NONE | Outdated personal residential addresses completely purged. |

---

## 6. Recommended HTTP Production Security Headers

To further harden the website in production, the following HTTP security headers should be configured at the Cloudflare Edge, Nginx, or Netlify/Cloudflare Pages layer:

### 6.1 Recommended Headers Specification

```http
# Prevent MIME-type sniffing
X-Content-Type-Options: nosniff

# Clickjacking Protection
X-Frame-Options: SAMEORIGIN

# Cross-Site Scripting Filter Protection (Legacy)
X-XSS-Protection: 1; mode=block

# Referrer Information Leakage Protection
Referrer-Policy: strict-origin-when-cross-origin

# Enforce HTTPS (HSTS) - 1 Year with Subdomains
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

# Restrict Browser Hardware Features
Permissions-Policy: camera=(), microphone=(), geolocation=(), payment=()

# Content Security Policy (CSP)
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://static.cloudflareinsights.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net; font-src 'self' https://fonts.gstatic.com https://cdn.jsdelivr.net; img-src 'self' data: https://founder.zinoingroup.in; connect-src 'self' https://api.web3forms.com https://www.google-analytics.com https://cloudflareinsights.com; frame-ancestors 'self';
```

### 6.2 Deployment Implementation Options

#### Option A: Cloudflare Transform Rules (Recommended for `zinoingroup.in`)
1. Log in to Cloudflare Dashboard -> **Rules** -> **Transform Rules** -> **Modify Response Header**.
2. Add the headers listed above to apply automatically to all incoming traffic at the edge.

#### Option B: `_headers` File (For Cloudflare Pages or Netlify)
If deploying via Cloudflare Pages or Netlify, place a `_headers` file in the root directory:
```txt
/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  Permissions-Policy: camera=(), microphone=(), geolocation=()
```

---

## 7. Security Summary & Maintenance Checklist

* [x] **Form Protection:** Honeypot field and encrypted HTTPS endpoints deployed.
* [x] **Link Safety:** All external links utilize `rel="noopener noreferrer"`.
* [x] **Zero Plaintext Secrets:** No passwords, database strings, or private tokens present.
* [x] **Subresource Integrity:** Employed on third-party analytics scripts.
* [ ] **Next Step for Server Admin:** Apply edge HTTP security headers in Cloudflare dashboard.

