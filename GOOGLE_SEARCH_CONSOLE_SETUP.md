# GOOGLE SEARCH CONSOLE SETUP & MONITORING MANUAL

**Target Domain:** [https://founder.zinoingroup.in/](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa Kumar (Founder & Developer at Zinoin Group)  
**Target Platform:** Google Search Central / Google Search Console  
**Document Version:** 2.0.0 (Production Release Guide)  
**Status:** Actionable Setup Manual for Website Owner  

---

## 1. Overview & Immediate Objective

Google Search Console (GSC) is Google's official, direct communication channel with website owners. To rank for **"Vishwa"**, **"Vishwa Kumar"**, and **"Vishwa Zinoin"**, claiming ownership and requesting immediate Googlebot indexing is mandatory.

> [!IMPORTANT]
> **Owner Action Required**  
> Google Search Console ownership requires access to either your Google account or your Cloudflare DNS dashboard. Follow the step-by-step instructions below.

---

## 2. Step 1: Claim & Verify Property in GSC

Google offers two property types: **Domain Property** (recommended) or **URL Prefix**.

### Method A: Domain Property via Cloudflare DNS (Recommended)
This single verification covers all current and future subdomains (`founder.zinoingroup.in`, `zinoingroup.in`, etc.):
1. Visit [search.google.com/search-console](https://search.google.com/search-console) and sign in with your Google account.
2. In the property selector dropdown, click **Add property**.
3. Under **Domain**, enter: `zinoingroup.in` (do not add `https://` or `www`). Click **Continue**.
4. Google will generate a **TXT verification record** (e.g., `google-site-verification=XXXXXXXXXXXXXXXXXXXXX`). Copy this string.
5. In a new tab, log into your [Cloudflare Dashboard](https://dash.cloudflare.com/):
   - Select your domain `zinoingroup.in`.
   - Go to **DNS** ➔ **Records** ➔ Click **Add record**.
   - **Type:** `TXT`
   - **Name:** `@` (or `zinoingroup.in`)
   - **Content:** Paste the copied `google-site-verification=...` string.
   - **TTL:** Auto. Click **Save**.
6. Return to Google Search Console and click **Verify**.
   *Result: Instant verification via Cloudflare Anycast DNS.*

---

### Method B: URL Prefix Property (Alternative)
1. In Google Search Console, under **URL prefix**, enter: `https://founder.zinoingroup.in/`.
2. Select **HTML tag** verification.
3. Copy the meta tag code provided.
4. Place it in `<head>` of `index.html` (or provide it to your engineer).
5. Click **Verify**.

---

## 3. Step 2: Submit the XML Sitemap

Once verified:
1. In the left navigation of GSC, click **Sitemaps** (under *Indexing*).
2. Under **Add a new sitemap**, type: `sitemap.xml`.
3. The full URL will display as: `https://founder.zinoingroup.in/sitemap.xml`.
4. Click **Submit**.
5. Within a few moments, the Status column should display **Success** (Green), confirming that Googlebot has successfully parsed your canonical URL.

---

## 4. Step 3: Trigger Rapid Indexing via URL Inspection

Do not wait weeks for Googlebot to discover the site passively:
1. At the top of GSC, locate the search bar: **Inspect any URL in "founder.zinoingroup.in"**.
2. Paste: `https://founder.zinoingroup.in/` and press Enter.
3. Google will report: *URL is not on Google* (since it is newly launched).
4. Click **Test Live URL** (takes ~30 seconds; tests mobile rendering and HTTP 200 response).
5. Once the live test confirms *URL is available to Google*, click **Request Indexing**.
   *Result: Google puts your homepage into a high-priority crawling queue (typically crawled within 24 to 72 hours).*

---

## 5. Step 4: Configure Performance Query Tracking

To monitor your ascent for "Vishwa" and related personal queries:
1. Navigate to **Performance** ➔ **Search results**.
2. Click **+ New** ➔ Select **Query**.
3. Choose **Queries containing** and enter: `Vishwa`.
4. This filter will display:
   - Total Impressions (how many times you appeared in search results for queries containing Vishwa).
   - Total Clicks (how many people clicked to your site).
   - Average CTR (Click-Through Rate).
   - Average Position (your exact ranking number in SERPs).

### Core Queries to Track Weekly:
* `Vishwa`
* `Vishwa Kumar`
* `Vishwa K`
* `thevishwakumar`
* `Vishwa Zinoin`
* `Vishwa Zinoin Group`
* `Vishwa Founder`
* `Vishwa Developer`
* `Vishwa Cyber Security`

---

## 6. Step 5: Monitor Page Experience & Core Web Vitals

* Under **Experience** in GSC:
  - Check **Page Experience**: Confirm 100% of URLs provide a Good page experience.
  - Check **Core Web Vitals**: Monitor mobile and desktop status as field data accumulates over the first 28 days.
  - Check **HTTPS**: Confirm valid SSL status.
