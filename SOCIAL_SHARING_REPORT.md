# Social Sharing & Open Graph Optimization Report
**Project:** Vishwa K – Founder Website  
**Domain:** [https://founder.zinoingroup.in/](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date:** November 13, 2026  
**Document Version:** 1.0.0 (Social Metadata & Link Previews)  

---

## 1. Executive Summary

This report documents the Open Graph (OG) and Twitter/X Card metadata implemented on `founder.zinoingroup.in`. When links to the website are shared on LinkedIn, WhatsApp, Twitter/X, Slack, Discord, or Facebook, the messaging platform parses this metadata to render a rich, branded preview card featuring the official founder portrait, corporate branding, professional headline, and summary description.

---

## 2. Complete Open Graph & Twitter Cards Metadata

```html
<!-- Open Graph Metadata (Facebook, LinkedIn, Slack, WhatsApp) -->
<meta property="og:type" content="profile">
<meta property="og:title" content="Vishwa K | Founder & Developer at Zinoin Group">
<meta property="og:description" content="Discover Vishwa K, Founder & Developer at Zinoin Group, exploring technology, cybersecurity, digital innovation and entrepreneurship.">
<meta property="og:url" content="https://founder.zinoingroup.in/">
<meta property="og:image" content="https://founder.zinoingroup.in/assets/img/about.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Vishwa K — Founder & Developer at Zinoin Group">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:site_name" content="Vishwa K - Zinoin Group">
<meta property="og:locale" content="en_US">

<!-- Twitter/X Card Metadata -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Vishwa K | Founder & Developer at Zinoin Group">
<meta name="twitter:description" content="Discover Vishwa K, Founder & Developer at Zinoin Group, exploring technology, cybersecurity, digital innovation and entrepreneurship.">
<meta name="twitter:image" content="https://founder.zinoingroup.in/assets/img/about.jpg">
<meta name="twitter:image:alt" content="Vishwa K — Founder & Developer at Zinoin Group">
<meta name="twitter:creator" content="@thevishwakumar">
```

---

## 3. Platform-Specific Unfurling Behavior

### 3.1 LinkedIn Post & Message Previews
* **Display Format:** Large rich preview card with thumbnail image, prominent bold title, domain attribution (`founder.zinoingroup.in`), and a concise two-line summary snippet.
* **Preview Card Elements:**
  * **Title:** `Vishwa K | Founder & Developer at Zinoin Group`
  * **Subtitle:** `founder.zinoingroup.in`
  * **Snippet:** `Discover Vishwa K, Founder & Developer at Zinoin Group, exploring technology, cybersecurity, digital innovation and entrepreneurship.`
  * **Image:** Crisp portrait photo with high visual impact in professional news feeds.

### 3.2 WhatsApp Link Previews
* **Display Format:** WhatsApp loads a compact preview card when the URL is pasted into a chat.
* **Requirements Met:**
  * Uses absolute HTTPS image URL (`https://founder.zinoingroup.in/assets/img/about.jpg`).
  * Declares explicit dimensions (`og:image:width: 1200` and `og:image:height: 630`) and mime-type (`image/jpeg`), which prevents WhatsApp from dropping the thumbnail.
  * Image file size is lightweight (< 300 KB), ensuring instant thumbnail generation on mobile bandwidth.

### 3.3 Twitter / X Summary Large Image Card
* **Display Format:** Full-width image card banner stacked above the title and description.
* **Attributes:**
  * `twitter:card="summary_large_image"` triggers high-engagement visual banner rendering rather than a tiny square thumbnail.
  * `twitter:creator="@thevishwakumar"` links the shared post to the owner's personal brand handle.

### 3.4 Slack & Discord Rich Snippets
* **Display Format:** Displays a color-accented embed block with title, site name ("Vishwa K - Zinoin Group"), description, and thumbnail image.

---

## 4. Preview Debugging & Cache Invalidation Tools

When sharing links immediately after deployment, social platforms may cache initial metadata. Use the following official debugging tools to inspect and flush cache:

1. **LinkedIn Post Inspector:**
   * URL: [https://www.linkedin.com/post-inspector/](https://www.linkedin.com/post-inspector/)
   * Action: Enter `https://founder.zinoingroup.in/` and click **Inspect**. This forces LinkedIn to immediately re-crawl the page and update its cached preview.
2. **Facebook / WhatsApp Sharing Debugger:**
   * URL: [https://developers.facebook.com/tools/debug/](https://developers.facebook.com/tools/debug/)
   * Action: Enter `https://founder.zinoingroup.in/` and click **Scrape Again**. WhatsApp shares Facebook's crawler cache, so scraping here updates WhatsApp previews globally.
3. **Twitter / X Card Preview:**
   * Test by drafting a tweet containing `https://founder.zinoingroup.in/` in the web composer to verify card rendering before posting.
