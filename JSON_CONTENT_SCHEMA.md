# JSON CONTENT SCHEMA SPECIFICATION

**Website:** [founder.zinoingroup.in](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date:** November 14, 2026  
**Schema Specification Standard:** JSON Schema Draft 2020-12  
**Data Directory:** `founder.zinoingroup.in/data/`  
**Status:** **ACTIVE SPECIFICATION**

---

## 1. Overview

This document specifies the exact JSON schemas, field data types, required constraints, and validation boundaries for all editable content on `founder.zinoingroup.in`.

Seven independent content files organize the portfolio's data:
1. `profile.json` — Identity, headlines, about bio, badges, contact metadata
2. `expertise.json` — 4 technical expertise categories & skill listings
3. `projects.json` — Featured engineering projects & business ventures
4. `experience.json` — Professional roles, timeline, and achievement bullets
5. `education.json` — Degrees, institutions, coursework, and grades
6. `certifications.json` — Verified credentials, issuing organizations, and IDs
7. `social-links.json` — Verified social channels, direct email, and website

---

## 2. Detailed Schema Definitions

### 2.1 `projects.json` Schema
- **File Location:** `data/projects.json`  
- **Schema File:** `data/schemas/projects.schema.json`  
- **Purpose:** Controls all project cards displayed in the `#projects` section.

| Field Name | Type | Required? | Description | Example Value |
|---|---|:---:|---|---|
| `id` | `string` | **YES** | Unique URL-friendly slug. | `"documind-ai"` |
| `title` | `string` | **YES** | Official title of the project or venture. | `"DocuMind AI"` |
| `tagline` | `string` | No | Subtitle describing architecture or role. | `"Full-Stack Enterprise RAG & Knowledge Assistant"` |
| `badge` | `string` | No | Overlay status pill on card image. | `"AI & Security RAG"` |
| `badgeStyle` | `string` | No | Optional inline CSS (e.g. background color). | `"background: rgba(14, 165, 233, 0.9);"` |
| `image` | `string` | No | Relative path to image/SVG asset. | `"assets/img/project-documind.svg"` |
| `imageAlt` | `string` | No | Descriptive accessibility alt text. | `"DocuMind AI full-stack RAG architecture diagram"` |
| `description` | `string` | **YES** | Detailed description of architecture & impact. | `"Document-grounded AI knowledge platform..."` |
| `technologies` | `array[string]` | No | Array of technology tags / tech pills. | `["FastAPI", "React", "ChromaDB", "Gemini AI"]` |
| `actions` | `array[object]` | No | List of buttons or status pills. | See action object breakdown below |

#### Project Action Object:
- `type`: `"link"` or `"pill"` (Required)
- `label`: Button text (e.g. `"View Code"`, `"Explore Venture"`)
- `url`: Destination URL (for type `"link"`)
- `icon`: Boxicons class (e.g. `"bx bxl-github"`, `"bx bx-globe"`)
- `buttonClass`: `"button--primary"` or `"button--secondary"`
- `ariaLabel`: Accessibility description for screen readers

---

### 2.2 `expertise.json` Schema
- **File Location:** `data/expertise.json`  
- **Schema File:** `data/schemas/expertise.schema.json`  
- **Purpose:** Controls the 4 technical capability cards in `#expertise`.

| Field Name | Type | Required? | Description | Example Value |
|---|---|:---:|---|---|
| `categories` | `array[object]` | **YES** | List of expertise areas. | `[...]` |
| `categories[].id` | `string` | **YES** | Unique identifier for category. | `"cybersecurity"` |
| `categories[].title` | `string` | **YES** | Category heading. | `"Cybersecurity"` |
| `categories[].icon` | `string` | **YES** | Boxicons CSS class for card icon. | `"bx bx-shield-quarter"` |
| `categories[].skills` | `array[string]` | **YES** | List of individual capabilities. | `["Networking", "Linux Fundamentals", ...]` |

---

### 2.3 `experience.json` Schema
- **File Location:** `data/experience.json`  
- **Schema File:** `data/schemas/experience.schema.json`  
- **Purpose:** Controls the professional timeline in `#experience`.

| Field Name | Type | Required? | Description | Example Value |
|---|---|:---:|---|---|
| `experiences` | `array[object]` | **YES** | List of timeline positions. | `[...]` |
| `experiences[].id` | `string` | **YES** | Unique identifier. | `"zinoin-founder"` |
| `experiences[].role` | `string` | **YES** | Professional role or title. | `"Founder & Lead Developer"` |
| `experiences[].company` | `string` | **YES** | Organization name. | `"Zinoin Group"` |
| `experiences[].companyIcon` | `string` | No | Boxicons class for organization. | `"bx bx-building-house"` |
| `experiences[].period` | `string` | **YES** | Date range. | `"2024 — Present"` |
| `experiences[].status` | `string` | No | Sub-badge text. | `"Active Venture"` |
| `experiences[].badgeStyle` | `string` | No | Optional badge CSS styling. | `"background: rgba(99, 102, 241, 0.1);"` |
| `experiences[].description` | `string` | No | High-level role overview. | `"Established and leads Zinoin Group..."` |
| `experiences[].bullets` | `array[object]` | No | List of key achievements. | `[{"icon": "bx bx-check-shield", "text": "..."}]` |
| `experiences[].technologies` | `array[string]` | No | Array of tech stack pills. | `["Venture Leadership", "Web Architecture", ...]` |

---

### 2.4 `education.json` Schema
- **File Location:** `data/education.json`  
- **Schema File:** `data/schemas/education.schema.json`  
- **Purpose:** Controls the academic milestones in `#education`.

| Field Name | Type | Required? | Description | Example Value |
|---|---|:---:|---|---|
| `education` | `array[object]` | **YES** | List of academic milestones. | `[...]` |
| `education[].id` | `string` | **YES** | Unique identifier. | `"be-cybersecurity"` |
| `education[].degree` | `string` | **YES** | Degree or qualification title. | `"Bachelor of Engineering (B.E.)"` |
| `education[].field` | `string` | No | Academic discipline. | `"Cybersecurity Engineering (Cyber Security)"` |
| `education[].institution` | `string` | **YES** | College or school name. | `"Sri Sai Ranganathan Engineering College"` |
| `education[].location` | `string` | No | Geographic location. | `"Coimbatore, Tamil Nadu, India"` |
| `education[].period` | `string` | No | Academic years. | `"2024–2028"` |
| `education[].badge` | `string` | No | Type badge (e.g. Undergraduate). | `"Undergraduate Degree"` |
| `education[].meta` | `array[object]` | No | Key-value pairs (CGPA, status). | `[{"label": "CGPA:", "value": "8.5 / 10"}]` |

---

### 2.5 `certifications.json` Schema
- **File Location:** `data/certifications.json`  
- **Schema File:** `data/schemas/certifications.schema.json`  
- **Purpose:** Controls the 9 verified credentials in `#certifications`.

| Field Name | Type | Required? | Description | Example Value |
|---|---|:---:|---|---|
| `certifications` | `array[object]` | **YES** | List of verified certificates. | `[...]` |
| `certifications[].id` | `string` | **YES** | Unique identifier. | `"cappriciosec-cybersecurity"` |
| `certifications[].title` | `string` | **YES** | Certificate title. | `"Cybersecurity & Ethical Hacking"` |
| `certifications[].organization` | `string` | **YES** | Issuing body. | `"CappricioSec University"` |
| `certifications[].orgIcon` | `string` | No | Boxicons class. | `"bx bx-award"` |
| `certifications[].footerLabel` | `string \| null` | No | Category track label. | `"Candidate Record"` |
| `certifications[].status` | `string` | No | Verification status badge. | `"Verified"` |
| `certifications[].isVerified` | `boolean` | No | Boolean verification indicator. | `true` |
| `certifications[].link` | `object \| null` | No | Verification link object. | `{"url": "...", "text": "ID: b093c0..."}` |

---

### 2.6 `profile.json` Schema
- **File Location:** `data/profile.json`  
- **Schema File:** `data/schemas/profile.schema.json`  
- **Purpose:** Controls identity, hero headlines, about text, badges, and contact metadata.

| Field Name | Type | Required? | Description | Example Value |
|---|---|:---:|---|---|
| `name` | `string` | **YES** | Full personal brand name. | `"Vishwa K"` |
| `alternateName` | `string` | No | Full alternative name. | `"Vishwa Kumar"` |
| `handle` | `string` | No | Universal social handle. | `"thevishwakumar"` |
| `role` | `string` | **YES** | Primary professional role. | `"Founder & Developer"` |
| `organization` | `string` | **YES** | Primary venture entity. | `"Zinoin Group"` |
| `badgeText` | `string` | No | Pulsing status pill in Hero. | `"Founder & Developer at Zinoin Group"` |
| `headlinePrefix` | `string` | No | Static headline prefix. | `"Founder. Developer."` |
| `typingTitles` | `array[string]` | No | Array of strings for typing effect. | `["Technology Enthusiast.", ...]` |
| `description` | `string` | **YES** | Hero summary paragraph. | `"I build digital solutions..."` |
| `about.subtitle` | `string` | **YES** | About section subtitle. | `"Technology · Entrepreneurship · Cybersecurity"` |
| `about.paragraphs` | `array[string]` | **YES** | Array of biographical paragraphs. | `["I'm Vishwa K...", ...]` |
| `about.badges` | `array[object]` | **YES** | Array of quick fact badges. | `[{"label": "Location", "value": "Tamil Nadu, India"}]` |
| `contact` | `object` | **YES** | Contact section heading and email. | `{"email": "thevishwaofficial@gmail.com"}` |

---

### 2.7 `social-links.json` Schema
- **File Location:** `data/social-links.json`  
- **Schema File:** `data/schemas/social-links.schema.json`  
- **Purpose:** Universal repository for all outbound social links.

| Field Name | Type | Required? | Description | Example Value |
|---|---|:---:|---|---|
| `links` | `array[object]` | **YES** | Array of profile links. | `[...]` |
| `links[].platform` | `string` | **YES** | Platform slug. | `"linkedin"` |
| `links[].label` | `string` | **YES** | Display name. | `"LinkedIn"` |
| `links[].displayValue` | `string` | No | Visible text value. | `"linkedin.com/in/thevishwakumar"` |
| `links[].url` | `string` | **YES** | Full target URL. | `"https://www.linkedin.com/in/thevishwakumar"` |
| `links[].icon` | `string` | **YES** | Boxicons class. | `"bx bxl-linkedin"` |
| `links[].ctaText` | `string` | No | Button CTA label. | `"Connect on LinkedIn"` |
| `links[].isPrimary` | `boolean` | No | Displayed in hero social row. | `true` |

---

*Refer to [CONTENT_UPDATE_GUIDE.md](file:///c:/Users/Vishw/Downloads/founder.zinoingroup.in/CONTENT_UPDATE_GUIDE.md) for how to edit these files.*
