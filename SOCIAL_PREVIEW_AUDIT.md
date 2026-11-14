# SOCIAL SHARING & OPEN GRAPH PREVIEW AUDIT

**Target Domain:** [https://founder.zinoingroup.in/](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Supported Platforms:** LinkedIn, Twitter/X, WhatsApp, Telegram, Slack, Discord, Facebook  
**Document Status:** Complete & Verified  
**Date:** November 14, 2026  

---

## 1. Executive Summary

Social preview optimization ensures that whenever `https://founder.zinoingroup.in/` is shared across social media platforms, professional networks, or messaging applications, it renders an eye-catching, accurate, and professional card rather than a bare hyperlink or broken snippet.

### Core Achievements:
- Implemented **15 Open Graph (OG) tags** including specialized `profile:*` properties.
- Implemented **7 Twitter / X Card tags** configured for high-visibility `summary_large_image` format.
- Standardized image dimensions (`1200 x 630 px`) with secure HTTPS image paths (`og:image:secure_url`).
- Perfect entity harmony between title, description, and visual asset across all scrapers.

---

## 2. Implemented Social Sharing Tag Inventory

### 2.1 Open Graph Protocol (ogp.me) Metadata

```html
<!-- Open Graph Metadata (Facebook, LinkedIn, Slack, WhatsApp) -->
<meta property="og:type" content="profile">
<meta property="og:title" content="Vishwa K | Founder & Developer at Zinoin Group">
<meta property="og:description" content="Discover Vishwa K (Vishwa Kumar), Founder & Developer at Zinoin Group. Exploring cybersecurity engineering, technology innovation, software development, and entrepreneurship.">
<meta property="og:url" content="https://founder.zinoingroup.in/">
<meta property="og:image" content="https://founder.zinoingroup.in/assets/img/about.jpg">
<meta property="og:image:secure_url" content="https://founder.zinoingroup.in/assets/img/about.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Vishwa K — Founder & Developer at Zinoin Group portrait photograph">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:site_name" content="Vishwa K - Zinoin Group">
<meta property="og:locale" content="en_US">
<meta property="profile:first_name" content="Vishwa">
<meta property="profile:last_name" content="K">
<meta property="profile:username" content="thevishwakumar">
```

### 2.2 Twitter / X Cards Specification

```html
<!-- Twitter/X Card Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Vishwa K | Founder & Developer at Zinoin Group">
<meta name="twitter:description" content="Discover Vishwa K (Vishwa Kumar), Founder & Developer at Zinoin Group. Exploring cybersecurity engineering, technology innovation, software development, and entrepreneurship.">
<meta name="twitter:image" content="https://founder.zinoingroup.in/assets/img/about.jpg">
<meta name="twitter:image:alt" content="Vishwa K — Founder & Developer at Zinoin Group portrait photograph">
<meta name="twitter:creator" content="@thevishwakumar">
<meta name="twitter:site" content="@thevishwakumar">
```

---

## 3. Platform Visual Simulation & Card Previews

### 3.1 LinkedIn Post & Feed Preview
- **Card Type:** Large Rich Link Preview
- **Title:** `Vishwa K | Founder & Developer at Zinoin Group`
- **Domain:** `founder.zinoingroup.in`
- **Image Display:** Prominently featured high-resolution 1.91:1 ratio banner preview.
- **Snippet:** Shows full two-sentence summary highlighting Zinoin Group leadership and cybersecurity engineering.

### 3.2 Twitter / X Large Summary Card
- **Card Format:** `summary_large_image`
- **Attribution:** `@thevishwakumar` (links author card to official X profile).
- **Visual Impact:** Expands across the full width of the user's feed, maximizing click-through rates.

### 3.3 WhatsApp & Telegram Messaging Previews
- **Thumbnail:** Compact square thumbnail generated from `og:image`.
- **Title & Description:** Automatically formatted below message input field with zero latency.

### 3.4 Slack & Discord Rich Embeds
- **Color Accent:** Inherits brand theme colors from HTML document background.
- **Embed Header:** `Vishwa K - Zinoin Group` (`og:site_name`).
- **Media:** Full-bleed embedded visual asset with alt text accessibility tag.

---

## 4. Official Social Scraper Verification Tools

When updating website content, use these official platform scrapers to clear cache and refresh preview data:

1. **LinkedIn Post Inspector:**  
   [https://www.linkedin.com/post-inspector/](https://www.linkedin.com/post-inspector/)  
   *Input `https://founder.zinoingroup.in/` -> Click Inspect to clear LinkedIn's 7-day OG cache.*

2. **Facebook Sharing Debugger:**  
   [https://developers.facebook.com/tools/debug/](https://developers.facebook.com/tools/debug/)  
   *Click "Scrape Again" to refresh WhatsApp and Facebook card previews.*

3. **Twitter / X Card Preview:**  
   *Post URL in a test draft to view live rendering.*

