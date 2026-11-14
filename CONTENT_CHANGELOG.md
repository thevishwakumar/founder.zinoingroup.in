# CONTENT & ARCHITECTURAL CHANGELOG

**Project:** Vishwa K – Founder Website  
**Production Domain:** https://founder.zinoingroup.in/  
**Local Working File:** `founder.zinoingroup.in/index.html`  
**Checkpoint Backup:** `founder.zinoingroup.in/index.html.pre-step14`  
**Execution Date:** November 2026

---

## 1. Summary of Changes

| Scope | Type of Change | Files / Lines Affected | Description |
|---|:---:|---|---|
| **Header** | Performance / Asset | `index.html` (L1491) | Swapped fallback navbar logo from `zinoin-logo.png` (115.8 KB) to `zinoin-logo.webp` (35.9 KB). |
| **Styles** | CSS Addition | `index.html` (L1200) | Added `.project__actions` and `.button--small` styling rules for project card action links. |
| **Navigation** | Structure / Reordering | `index.html` (L1510) | Reordered navbar links so `Projects & Ventures` immediately follows `Expertise`. |
| **DOM Hierarchy** | Section Reordering | `index.html` (L1700) | Moved `<section id="projects">` before `<section id="education">` and `<section id="certifications">`. |
| **Projects Grid** | Content / Feature | `index.html` (L1700) | Added `DocuMind AI` card, upgraded `TNT Commercial Platforms` card, and added direct GitHub repo links. |
| **New Asset** | Asset Creation | `assets/img/project-documind.svg` | Created dark navy architectural vector diagram illustrating DocuMind AI's RAG & ChromaDB pipeline. |
| **Contact Form** | Security Hardening | `index.html` (L2340) | Replaced `.innerHTML` concatenation with `document.createTextNode()` to eliminate potential DOM-based XSS. |
| **Footer** | Navigation Alignment | `index.html` (L2380) | Synchronized footer quick links to reflect the updated section sequence. |

---

## 2. Granular Code Diffs

### Diff 1: Navbar Logo Optimization (Saving ~80 KB)
```html
<<<< BEFORE
<img src="assets/img/zinoin-logo.png" alt="Zinoin Group official corporate emblem" class="nav__logo-img" width="32" height="36" loading="eager" decoding="async">
====
<img src="assets/img/zinoin-logo.webp" alt="Zinoin Group official corporate emblem" class="nav__logo-img" width="32" height="36" loading="eager" decoding="async">
>>>>
```

---

### Diff 2: Navbar Navigation Links Sequence
```html
<<<< BEFORE
<li class="nav__item"><a href="#expertise" class="nav__link">Expertise</a></li>
<li class="nav__item"><a href="#education" class="nav__link">Education</a></li>
<li class="nav__item"><a href="#certifications" class="nav__link">Certifications</a></li>
<li class="nav__item"><a href="#projects" class="nav__link">Projects & Ventures</a></li>
====
<li class="nav__item"><a href="#expertise" class="nav__link">Expertise</a></li>
<li class="nav__item"><a href="#projects" class="nav__link">Projects & Ventures</a></li>
<li class="nav__item"><a href="#education" class="nav__link">Education</a></li>
<li class="nav__item"><a href="#certifications" class="nav__link">Certifications</a></li>
>>>>
```

---

### Diff 3: Projects Section Expansion & Upgrades
```html
<<<< BEFORE (3 Cards, No Direct Repo Action Buttons)
Card 1: Zinoin Group
Card 2: CampusBridge / SkillTrack
Card 3: TNT Tamil Calendar
Global Button: View Technical Projects on GitHub
====
>>>> AFTER (4 Cards, Symmetrical 2x2 Grid, Direct GitHub Repo Action Buttons)
Card 1: Zinoin Group
  └── Action: [Explore Venture] -> https://zinoingroup.in/

Card 2: DocuMind AI (NEW)
  └── Image: assets/img/project-documind.svg
  └── Tag: AI & Security RAG
  └── Desc: Document-grounded AI knowledge platform engineered with Google Gemini AI and ChromaDB semantic vector search. Features multi-tenant database isolation, JWT auth, and automated RBAC security test suites.
  └── Tech: FastAPI • React • ChromaDB • Gemini AI • RBAC Security
  └── Action: [View Code] -> https://github.com/thevishwakumar/documind

Card 3: TNT Commercial Platforms (UPGRADED)
  └── Image: assets/img/project-tnt.webp
  └── Tag: Client Platform
  └── Desc: Engineered commercial ordering software with anti-enumeration security for client Shree Taste N Taste Catering, alongside the high-performance TNT Tamil Calendar mobile application.
  └── Tech: JavaScript ES6 • Supabase • PostgreSQL • Security Controls
  └── Action: [View Code] -> https://github.com/thevishwakumar/tntdiwaliordermanagement

Card 4: CampusBridge / SkillTrack
  └── Image: assets/img/project-campusbridge.svg
  └── Tag: In Development
  └── Status: Architecture & Engine In Progress

Global Button: View Technical Projects on GitHub -> https://github.com/thevishwakumar
```

---

### Diff 4: Contact Form Error Handler Security Fix [SEC-01]
```javascript
<<<< BEFORE
contactResult.innerHTML = "<i class='bx bx-error-circle' aria-hidden='true'></i> " + (resJson.message || "Failed to send message. Please try again.");
====
contactResult.innerHTML = "<i class='bx bx-error-circle' aria-hidden='true'></i> ";
const errorText = document.createTextNode(resJson.message || "Failed to send message. Please try again.");
contactResult.appendChild(errorText);
>>>>
```

---

### Diff 5: Footer Quick Links Alignment
```html
<<<< BEFORE
<li><a href="#home" class="footer__nav-link">Home</a></li>
<li><a href="#about" class="footer__nav-link">About</a></li>
<li><a href="#education" class="footer__nav-link">Education</a></li>
<li><a href="#projects" class="footer__nav-link">Projects</a></li>
<li><a href="#contact" class="footer__nav-link">Contact</a></li>
====
<li><a href="#home" class="footer__nav-link">Home</a></li>
<li><a href="#about" class="footer__nav-link">About</a></li>
<li><a href="#expertise" class="footer__nav-link">Expertise</a></li>
<li><a href="#projects" class="footer__nav-link">Projects</a></li>
<li><a href="#education" class="footer__nav-link">Education</a></li>
<li><a href="#certifications" class="footer__nav-link">Certifications</a></li>
<li><a href="#contact" class="footer__nav-link">Contact</a></li>
>>>>
```

