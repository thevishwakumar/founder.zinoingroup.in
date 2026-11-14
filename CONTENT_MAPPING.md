# Detailed Content Mapping Report
**Project:** Zinoin Founder Website  
**URL:** [https://founder.zinoingroup.in/](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Document Version:** 1.0.0 (Pre-Implementation Mapping)  

This document provides a line-by-line and section-by-section mapping from the existing website copy to the recommended executive copy. For every section, the current state, proposed replacement, rationale, and items requiring owner verification are clearly delineated.

---

## 1. Page Header, Meta & SEO Tags

### Current Content
```html
<title>Vishwa K - Cybersecurity & Marketing Professional</title>
<meta name="description" content="Professional portfolio of Vishwa K - Cybersecurity student and Marketing expert with 1.5 years of experience.">
<meta name="keywords" content="Cybersecurity, Digital Marketing, Marketing Analytics, Vishwa K, Portfolio">
<meta name="author" content="Vishwa K">
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" href="assets/img/about.jpg">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
```

### Recommended Replacement
```html
<title>Vishwa K | Founder & Developer, Zinoin Group | Cybersecurity & Digital Innovation</title>
<meta name="description" content="Official website of Vishwa K — Founder & Developer at Zinoin Group. Specializing in cyber defense architecture, enterprise identity governance, and high-impact digital ventures.">
<meta name="keywords" content="Vishwa K, Zinoin Group, Founder Zinoin, Cybersecurity Engineer, Autonomous Cyber Defense, AccessFlow, ETHOS, Coimbatore, Digital Innovation">
<meta name="author" content="Vishwa K">
<link rel="canonical" href="https://founder.zinoingroup.in/">

<!-- Open Graph / Social Sharing -->
<meta property="og:type" content="profile">
<meta property="og:title" content="Vishwa K | Founder & Developer at Zinoin Group">
<meta property="og:description" content="Founder & Developer at Zinoin Group. Engineering secure digital infrastructure, autonomous threat defense systems, and digital ventures.">
<meta property="og:url" content="https://founder.zinoingroup.in/">
<meta property="og:image" content="https://founder.zinoingroup.in/assets/img/about.jpg">
<meta property="og:site_name" content="Vishwa K - Zinoin Group">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Vishwa K | Founder & Developer at Zinoin Group">
<meta name="twitter:description" content="Founder & Developer at Zinoin Group. Cybersecurity Engineering, Autonomous Threat Defense & Digital Innovation.">
<meta name="twitter:image" content="https://founder.zinoingroup.in/assets/img/about.jpg">

<!-- Structured Data (JSON-LD) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Vishwa K",
  "url": "https://founder.zinoingroup.in/",
  "image": "https://founder.zinoingroup.in/assets/img/about.jpg",
  "jobTitle": "Founder & Developer",
  "worksFor": {
    "@type": "Organization",
    "name": "Zinoin Group",
    "url": "https://zinoingroup.in/"
  },
  "alumniOf": {
    "@type": "EducationalOrganization",
    "name": "Sri Sai Ranganathan Engineering College"
  },
  "sameAs": [
    "https://www.linkedin.com/in/thevishwakumar",
    "https://www.instagram.com/thevishwa._"
  ],
  "knowsAbout": [
    "Cybersecurity Engineering",
    "Autonomous Cyber Defense",
    "Identity Governance & Administration",
    "Digital Marketing & Growth",
    "Software Engineering"
  ]
}
</script>
```

### Reason for Replacement
* Replaces junior student meta copy with authoritative corporate founder positioning.
* Adds missing Canonical link, Open Graph metadata, Twitter Cards, and Google JSON-LD schema for SEO visibility.
* Fixes broken link to non-existent `assets/img/apple-touch-icon.png`.

### Items Requiring Owner Verification
* Confirm whether Twitter/X handle should be added to Twitter meta tags.

---

## 2. Navigation Bar & Branding

### Current Content
```html
<a href="#" class="nav__logo">Vishwa</a>

<ul class="nav__list">
    <li class="nav__item"><a href="#home" class="nav__link active">Home</a></li>
    <li class="nav__item"><a href="#about" class="nav__link">About</a></li>
    <li class="nav__item"><a href="#skills" class="nav__link">Skills</a></li>
    <li class="nav__item"><a href="#education" class="nav__link">Education</a></li>
    <li class="nav__item"><a href="#certificates" class="nav__link">Certificates</a></li>
    <li class="nav__item"><a href="#contact" class="nav__link">Contact</a></li>
</ul>
```

### Recommended Replacement
```html
<a href="#home" class="nav__logo">
    <img src="assets/img/zinoin-logo.png" alt="Zinoin Group Emblem" class="nav__logo-img" width="30" height="34">
    <span class="nav__logo-text">Vishwa K</span>
    <span class="nav__logo-badge">Founder</span>
</a>

<ul class="nav__list">
    <li class="nav__item"><a href="#home" class="nav__link active">Home</a></li>
    <li class="nav__item"><a href="#about" class="nav__link">About</a></li>
    <li class="nav__item"><a href="#expertise" class="nav__link">Expertise</a></li>
    <li class="nav__item"><a href="#education" class="nav__link">Education</a></li>
    <li class="nav__item"><a href="#certifications" class="nav__link">Certifications</a></li>
    <li class="nav__item"><a href="#projects" class="nav__link">Projects & Ventures</a></li>
    <li class="nav__item"><a href="#contact" class="nav__link">Contact</a></li>
</ul>
```

### Reason for Replacement
* Plain text "Vishwa" looks like an informal student assignment. Pairing it with the official Zinoin emblem and "Founder" badge instantly establishes corporate credibility.
* Updates navigation anchors to match modern section nomenclature ("Expertise" instead of "Skills", "Certifications" instead of "Certificates", and adds "Projects & Ventures").

### Items Requiring Owner Verification
* Confirm inclusion of the Zinoin emblem in the top navbar.

---

## 3. Hero / Home Section

### Current Content
```html
<h1 class="home__title fade-in-up delay-1">
    Hi,<br />I'am <span class="home__title-color">Vishwa K</span><br />
    <span class="typing-container">
        <span class="typing-text">Founder of Zinoin Group</span>
    </span>
</h1>
<p class="fade-in-up delay-3">Cybersecurity student with 1.5 years of experience in digital marketing and analytics</p>
<a href="#contact" class="button fade-in-up delay-4">Contact</a>

<div class="home__social fade-in-up delay-4">
    <a href="https://www.linkedin.com/in/vishwa-k-b0ba2834b" class="home__social-icon" target="_blank" aria-label="LinkedIn">
        <i class="bx bxl-linkedin"></i>
    </a>
    <a href="/cdn-cgi/l/email-protection#81f5e9e4f7e8f2e9f6e0eee7e7e8e2e8e0edc1e6ece0e8edafe2eeec" class="home__social-icon" aria-label="Email">
        <i class="bx bx-envelope"></i>
    </a>
    <a href="https://www.instagram.com/thevishwa._?igsh=MWx4ZGQydHQxYTE4bw==" class="home__social-icon" target="_blank" aria-label="Instagram">
        <i class="bx bxl-instagram"></i>
    </a>
</div>
```

### Recommended Replacement
```html
<div class="home__data">
    <div class="home__badge fade-in-up delay-1">
        <span class="pulse-dot"></span> Founder & Developer at Zinoin Group
    </div>
    <h1 class="home__title fade-in-up delay-2">
        Building Secure Systems &<br />
        <span class="home__title-color">Digital Innovation</span><br />
        <span class="typing-container">
            <span class="typing-text">Vishwa K</span>
        </span>
    </h1>
    <p class="home__subtitle fade-in-up delay-3">
        Cybersecurity Engineering undergraduate and technical entrepreneur. Leading Zinoin Group in engineering autonomous cyber defense concepts, enterprise identity governance, and high-impact digital ventures.
    </p>
    <div class="home__actions fade-in-up delay-4">
        <a href="#projects" class="button button--primary">Explore Ventures</a>
        <a href="#contact" class="button button--secondary">Get in Touch</a>
    </div>

    <div class="home__social fade-in-up delay-5">
        <a href="https://www.linkedin.com/in/thevishwakumar" class="home__social-icon" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn Profile">
            <i class="bx bxl-linkedin"></i>
        </a>
        <a href="mailto:thevishwaofficial@gmail.com" class="home__social-icon" aria-label="Direct Email">
            <i class="bx bx-envelope"></i>
        </a>
        <a href="https://www.instagram.com/thevishwa._" class="home__social-icon" target="_blank" rel="noopener noreferrer" aria-label="Instagram Profile">
            <i class="bx bxl-instagram"></i>
        </a>
    </div>
</div>
```

### Reason for Replacement
* Eliminates grammatical error (`"I'am"`).
* Eliminates weak student positioning statement.
* Updates outdated LinkedIn URL from `vishwa-k-b0ba2834b` to official `thevishwakumar`.
* Replaces single contact CTA with dual executive CTAs ("Explore Ventures" + "Get in Touch").
* Typing animation cycles: *"Founder & Developer"*, *"Cybersecurity Specialist"*, *"Digital Innovation Strategist"*.

### Items Requiring Owner Verification
* Confirm whether direct `mailto:` link is preferred or if Cloudflare email protection obfuscation should be preserved.

---

## 4. About Me Section

### Current Content
```html
<section class="about section" id="about">
    <h2 class="section-title">About</h2>
    <div class="about__container bd-grid">
        <div class="about__img scroll-animate">
            <img src="assets/img/about.jpg" alt="Vishwa" />
        </div>
        <div class="scroll-animate">
            <h2 class="about__subtitle scroll-animate">Founder of Zinoin Group</h2>
            <p class="about__text scroll-animate">
                I am a passionate Cybersecurity student currently in my second year of studies. With 1.5 years of professional experience in marketing, advertising, analytics, and leadership, I bring a unique perspective to the field of cybersecurity.
            </p>
            <p class="about__text scroll-animate">
                My background in analytics helps me understand data patterns and security vulnerabilities, while my leadership experience enables me to effectively communicate security protocols and lead teams in implementing security measures.
            </p>
            <p class="about__text scroll-animate">
                I'm dedicated to staying current with the latest cybersecurity trends and technologies to protect digital assets and ensure data privacy.
            </p>
            <div class="personal-info scroll-animate">
                <div class="info-item">
                    <i class='bx bx-envelope info-icon'></i>
                    <span>thevishwaofficial@gmail.com</span>
                </div>
                <div class="info-item">
                    <i class='bx bx-map info-icon'></i>
                    <span>Bangalore, India</span>
                </div>
            </div>
        </div>
    </div>
</section>
```

### Recommended Replacement
```html
<section class="about section" id="about">
    <h2 class="section-title">About Me</h2>

    <div class="about__container bd-grid">
        <div class="about__img scroll-animate">
            <div class="about__img-wrapper">
                <img src="assets/img/about.jpg" alt="Vishwa K - Founder & Developer at Zinoin Group" width="500" height="500" loading="lazy" decoding="async" />
            </div>
        </div>

        <div class="about__data scroll-animate">
            <h3 class="about__subtitle">Bridging Cybersecurity Engineering & Strategic Entrepreneurship</h3>
            <p class="about__text">
                I am the <strong>Founder & Developer at Zinoin Group</strong> and an engineering undergraduate specializing in <strong>Cyber Security Engineering</strong> at Sri Sai Ranganathan Engineering College, Coimbatore. I operate at the intersection of technical defensive architecture, systems engineering, and technology entrepreneurship.
            </p>
            <p class="about__text">
                At Zinoin Group, I spearhead technological ventures, direct digital initiatives, and architect security-first systems. My engineering focus centers on autonomous threat detection, deception and trap networks, enterprise identity governance (Zero Trust), and safeguarding enterprise data integrity in the age of artificial intelligence.
            </p>
            <p class="about__text">
                By synthesizing analytical security principles with digital growth strategy, I lead cross-functional development cycles that turn complex technical concepts into resilient, scalable platforms.
            </p>

            <div class="personal-info">
                <div class="info-item">
                    <i class='bx bx-briefcase-alt-2 info-icon'></i>
                    <span><strong>Role:</strong> Founder & Developer</span>
                </div>
                <div class="info-item">
                    <i class='bx bx-buildings info-icon'></i>
                    <span><strong>Organization:</strong> Zinoin Group</span>
                </div>
                <div class="info-item">
                    <i class='bx bx-envelope info-icon'></i>
                    <span><strong>Email:</strong> thevishwaofficial@gmail.com</span>
                </div>
                <div class="info-item">
                    <i class='bx bx-map-pin info-icon'></i>
                    <span><strong>Location:</strong> Tamil Nadu, India (Global Engagements)</span>
                </div>
            </div>
        </div>
    </div>
</section>
```

### Reason for Replacement
* Permanently resolves the outdated "second year" claim.
* Completely removes the outdated Bangalore location.
* Adds missing `width`, `height`, `loading="lazy"`, and `decoding="async"` to `about.jpg` to prevent layout shifts (CLS).
* Frames Vishwa's leadership role at Zinoin Group authoritatively.

### Items Requiring Owner Verification
* Confirm location display string: *"Tamil Nadu, India"* vs *"Coimbatore, Tamil Nadu, India"*.

---

## 5. Skills Section to Expertise Section

### Current Content
* Flat grid of 30 items: Meta Ads, Social Media Marketing, Google Analytics, Email Marketing, Marketing Strategy, Risk Management, Leadership, Digital Marketing, Business Development, Team Management, Business Administration, Frontend Development, Strategic Planning, Market Research, Financial Planning, Facebook Ads, Generative AI, Prompt Engineering, WordPress Development, SEO Optimization, Google Ads, PPC Advertising, Business Management, Operations Management, Data Analysis, Innovation Thinking, Banking Processes, Financial Operations, Business Ideation, Growth Strategy.
* Detailed Bangalore residential address printed in resume section.

### Recommended Replacement
Structure into 4 domain pillars with verified technical competencies:

#### Pillar 1: Cybersecurity & Defense Architecture
* Autonomous Cyber Defense & Deception Mechanisms
* Threat Modeling, Log Analysis & Vulnerability Assessment
* Network Protocols & Security: TCP/IP, DNS, HTTP/HTTPS, SSH, VPN
* Security Tooling: Wireshark, Nmap, Cisco Packet Tracer, Linux CLI
* AI Threat & Phishing Detection (CyberGuard Framework)

#### Pillar 2: Systems, Software & Infrastructure
* Core Languages: Python, Java, SQL
* Web Engineering: Modern Semantic HTML5, CSS3, Vanilla JavaScript (ES6+), Responsive UI
* Systems & Databases: Linux Administration, Windows Security Fundamentals, MySQL, PostgreSQL
* Identity & Access Management (IAM): Role-Based Access Control (RBAC), Zero Trust Concepts (AccessFlow)
* Tooling & Version Control: Git, GitHub, VS Code, RESTful APIs

#### Pillar 3: Enterprise AI & Data Security
* AI Data Privacy & Compliance Shields (ETHOS Architecture)
* Data Redaction & Middleware Protection for Enterprise LLMs
* Generative AI Strategy & Advanced Prompt Engineering
* Content Classification & Anomaly Detection Workflows

#### Pillar 4: Digital Strategy & Venture Operations
* Technical Venture Leadership & Digital Infrastructure (Zinoin Group)
* Search Engine Optimization (SEO) & Marketing Analytics (Google Analytics)
* Growth Architecture & Strategic Digital Operations
* Technical Documentation & Stakeholder Advisory

#### Languages Matrix
* **English:** Professional Working Proficiency
* **Tamil:** Native / Fluent
* **Kannada:** Working Proficiency
* **Hindi:** Basic Working Knowledge

### Reason for Replacement
* Strips out unverified/unsupported claims (*"Banking Processes"*, *"Financial Operations"*).
* Pulls verified technical skills directly from Vishwa's technical resume.
* Eliminates the personal residential address completely.

### Items Requiring Owner Verification
* Confirm if any additional technical programming languages or cloud tools should be added.

---

## 6. Education Section

### Current Content
```html
<div class="education__item scroll-animate">
    <h3 class="education__title">B.E Cyber Security</h3>
    <p class="education__org">Sri Sai Ranganathan Engineering College, Coimbatore</p>
    <p class="education__date">Currently Pursuing (Second Year)</p>
    <p>Building strong technical knowledge in network security, ethical hacking, and data protection while actively exploring hands-on projects to enhance skills.</p>
</div>

<div class="education__item scroll-animate">
    <h3 class="education__title">Higher Secondary (3rd Year)</h3>
    <p class="education__org">Krishnagiri District Model School, Krishnagiri</p>
    <p class="education__date">Completed with 72.83%</p>
    <p>Developed a strong foundation in core subjects such as Mathematics, Physics, and Chemistry. Gained essential skills in communication and problem-solving through academic and co-curricular activities.</p>
</div>
```

### Recommended Replacement
```html
<div class="education__item scroll-animate">
    <div class="education__header">
        <span class="education__badge">Undergraduate Degree</span>
        <span class="education__date">2024 – 2028</span>
    </div>
    <h3 class="education__title">Bachelor of Engineering in Cyber Security Engineering</h3>
    <p class="education__org"><i class='bx bx-building'></i> Sri Sai Ranganathan Engineering College, Coimbatore, Tamil Nadu</p>
    <div class="education__meta">
        <span class="meta-tag"><i class='bx bx-award'></i> <strong>CGPA:</strong> 8.5 / 10</span>
        <span class="meta-tag"><i class='bx bx-check-circle'></i> <strong>Status:</strong> Currently Pursuing</span>
    </div>
    <p class="education__desc">
        Specializing in network security architectures, defensive deception systems, ethical hacking, cryptography, operating systems, and enterprise data protection protocols.
    </p>
</div>

<div class="education__item scroll-animate">
    <div class="education__header">
        <span class="education__badge">Secondary Education</span>
        <span class="education__date">Completed</span>
    </div>
    <h3 class="education__title">Higher Secondary Education (HSC)</h3>
    <p class="education__org"><i class='bx bx-building'></i> Krishnagiri District Model School, Krishnagiri, Tamil Nadu</p>
    <div class="education__meta">
        <span class="meta-tag"><i class='bx bx-bar-chart'></i> <strong>Score:</strong> 72.83%</span>
    </div>
    <p class="education__desc">
        Core focus in Mathematics, Physics, Chemistry, and Computer Science fundamentals, establishing the analytical base for advanced engineering studies.
    </p>
</div>
```

### Reason for Replacement
* Meets all requirements of the prompt's Education specification.
* Formally states degree as *Bachelor of Engineering in Cyber Security Engineering*.
* Includes official CGPA (8.5/10), tenure (2024–2028), and removes transient "second year" phrasing.

### Items Requiring Owner Verification
* None; verified against prompt and resume.

---

## 7. Certifications Section

### Current Content
* 40 entries, with 18 duplicate titles, blank dates, and zero credential verification details.
* Omits all verified cybersecurity certifications.

### Recommended Replacement
Curated, deduplicated catalog of 14 verified certifications organized into 3 high-impact domains:

#### Domain 1: Cybersecurity & Defensive Security
1. **Cybersecurity Fundamentals** — IBM SkillsBuild *(Issued: Aug 2026)*
2. **Getting Started with Cybersecurity** — IBM SkillsBuild *(Issued: Aug 2026)*
3. **Ethical Hacking 101: Beginner's Guide** — Simplilearn SkillUp *(Issued: Aug 2026)*
4. **Cybersecurity & Ethical Hacking** — CappricioSec University *(Issued: Apr 2026)*

#### Domain 2: Artificial Intelligence & Technical Analytics
5. **Introduction to GenAI & Prompting** — LetsUpgrade
6. **Digital Marketing with AI** — LetsUpgrade
7. **Business Analytics with Excel** — Microsoft / Simplilearn

#### Domain 3: Digital Strategy, Leadership & Governance
8. **Digital Marketing Certified** — HubSpot Academy
9. **Google Ads Display & Search Certifications** — Google
10. **Campaign Manager 360 Certification** — Google
11. **Fundamentals of Marketing Analytics** — Semrush Academy
12. **Effective Leadership & Social Entrepreneurship** — HP LIFE Foundation
13. **Corporate Actions & Investor Awareness** — TCS iON / SEBI (NISM)
14. **Entrepreneurship Foundations** — LinkedIn Learning

### Reason for Replacement
* Eliminates all 18 duplicates.
* Surfaces genuine cybersecurity credentials that reinforce the founder's core domain.
* Preserves legitimate business, marketing, and leadership achievements.

### Items Requiring Owner Verification
* Confirm if specific Credential IDs or verification URLs should be linked for any of these certificates.

---

## 8. Projects & Ventures Section (BRAND NEW)

### Current Content
* **None (Section was completely omitted in the old website).**

### Recommended Replacement
```html
<section class="projects section" id="projects">
    <h2 class="section-title">Projects & Ventures</h2>

    <div class="projects__container bd-grid">
        <!-- Venture 1: Zinoin Group -->
        <div class="project__card scroll-animate">
            <div class="project__header">
                <span class="project__tag">Core Venture</span>
                <span class="project__role">Founder & Developer</span>
            </div>
            <h3 class="project__title">Zinoin Group</h3>
            <p class="project__desc">
                Leading the strategic vision and engineering operations of Zinoin Group. Overseeing the design, architecture, and deployment of secure enterprise digital infrastructure, client solutions, and emerging technology ventures.
            </p>
            <div class="project__tech">
                <span>Enterprise Technology</span>
                <span>Cybersecurity</span>
                <span>Digital Infrastructure</span>
                <span>Venture Leadership</span>
            </div>
        </div>

        <!-- Project 2: Autonomous AI Defense -->
        <div class="project__card scroll-animate">
            <div class="project__header">
                <span class="project__tag">Cybersecurity / AI</span>
                <span class="project__role">Lead Architect</span>
            </div>
            <h3 class="project__title">Autonomous AI Defense & Trap Network</h3>
            <p class="project__desc">
                Engineered an autonomous cyber defense framework that inspects suspicious network activity and initiates automated threat mitigation. Integrated controlled deception and trap mechanisms to capture attacker telemetry and observe exploitation techniques in real time.
            </p>
            <div class="project__tech">
                <span>Deception Networks</span>
                <span>Automated Defense</span>
                <span>Threat Analysis</span>
                <span>Python</span>
            </div>
        </div>

        <!-- Project 3: CyberGuard -->
        <div class="project__card scroll-animate">
            <div class="project__header">
                <span class="project__tag">Threat Intelligence</span>
                <span class="project__role">Developer</span>
            </div>
            <h3 class="project__title">CyberGuard — AI Threat & Content Detection</h3>
            <p class="project__desc">
                Designed a security analysis system that inspects security logs, incoming mail telemetry, and malicious hyperlinks to detect phishing and spoofing indicators. Built classification pipelines to flag anomalous communication before network intrusion occurs.
            </p>
            <div class="project__tech">
                <span>Phishing Detection</span>
                <span>Log Inspection</span>
                <span>Threat Classification</span>
                <span>Security Analytics</span>
            </div>
        </div>

        <!-- Project 4: ETHOS -->
        <div class="project__card scroll-animate">
            <div class="project__header">
                <span class="project__tag">AI Security / DLP</span>
                <span class="project__role">Security Engineer</span>
            </div>
            <h3 class="project__title">ETHOS — AI Data Confidentiality & Compliance Shield</h3>
            <p class="project__desc">
                Developed a policy-based data security middleware designed to intercept and inspect prompt payloads, preventing sensitive enterprise intellectual property and confidential financial records from leaking to third-party AI endpoints.
            </p>
            <div class="project__tech">
                <span>Data Loss Prevention</span>
                <span>AI Governance</span>
                <span>Policy Enforcement</span>
                <span>Compliance</span>
            </div>
        </div>

        <!-- Project 5: AccessFlow -->
        <div class="project__card scroll-animate">
            <div class="project__header">
                <span class="project__tag">Identity Governance</span>
                <span class="project__role">System Architect</span>
            </div>
            <h3 class="project__title">AccessFlow — Identity Governance & ITDR Platform</h3>
            <p class="project__desc">
                Comprehensive Zero Trust Identity Governance and Administration (IGA) framework incorporating Privileged Access Management (PAM) and Identity Threat Detection & Response (ITDR) to eliminate credential sprawl and unauthorized lateral movement.
            </p>
            <div class="project__tech">
                <span>Zero Trust</span>
                <span>Identity Governance</span>
                <span>PAM</span>
                <span>ITDR Architecture</span>
            </div>
        </div>
    </div>
</section>
```

### Reason for Replacement
* Elevates the website from a basic CV into a true founder-level showcase.
* Directly addresses the prompt requirement: *"6. Projects & Ventures"*.
* All projects are authentic and sourced from Vishwa's verified resume and Zinoin technical documentation.

### Items Requiring Owner Verification
* Confirm if live URLs or GitHub repositories should be linked for any of these projects.

---

## 9. Contact Section & Form Backend

### Current Content
```html
<form action="https://api.web3forms.com/submit" method="POST" class="contact__form">
    <input type="hidden" name="access_key" value="eb8f26d7-359a-4d92-a252-7851ef76b341">
    <input type="text" placeholder="Name" class="contact__input" name="name" required>
    <input type="email" placeholder="Email" class="contact__input" name="email" required>
    <input type="tel" placeholder="Phone Number" class="contact__input" name="phone">
    <textarea name="message" cols="0" rows="10" class="contact__input" placeholder="Your Message" required></textarea>
    <input type="submit" value="Send" class="contact__button button" id="contact-submit">
    <div id="contact-result" class="contact__result"></div>
</form>
```

### Recommended Replacement
* Keep the form fields clean, accessible, and responsive.
* Fix JavaScript submission handler: Remove broken `window.location.href = 'success.html'`. Replace with an animated, inline success state that informs the user their message was delivered and clears the form inputs.
* Retain compatibility with Web3Forms access key `eb8f26d7-359a-4d92-a252-7851ef76b341` unless owner supplies a Jotform form ID.

### Reason for Replacement
* Fixes the fatal 404 error on form submission.
* Clarifies the Jotform vs. Web3Forms backend integration.

### Items Requiring Owner Verification
* Confirm whether to keep Web3Forms with fixed AJAX toast or replace with Jotform embed.

---

## 10. Footer Section

### Current Content
```html
<footer class="footer">
    <p class="footer__title">Vishwa</p>
    <div class="footer__social">
        <a href="https://www.linkedin.com/in/vishwa-k-b0ba2834b" class="footer__icon" target="_blank" aria-label="LinkedIn"><i class="bx bxl-linkedin"></i></a>
        <a href="/cdn-cgi/l/email-protection#..." class="footer__icon" aria-label="Email"><i class="bx bx-envelope"></i></a>
        <a href="https://www.instagram.com/thevishwa._?igsh=MWx4ZGQydHQxYTE4bw==" class="footer__icon" target="_blank" aria-label="Instagram"><i class="bx bxl-instagram"></i></a>
    </div>
    <p class="footer__copy">&#169; Vishwa | All rights reserved</p>
</footer>
```

### Recommended Replacement
```html
<footer class="footer">
    <div class="footer__container bd-grid">
        <div class="footer__brand">
            <p class="footer__title">Vishwa K</p>
            <p class="footer__tagline">Founder & Developer · Zinoin Group</p>
        </div>
        <div class="footer__social">
            <a href="https://www.linkedin.com/in/thevishwakumar" class="footer__icon" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"><i class="bx bxl-linkedin"></i></a>
            <a href="mailto:thevishwaofficial@gmail.com" class="footer__icon" aria-label="Email"><i class="bx bx-envelope"></i></a>
            <a href="https://www.instagram.com/thevishwa._" class="footer__icon" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="bx bxl-instagram"></i></a>
        </div>
    </div>
    <p class="footer__copy">&#169; <span id="current-year">2026</span> Vishwa K · Zinoin Group. All rights reserved.</p>
</footer>
```

### Reason for Replacement
* Updates LinkedIn link.
* Adds corporate affiliation tagline.
* Sets dynamic copyright year calculation.

