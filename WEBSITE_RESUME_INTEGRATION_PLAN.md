# WEBSITE RESUME INTEGRATION PLAN

**Target Domain:** https://founder.zinoingroup.in/  
**Owner:** Vishwa K  
**Brand:** Zinoin Group  
**Document Status:** Architectural Implementation Plan (No Codebase Changes Applied in Step 11)  
**Prerequisite:** Awaiting Owner Creation & Approval of the Final Resume PDF

---

## 1. Current State & Assessment

A comprehensive scan of the local repository confirmed that:
1. **No resume PDF currently exists** in the repository or assets folders.
2. **No broken or placeholder "Download Resume" buttons exist** in `founder.zinoingroup.in/index.html`.
3. In strict compliance with professional QA standards, **no simulated or fake PDF files have been generated**, and **no non-functional download triggers have been inserted into the live codebase**.

This plan provides the exact, production-ready blueprint for seamlessly introducing a resume download workflow once the approved PDF is provided by Vishwa K.

---

## 2. PDF Asset Compilation Standards

Before linking a PDF to the live website, the document must adhere to these technical and aesthetic standards:

| Specification | Standard | Rationale |
|---|---|---|
| **File Name** | `Vishwa_K_Resume.pdf` | Clean, recognizable, professional, contains candidate's name. |
| **Target File Size** | < 250 KB (Optimized vector text) | Instant mobile downloads; zero data lag for prospective recruiters. |
| **Page Count** | Maximum 2 Pages (1 Page preferred for undergraduate) | Standard for technical & executive ATS scanning. |
| **Typography** | Standard fonts (Inter, Roboto, Arial, or Calibri) | Guarantees universal rendering across all PDF viewers and mobile OS. |
| **Text Layer** | Real selectable text (Never flattened image) | Mandatory for Applicant Tracking Systems (ATS) parsing. |
| **Color Palette** | Dark Navy (`#0A192F`), Slate Grey (`#475569`), White | Matches the corporate brand identity of `founder.zinoingroup.in`. |
| **Target Storage Location** | `founder.zinoingroup.in/assets/docs/Vishwa_K_Resume.pdf` | Clean asset separation; avoids root folder clutter. |

---

## 3. Recommended Website Placement Options

### Placement Option 1: Hero Section Action Bar (Recommended)
Add a tertiary action button in the Hero section alongside "Explore My Work" and "Connect on LinkedIn".

```
┌─────────────────────────────────────────────────────────────┐
│                       HERO SECTION                          │
│                                                             │
│   [ Explore My Work ]   [ Connect on LinkedIn ]             │
│   [ 📄 Download Resume (PDF) ]                              │
└─────────────────────────────────────────────────────────────┘
```

#### HTML Snippet (Hero Actions):
```html
<a href="assets/docs/Vishwa_K_Resume.pdf" 
   class="button button--secondary button--resume" 
   download="Vishwa_K_Resume.pdf" 
   target="_blank" 
   rel="noopener noreferrer" 
   aria-label="Download Vishwa K Professional Resume (PDF, 220 KB)"
   onclick="if(typeof trackEvent === 'function') trackEvent('resume_download', { location: 'hero_cta', file_format: 'pdf' });">
    <i class='bx bx-file-blank' aria-hidden="true"></i> Download Resume
</a>
```

---

### Placement Option 2: About Section Signature Block
Integrate the resume download directly after the founder summary narrative in the About section. This serves visitors who have read Vishwa's background and are seeking a formal qualification record.

#### HTML Snippet (About Section):
```html
<div class="about__resume-cta scroll-animate" style="margin-top: 2rem;">
    <div class="resume-badge-card">
        <div class="resume-badge-info">
            <span class="resume-badge-title">Comprehensive Professional Profile</span>
            <span class="resume-badge-meta">ATS-Optimized • PDF Format • Updated November 2026</span>
        </div>
        <a href="assets/docs/Vishwa_K_Resume.pdf" 
           class="button button--primary" 
           download="Vishwa_K_Resume.pdf" 
           target="_blank" 
           rel="noopener noreferrer"
           aria-label="Download complete Curriculum Vitae for Vishwa K in PDF format"
           onclick="if(typeof trackEvent === 'function') trackEvent('resume_download', { location: 'about_section', file_format: 'pdf' });">
            <i class='bx bx-download' aria-hidden="true"></i> Download CV (PDF)
        </a>
    </div>
</div>
```

