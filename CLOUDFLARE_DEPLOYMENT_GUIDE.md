# CLOUDFLARE DEPLOYMENT & PRODUCTION HOSTING GUIDE

**Production Domain:** https://founder.zinoingroup.in/  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Target Platform:** Cloudflare Pages & Cloudflare Edge Proxy  
**Document Version:** 1.0.0 (Production Release Guide)  
**Status:** Pre-Deployment Architectural Guide (Zero Automated Deployment Triggered)

---

## 1. Cloudflare Infrastructure Overview

The production domain `founder.zinoingroup.in` actively utilizes Cloudflare for DNS management, edge proxying, and global CDN caching. 

### Why Cloudflare Pages is the Optimal Hosting Target:
1. **Global Anycast CDN:** Deploys content to 330+ edge data centers worldwide, delivering **sub-25ms Time-To-First-Byte (TTFB)**.
2. **Native HTTP/3 & QUIC Support:** Eliminates head-of-line blocking and provides instant 0-RTT handshakes for mobile visitors.
3. **Automated Brotli Compression:** Automatically compresses HTML, CSS, JS, and SVG assets by an additional 15–20% compared to standard Gzip.
4. **Zero Cold Starts & High Reliability:** Because the site is pure static HTML/CSS/JS, there is zero server runtime overhead or container boot time.
5. **Instant Rollbacks:** Cloudflare Pages preserves historical deployment artifacts, enabling 1-click instantaneous rollbacks.

---

## 2. Edge Configuration Files (`_headers` and `_redirects`)

Cloudflare Pages natively parses two configuration files placed in the project root directory:

### A. Edge Security & Caching Headers (`_headers`)
Placing a `_headers` file in `founder.zinoingroup.in/` instructs Cloudflare edge servers to return modern HTTP security and cache headers on every request:

```http
# Global Security Headers for All Routes
/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Cache-Control: public, max-age=3600, must-revalidate

# Long-Lived Immutable Cache for Static Image Assets
/assets/img/*
  Cache-Control: public, max-age=31536000, immutable

# Favicon Caching
/favicon.ico
  Cache-Control: public, max-age=604800, must-revalidate

# Search Engine Index Maps
/robots.txt
  Cache-Control: public, max-age=86400, must-revalidate
/sitemap.xml
  Cache-Control: public, max-age=86400, must-revalidate
```

### B. Routing & Canonical Redirects (`_redirects`)
Placing a `_redirects` file in `founder.zinoingroup.in/` normalizes incoming URLs:

```text
# Ensure trailing slash consistency
/index.html   /   301!

# Custom 404 Error Routing
/*   /404.html   404
```

---

## 3. Step-by-Step Deployment Methods

Depending on the owner's hosting workflow, deployment can be executed via either of two standard paths:

### Method 1: Cloudflare Pages Direct Git Integration (Recommended)
1. **Repository Connection:**
   - Log into the [Cloudflare Dashboard](https://dash.cloudflare.com/).
   - Navigate to **Workers & Pages** ➔ **Create Application** ➔ **Pages** ➔ **Connect to Git**.
   - Select the GitHub repository `thevishwakumar/founder.zinoingroup.in` (or relevant repo).
2. **Build Configuration Settings:**
   - **Framework Preset:** `None` (Static HTML)
   - **Build Command:** *(Leave Empty — no build step required)*
   - **Build Output Directory:** `founder.zinoingroup.in` (or root `/` if repository root contains `index.html`)
3. **Custom Domain Association:**
   - In the Pages project dashboard, navigate to **Custom Domains**.
   - Click **Set up a domain** and input: `founder.zinoingroup.in`.
   - Cloudflare will automatically provision Universal SSL certificates and route traffic to the Pages deployment.

---

### Method 2: Direct Upload via Wrangler CLI
If deploying directly from the terminal without Git continuous deployment:
```bash
# 1. Authenticate with Cloudflare
npx wrangler login

# 2. Deploy static folder to Cloudflare Pages
npx wrangler pages deploy founder.zinoingroup.in --project-name=founder-zinoingroup --branch=main
```

---

### Method 3: Origin Server with Cloudflare Proxy (Existing Web Host)
If the domain points to an Apache, Nginx, or cPanel origin server with Cloudflare proxy enabled (Orange Cloud icon):
1. Upload the files inside `founder.zinoingroup.in/` (`index.html`, `assets/`, `robots.txt`, `sitemap.xml`, `favicon.ico`) directly to the origin web root (e.g. `public_html/` or `/var/www/html/`).
2. Log into Cloudflare Dashboard and navigate to **Caching** ➔ **Configuration** ➔ **Purge Everything**.
3. Verify the live site at `https://founder.zinoingroup.in/`.

---

## 4. Cloudflare Dashboard Recommended Settings

To extract maximum performance and security without altering core functionality:

1. **SSL/TLS Encryption Mode:**  
   Set to **Full (Strict)**. This ensures end-to-end cryptographic encryption between browser, Cloudflare edge, and the origin server.
2. **Always Use HTTPS:**  
   Enable in **SSL/TLS** ➔ **Edge Certificates** to automatically redirect `http://` traffic to `https://`.
3. **Minimum TLS Version:**  
   Set to **TLS 1.2** (disables vulnerable legacy TLS 1.0 and 1.1 protocols).
4. **Auto Minify:**  
   In **Speed** ➔ **Optimization**, leave HTML minification enabled (or disabled, as CSS and JS are already optimized).
5. **Brotli Compression:**  
   Enable in **Speed** ➔ **Optimization** (provides superior compression over Gzip).
6. **Early Hints:**  
   Enable in **Speed** ➔ **Optimization** (accelerates 103 Early Hints for Google Fonts and preconnect directives).

---

## 5. Post-Deployment Cache Purge Procedure

Whenever new changes are deployed:
1. Navigate to **Cloudflare Dashboard** ➔ Select domain `zinoingroup.in`.
2. Go to **Caching** ➔ **Configuration**.
3. Click **Purge Everything** (or **Custom Purge** and enter `https://founder.zinoingroup.in/`).
4. Perform a hard refresh in Chrome (`Ctrl + Shift + R` or `Cmd + Shift + R`) to observe live updates immediately.

