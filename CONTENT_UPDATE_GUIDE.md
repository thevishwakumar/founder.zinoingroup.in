# CONTENT UPDATE WORKFLOW & OWNER HANDBOOK

**Website:** [founder.zinoingroup.in](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date:** November 14, 2026  
**Audience:** Website Owner & Frontend Developers  
**Status:** **OPERATIONAL GUIDE**

---

## 1. Quick Overview

Updating your personal portfolio no longer requires editing thousands of lines of complex HTML. All portfolio content is managed through clean, human-readable JSON files located in the `founder.zinoingroup.in/data/` folder:

```
founder.zinoingroup.in/data/
├── profile.json           # Your name, headlines, bio, and contact info
├── expertise.json         # Technical domains and skills
├── projects.json          # Featured projects, code repos, and ventures
├── experience.json        # Professional timeline and company roles
├── education.json         # University degree and schooling milestones
├── certifications.json    # Verified certificates, IDs, and issuing bodies
└── social-links.json      # LinkedIn, GitHub, Instagram, and email links
```

When you edit any of these files, the website dynamically loads and displays your updated content automatically!

---

## 2. Step-by-Step Task Guides

### Task 1: How to Add a New Project
1. Open `founder.zinoingroup.in/data/projects.json`.
2. Locate the `"projects"` array.
3. Add a new object inside the array (don't forget a comma after the previous project object):

```json
{
  "id": "my-new-app",
  "title": "Autonomous Security Scanner",
  "tagline": "Automated Cloud Vulnerability Auditing",
  "badge": "Active Beta",
  "badgeStyle": "background: rgba(16, 185, 129, 0.9);",
  "image": "assets/img/project-security.webp",
  "imageAlt": "Security Scanner architecture diagram",
  "description": "High-throughput cloud security auditor written in Go, analyzing multi-tenant AWS environments for misconfigurations.",
  "technologies": [
    "Go",
    "AWS Security",
    "Docker",
    "CI/CD Pipeline"
  ],
  "actions": [
    {
      "type": "link",
      "label": "View on GitHub",
      "url": "https://github.com/thevishwakumar/security-scanner",
      "icon": "bx bxl-github",
      "buttonClass": "button--primary",
      "ariaLabel": "View Autonomous Security Scanner source code"
    }
  ]
}
```
4. Save the file. Refresh `http://localhost:8080/` to immediately view your new project card!

---

### Task 2: How to Update an Existing Project Description or Tags
1. Open `founder.zinoingroup.in/data/projects.json`.
2. Find the project by its `"id"` (e.g. `"documind-ai"`).
3. Modify the `"description"` text or add new entries to the `"technologies"` list:
```json
"technologies": [
  "FastAPI",
  "React",
  "ChromaDB",
  "Gemini AI",
  "RBAC Security",
  "Docker Containerization"  <-- Added new skill
]
```
4. Save the file.

---

### Task 3: How to Add a New Certification
1. Open `founder.zinoingroup.in/data/certifications.json`.
2. Add a new certification block into the `"certifications"` array:

```json
{
  "id": "aws-cloud-practitioner",
  "title": "AWS Certified Cloud Practitioner",
  "organization": "Amazon Web Services",
  "orgIcon": "bx bx-award",
  "footerLabel": "Cloud Architecture",
  "status": "Certified",
  "isVerified": true,
  "link": {
    "url": "https://aws.amazon.com/verification",
    "text": "ID: AWS-99482710",
    "title": "Verify AWS Credential"
  }
}
```
*Note: If your certificate does not have an online verification link, simply set `"link": null` and provide a `"footerLabel": "Academic Track"`.*

---

### Task 4: How to Update Education Milestones
1. Open `founder.zinoingroup.in/data/education.json`.
2. To update your CGPA, academic status, or graduation year for your B.E. in Cybersecurity, modify the `"meta"` array or `"period"`:
```json
"meta": [
  {
    "label": "CGPA:",
    "value": "8.7 / 10",
    "isHighlight": false
  },
  {
    "label": "Status:",
    "value": "Final Year Candidate",
    "isHighlight": true,
    "statusIcon": "bx bx-check-circle"
  }
]
```
3. Save the file.

---

### Task 5: How to Edit Expertise Skills
1. Open `founder.zinoingroup.in/data/expertise.json`.
2. Under `"categories"`, find the category (e.g. `"cybersecurity"`).
3. Add, remove, or rename skills in the `"skills"` array:
```json
"skills": [
  "Networking",
  "Linux Fundamentals",
  "Ethical Hacking Fundamentals",
  "Security Awareness",
  "Cloud Security (AWS)"
]
```

---

### Task 6: How to Update or Add Social Profile Links
1. Open `founder.zinoingroup.in/data/social-links.json`.
2. To update a URL or add a new profile (such as X/Twitter or YouTube):
```json
{
  "platform": "twitter",
  "label": "X (Twitter)",
  "handle": "@thevishwakumar",
  "displayValue": "x.com/thevishwakumar",
  "url": "https://x.com/thevishwakumar",
  "icon": "bx bxl-twitter",
  "ctaText": "Follow on X",
  "isPrimary": false
}
```

---

### Task 7: How to Update Professional Headlines & Bio
1. Open `founder.zinoingroup.in/data/profile.json`.
2. You can update:
   - `"badgeText"`: The pulsing pill in the Hero section (e.g. `"Founder & Developer at Zinoin Group"`).
   - `"typingTitles"`: The animated rotating text array in the Hero headline:
     ```json
     "typingTitles": [
       "Technology Enthusiast.",
       "Technology Entrepreneur.",
       "Founder & Developer.",
       "Cybersecurity Explorer.",
       "Cloud Systems Builder."
     ]
     ```
   - `"about.paragraphs"`: Any biography paragraphs.

---

## 3. Important Rules for JSON Editing (Avoid Common Pitfalls)

To ensure your updates load cleanly without syntax errors, follow these simple JSON rules:

1. **Always Use Double Quotes (`"..."`):**
   - Correct: `"title": "DocuMind AI"`
   - Incorrect: `'title': 'DocuMind AI'` (Single quotes cause JSON syntax errors)
2. **Watch the Commas:**
   - Put a comma (`,`) between items in a list or properties in an object.
   - **Do NOT put a comma after the very last item** before a closing `}` or `]`.
3. **Escaping Special Characters:**
   - If your text contains quotation marks, escape them with a backslash:  
     `"description": "Engineered the \"TNT\" mobile platform..."`
4. **Valid Image Paths:**
   - Always place image assets in `assets/img/` and reference them relatively (e.g. `"image": "assets/img/my-new-project.webp"`).

---

## 4. Local Preview Verification

After editing any JSON file:
1. Ensure your local preview server is running on `http://localhost:8080/`.
2. Open `http://localhost:8080/` in Google Chrome or Microsoft Edge.
3. Refresh the page (or press `Ctrl + F5` for hard reload).
4. Verify that your new project, skill, or certificate renders immediately with proper theme colors (Light and Dark).

*Refer to [CONTENT_VALIDATION_REPORT.md](file:///c:/Users/Vishw/Downloads/founder.zinoingroup.in/CONTENT_VALIDATION_REPORT.md) for automated validation results.*