---

### Placement Option 3: Global Footer Quick Links
Ensure recruiters navigating to the bottom of the page can instantly access the resume without scrolling back to the top.

#### HTML Snippet (Footer):
```html
<li class="footer__link-item">
    <a href="assets/docs/Vishwa_K_Resume.pdf" 
       class="footer__link" 
       download="Vishwa_K_Resume.pdf" 
       target="_blank" 
       rel="noopener noreferrer"
       aria-label="Download Vishwa K Professional Resume PDF"
       onclick="if(typeof trackEvent === 'function') trackEvent('resume_download', { location: 'footer', file_format: 'pdf' });">
        <i class='bx bx-file' aria-hidden="true"></i> Resume (PDF)
    </a>
</li>
```

---

## 4. CSS Styling Specification

To maintain the sleek corporate design system, add the following lightweight CSS rules to `assets/css/styles.css`:

```css
/* ===== RESUME DOWNLOAD CTA ===== */
.button--resume {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.5rem;
    font-size: var(--normal-font-size);
    font-weight: var(--font-medium);
    border-radius: var(--radius-md);
    transition: var(--transition-fast);
}

.resume-badge-card {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1.25rem;
    padding: 1.25rem 1.75rem;
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
}

.resume-badge-info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.resume-badge-title {
    font-size: 1rem;
    font-weight: var(--font-semi);
    color: var(--text-title);
}

.resume-badge-meta {
    font-size: var(--smaller-font-size);
    color: var(--text-muted);
}

@media screen and (max-width: 768px) {
    .resume-badge-card {
        flex-direction: column;
        align-items: flex-start;
    }
}
```

---

## 5. Analytics & Event Telemetry

In Step 7, we integrated privacy-conscious Google Analytics 4 event tracking into `main.js`:
```javascript
function trackEvent(eventName, params) {
    if (window.dataLayer && Array.isArray(window.dataLayer)) {
        window.dataLayer.push({
            event: eventName,
            ...params,
            timestamp: new Date().toISOString()
        });
    }
}
```

When a user clicks "Download Resume", the following event will automatically be dispatched to Google Tag Manager / GA4:
```json
{
  "event": "resume_download",
  "location": "hero_cta",
  "file_name": "Vishwa_K_Resume.pdf",
  "file_format": "pdf",
  "timestamp": "2026-11-13T19:30:00.000Z"
}
```
This enables accurate tracking of recruiter engagement without compromising visitor privacy or capturing personal identifying information.

---

## 6. Server & Security Configuration (for Cloudflare / Apache / Nginx)

When deploying the PDF asset, ensure the web server serves it with optimal caching and security headers:

```nginx
# Nginx Configuration Example
location = /assets/docs/Vishwa_K_Resume.pdf {
    add_header Content-Type "application/pdf";
    add_header Content-Disposition "inline; filename=Vishwa_K_Resume.pdf";
    add_header Cache-Control "public, max-age=86400, must-revalidate";
    add_header X-Content-Type-Options "nosniff";
}
```

---

## 7. Execution Checklist (Once PDF is Provided)

- [ ] 1. Save finalized PDF to `founder.zinoingroup.in/assets/docs/Vishwa_K_Resume.pdf`.
- [ ] 2. Verify PDF file size is under 300 KB.
- [ ] 3. Insert the Hero / About HTML buttons into `founder.zinoingroup.in/index.html`.
- [ ] 4. Append the CSS rules to `assets/css/styles.css`.
- [ ] 5. Test download behavior in Chrome DevTools (verify 200 OK and correct MIME type `application/pdf`).
- [ ] 6. Test on mobile viewports (ensure button wraps responsively).
- [ ] 7. Commit changes to Git and await owner deployment sign-off.

