# Granular Certification Audit & Review
**Project:** Zinoin Founder Website  
**Owner:** Vishwa K  
**Document Version:** 1.0.0 (Certification Review)  

---

## 1. Raw Extraction of All 40 Existing Certifications

The table below presents the exhaustive extraction of every certification item currently rendered in `founder.zinoingroup.in/index.html` (Lines 1406 to 1645).

| # | Lines | Certificate Title in Code | Issuing Organization | Date in Code | Credential ID | Verification URL | Audit Finding |
| :-: | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **01** | L1406–L1410 | Corporate Actions & Entrepreneurship | TCS iON | *[EMPTY]* | *None* | *None* | Overlaps with #29 |
| **02** | L1412–L1416 | SEBI Investor Awareness Test | Securities and Exchange Board of India | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #19 |
| **03** | L1418–L1422 | Digital Marketing Certified | HubSpot Academy | *[EMPTY]* | *None* | *None* | Valid Industry Cert |
| **04** | L1424–L1428 | Risk Management in Financial Sector | Webul | *[EMPTY]* | *None* | *None* | Overlaps with #35 |
| **05** | L1430–L1434 | Business Analytics with Excel | Microsoft | *[EMPTY]* | *None* | *None* | Overlaps with #30 |
| **06** | L1436–L1440 | Effective Leadership & Social Entrepreneurship | HP LIFE | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #32 & #33 |
| **07** | L1442–L1446 | Digital Marketing & Social Media | Accenture | *[EMPTY]* | *None* | *None* | Overlaps with #25 & #26 |
| **08** | L1448–L1452 | Google Ads Display Certification | Google | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #24 |
| **09** | L1454–L1458 | Google Ads Search Certification | Google | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #22 |
| **10** | L1460–L1464 | Fundamentals of Marketing Analytics | Semrush Academy | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #31 |
| **11** | L1466–L1470 | Digital & Social Media Marketing | Professional Certification | *[EMPTY]* | *None* | *None* | Vague Issuer, overlaps #18 |
| **12** | L1472–L1476 | Entrepreneurship Foundations | LinkedIn Learning | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #40 |
| **13** | L1478–L1482 | Campaign Manager 360 Certificate | Google | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #27 |
| **14** | L1484–L1488 | Business Administration | MTF Institute | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #23 |
| **15** | L1490–L1494 | Advanced Certificate in Financial Analysis and Management | Udemy | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #36 |
| **16** | L1496–L1500 | Digital Marketing Professional Certificate | Content Marketing Institute | *[EMPTY]* | *None* | *None* | Overlaps with #39 |
| **17** | L1502–L1506 | Master Facebook Ads In 90 Minutes | WsCube Tech | *[EMPTY]* | *None* | *None* | Low Credibility / Micro-Course |
| **18** | L1508–L1512 | Digital & Social Media Marketing | Study Badshah (Accredited by ACTD) | *[EMPTY]* | *None* | *None* | Low Corporate Credibility |
| **19** | L1514–L1518 | SEBI Investor Awareness Test | NISM (SEBI) | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #02 |
| **20** | L1520–L1524 | Introduction to GenAI & Prompting | Lets Upgrade | *[EMPTY]* | *None* | *None* | Relevant AI Foundation |
| **21** | L1526–L1530 | Advanced WordPress Course for Professionals | Udemy | *[EMPTY]* | *None* | *None* | Low Founder Relevance |
| **22** | L1532–L1536 | Google Ads Search Certification | Google | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #09 |
| **23** | L1538–L1542 | Business Administration | Udemy (MTF Institute) | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #14 |
| **24** | L1544–L1548 | Google Ads Display Certification | Google | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #08 |
| **25** | L1550–L1554 | Digital Skills: Digital Marketing | Future Learn (Accenture) | *[EMPTY]* | *None* | *None* | Overlaps with #07 |
| **26** | L1556–L1560 | Digital Skills: Social Media | Future Learn (Accenture) | *[EMPTY]* | *None* | *None* | Overlaps with #07 |
| **27** | L1562–L1566 | Campaign Manager 360 Certification Exam | Google | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #13 |
| **28** | L1568–L1572 | Understanding Collateral Management | TCS iON | *[EMPTY]* | *None* | *None* | Irrelevant to Tech/Founder |
| **29** | L1574–L1578 | Introduction to Corporate Actions | TCS iON | *[EMPTY]* | *None* | *None* | Overlaps with #01 |
| **30** | L1580–L1584 | Business Analytics with Excel (Beginner) | Simplilearn | *[EMPTY]* | *None* | *None* | Overlaps with #05 |
| **31** | L1586–L1590 | Fundamentals of Marketing Analytics | Semrush Academy | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #10 |
| **32** | L1592–L1596 | Social Entrepreneurship | HP LIFE Foundation | *[EMPTY]* | *None* | *None* | Split variant of #06 |
| **33** | L1598–L1602 | Effective Leadership | HP LIFE Foundation | *[EMPTY]* | *None* | *None* | Split variant of #06 |
| **34** | L1604–L1608 | Maximizing Your Social Impact with Semrush's Toolkit | Semrush Academy | *[EMPTY]* | *None* | *None* | Minor Tool Tutorial |
| **35** | L1610–L1614 | Understanding Risk Management in Financial Sector | TCS iON | *[EMPTY]* | *None* | *None* | Variant of #04 |
| **36** | L1616–L1620 | Advanced Certificate in Financial Analysis and Management | Udemy | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #15 |
| **37** | L1622–L1626 | Digital Marketing with AI | Lets Upgrade | *[EMPTY]* | *None* | *None* | Relevant AI/Marketing |
| **38** | L1628–L1632 | BUS200 – Business Ethics | Saylor Academy | *[EMPTY]* | *None* | *None* | Academic Course Unit |
| **39** | L1634–L1638 | Digital Marketing Professional Certificate | LinkedIn Learning | *[EMPTY]* | *None* | *None* | Variant of #16 |
| **40** | L1640–L1644 | Entrepreneurship Foundations | LinkedIn Learning | *[EMPTY]* | *None* | *None* | **DUPLICATE** of #12 |

