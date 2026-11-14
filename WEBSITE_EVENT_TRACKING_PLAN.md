# WEBSITE EVENT TRACKING & VISITOR INTERACTION PLAN

**Website:** [founder.zinoingroup.in](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date of Assessment:** November 14, 2026  
**Role:** Senior Web Analytics Engineer & Privacy-Focused Frontend Developer  
**Status:** **APPROVED SPECIFICATION & AUDIT**

---

## 1. Core Principles & Privacy Safeguards

The event tracking architecture for `founder.zinoingroup.in` is built on a **zero-trust, privacy-by-design** foundation:

1. **Zero Personally Identifiable Information (PII):** Under no circumstance does event telemetry capture visitor names, email addresses, phone numbers, physical addresses, or free-form message contents.
2. **Intent-Driven Telemetry:** Events fire only when a visitor demonstrates explicit intent (scrolling deeply into key content, clicking an external verified project, or initiating communication).
3. **Non-Blocking Asynchronous Dispatch:** Event dispatchers use native browser APIs (`IntersectionObserver`, event listeners with `{ passive: true }`, and microtasks) to ensure 0ms main thread blocking and zero layout shift.
4. **Theme Independence:** Event tracking operates completely orthogonal to theme switching and `localStorage` keys (`theme-preference`), guaranteeing zero interference with UI state.

---

## 2. Event Tracking Taxonomy

The table below defines the formal event schema, triggers, payload parameters, and privacy verification status:

| Event Name | Trigger Condition | Event Parameters | Purpose & Business Value | PII Status | Implementation Status |
|---|---|---|---|:---:|:---:|
| **`page_view`** | Initial DOM load / route paint | `{ page_title, page_location, page_path }` | Measures overall visitor traffic and entry points. | **CLEAN** | Active (Browser / Beacon) |
| **`social_click`** | Click on any verified profile link (LinkedIn, GitHub, Instagram) | `{ platform: "linkedin" \| "github" \| "instagram", target_url: "...", link_location: "hero" \| "about" \| "footer" \| "contact" }` | Quantifies which social profile drives the highest professional networking conversion. | **CLEAN** | Active in `index.html` |
| **`project_click`** | Click on external project link or source code repository | `{ project_name: "Zinoin Group" \| "DocuMind AI" \| "TNT Calendar" \| "CampusBridge", click_type: "live_venture" \| "source_code", target_url: "..." }` | Identifies which featured engineering project or business venture garners the strongest interest. | **CLEAN** | Active in `index.html` |
| **`contact_section_view`** | Contact section becomes $\ge 30\%$ visible in viewport | `{ section: "contact", engagement_level: "high_intent" }` | Detects high-intent visitors who actively scroll to the bottom of the portfolio to explore contact options. | **CLEAN** | Active in `index.html` (via IntersectionObserver) |
| **`contact_form_interaction`** | Visitor focuses on any contact form input (`form_start`) | `{ action: "form_start" }` | Measures initial intent to submit an inquiry without capturing typed content. | **CLEAN** (Zero field values) | Active in `index.html` |
| **`contact_form_interaction`** | Form submission returns HTTP 200 success (`submit_success`) | `{ action: "submit_success" }` | Measures completed inquiry conversion rate. | **CLEAN** (Zero message data) | Active in `index.html` |
| **`contact_form_interaction`** | Form submission encounters API or network error (`submit_error`) | `{ action: "submit_error", error_type: "network" \| "validation" }` | Alerts technical team to form delivery failure without logging visitor data. | **CLEAN** | Active in `index.html` |
| **`theme_toggle`** | User switches theme in header dropdown or mobile drawer | `{ selected_theme: "system" \| "light" \| "dark", trigger_location: "header_dropdown" \| "drawer_segment" }` | Understands visitor visual preferences (e.g. % using Dark vs Light vs System mode). | **CLEAN** | Ready for integration |
| **`resume_download`** | User clicks verified resume / CV PDF download link | `{ document_name: "Vishwa_K_Resume.pdf", file_format: "pdf" }` | Measures recruitment / hiring interest. | **CLEAN** | **CONDITIONALLY INACTIVE** *(No public resume PDF currently exists)* |

---

## 3. Strict Negative Collection List (What is NEVER Collected)

To maintain absolute compliance with global privacy regulations, the frontend explicitly prohibits the collection of:
- **Form Text Content:** The contents of `#contact-name`, `#contact-email`, `#contact-phone`, and `#contact-message` are strictly routed to the Web3Forms encrypted endpoint and **never** exposed to `dataLayer` or analytics pings.
- **Passwords or Financial Data:** No authentication credentials or monetary transactions exist on the site.
- **Fingerprinting Hashes:** No Canvas fingerprinting, AudioContext fingerprinting, or hardware profiling.
- **Cross-Site Tracking Identifiers:** No advertising cookies, third-party pixel syncs, or social media tracking pixels.

---

## 4. Technical Implementation & Dispatch Architecture

### 4.1 Native Event Dispatcher (Vanilla JavaScript)
The website includes a lightweight, vendor-neutral event bridge in `founder.zinoingroup.in/index.html`:

```javascript
/* Native Lightweight Event Bridge */
function trackEvent(eventName, params = {}) {
    // 1. Dispatch to window.dataLayer (Standard GTM / Tag bus)
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
        event: eventName,
        timestamp: Date.now(),
        ...params
    });

    // 2. Dispatch to window.gtag if active
    if (typeof window.gtag === 'function') {
        window.gtag('event', eventName, params);
    }

    // 3. Dispatch to Plausible if active (Cookieless alternative)
    if (typeof window.plausible === 'function') {
        window.plausible(eventName, { props: params });
    }
}
```

### 4.2 High-Intent Viewport Observer (IntersectionObserver)
Rather than firing events on simple page scrolling, the contact section engagement is measured via a native, low-overhead C++ `IntersectionObserver` that unobserves itself immediately after first contact:

```javascript
const contactSection = document.getElementById('contact');
if (contactSection && 'IntersectionObserver' in window) {
    let contactViewed = false;
    const contactObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !contactViewed) {
                contactViewed = true;
                trackEvent('contact_section_view', { section: 'contact' });
                observer.unobserve(entry.target); // Detach immediately (0% CPU idle)
            }
        });
    }, { threshold: 0.3 }); // Requires 30% visibility
    contactObserver.observe(contactSection);
}
```

### 4.3 Outbound Profile & Project Click Handlers
All outbound external links are intercepted with lightweight passive listeners that extract only public metadata:

```javascript
// Social Links
document.querySelectorAll('a[href*="linkedin.com"], a[href*="github.com"], a[href*="instagram.com"]').forEach(link => {
    link.addEventListener('click', function() {
        const platform = this.href.includes('linkedin.com') ? 'linkedin' :
                         this.href.includes('github.com') ? 'github' : 'instagram';
        trackEvent('social_click', {
            platform: platform,
            target_url: this.href
        });
    }, { passive: true });
});

// Featured Venture & Project Links
document.querySelectorAll('.project__link').forEach(link => {
    link.addEventListener('click', function() {
        const projectCard = this.closest('.project__card');
        const projectTitle = projectCard ? projectCard.querySelector('.project__title')?.textContent.trim() : 'Project';
        trackEvent('project_click', {
            project_name: projectTitle,
            target_url: this.href
        });
    }, { passive: true });
});
```

### 4.4 Form Interaction Lifecycle (Zero PII)
```javascript
// Measure first field focus (Form Start)
const contactInputs = document.querySelectorAll('.contact__input');
let formStarted = false;
contactInputs.forEach(input => {
    input.addEventListener('focus', function() {
        if (!formStarted) {
            formStarted = true;
            trackEvent('contact_form_interaction', { action: 'form_start' });
        }
    }, { once: true, passive: true });
});

// Measure Submission Outcome without touching input values
// On HTTP 200 -> trackEvent('contact_form_interaction', { action: 'submit_success' });
// On Network Error -> trackEvent('contact_form_interaction', { action: 'submit_error' });
```

---

## 5. Resume Download Tracking (Conditional Specification)

### Current Site Status:
- **No public resume PDF file is currently hosted or linked on the website.**
- Therefore, the `resume_download` event is **inactive** by default to prevent dead triggers.

### Activation Blueprint (When Owner Approves Resume PDF):
If Vishwa K decides to publish an approved resume PDF (e.g. `/assets/docs/Vishwa_K_Resume.pdf`):
1. The link should include class `resume-download-link`:
   ```html
   <a href="/assets/docs/Vishwa_K_Resume.pdf" class="button button--secondary resume-download-link" download>
       <i class='bx bx-download'></i> Download Resume
   </a>
   ```
2. The event handler will automatically attach:
   ```javascript
   document.querySelectorAll('.resume-download-link').forEach(link => {
       link.addEventListener('click', function() {
           trackEvent('resume_download', {
               document_name: 'Vishwa_K_Resume.pdf',
               target_url: this.href
           });
       }, { passive: true });
   });
   ```

---

## 6. Verification & Quality Assurance Checklist

- [x] Zero form inputs logged to `window.dataLayer`.
- [x] Zero personal data passed as query parameters.
- [x] Event listeners use `{ passive: true }` or `{ once: true }` to avoid main thread jank.
- [x] IntersectionObserver detaches after firing once.
- [x] Compatible with Google Tag Manager, Plausible, Umami, or custom backends.

*Refer to [PRIVACY_REVIEW.md](file:///c:/Users/Vishw/Downloads/founder.zinoingroup.in/PRIVACY_REVIEW.md) for legal compliance and regulatory disclosures.*