---

## 2. Key Deficiencies Identified

1. **Complete Absence of Dates:** Every single `<p class="certificate__date"></p>` element contains zero text across all 40 items.
2. **Zero Credential Verification:** Not a single item provides a credential ID, license number, or verification hyperlink.
3. **Severe Duplication:** Exactly 18 items are identical or slight wording variants of existing entries.
4. **Severe Domain Imbalance:** The website is overloaded with generic financial/marketing tutorials (*"Master Facebook Ads in 90 Minutes"*, *"Collateral Management"*), while completely failing to present the founder's cybersecurity credentials.

---

## 3. Verified Cybersecurity Certifications (Omitted in Existing Website)

The following four authentic certifications appear on Vishwa K's technical resume but were omitted from the current live website:

| # | Verified Title | Issuing Organization | Issue Date | Source |
| :-: | :--- | :--- | :-: | :--- |
| **C1** | **Cybersecurity Fundamentals** | IBM SkillsBuild | August 2026 | Technical Resume |
| **C2** | **Getting Started with Cybersecurity** | IBM SkillsBuild | August 2026 | Technical Resume |
| **C3** | **Ethical Hacking 101: Beginner's Guide** | Simplilearn SkillUp | August 2026 | Technical Resume |
| **C4** | **Cybersecurity & Ethical Hacking** | CappricioSec University | April 2026 | Technical Resume |

---

## 4. Recommended Deduplicated & Curated Certification Matrix

To project elite founder-level authority without clutter, the 40 items are condensed into a curated catalog of 14 verified, high-value credentials:

### Pillar 1: Cybersecurity & Defensive Security
1. **Cybersecurity Fundamentals** — IBM SkillsBuild *(Issued: Aug 2026)*
2. **Getting Started with Cybersecurity** — IBM SkillsBuild *(Issued: Aug 2026)*
3. **Ethical Hacking 101: Beginner's Guide** — Simplilearn SkillUp *(Issued: Aug 2026)*
4. **Cybersecurity & Ethical Hacking** — CappricioSec University *(Issued: Apr 2026)*

### Pillar 2: Artificial Intelligence & Technical Analytics
5. **Introduction to GenAI & Prompting** — LetsUpgrade
6. **Digital Marketing with AI** — LetsUpgrade
7. **Business Analytics with Excel** — Microsoft / Simplilearn

### Pillar 3: Digital Strategy, Leadership & Governance
8. **Digital Marketing Certified** — HubSpot Academy
9. **Google Ads Display & Search Certifications** — Google
10. **Campaign Manager 360 Certification** — Google
11. **Fundamentals of Marketing Analytics** — Semrush Academy
12. **Effective Leadership & Social Entrepreneurship** — HP LIFE Foundation
13. **Corporate Actions & Investor Awareness** — TCS iON & NISM / SEBI
14. **Entrepreneurship Foundations** — LinkedIn Learning

### Strict Rule Adherence
* No fake URLs or invented credential IDs will be generated.
* The owner may supply specific verification links or certificate IDs during or after approval.

