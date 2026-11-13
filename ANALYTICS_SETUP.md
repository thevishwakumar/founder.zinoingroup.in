# Google Analytics 4 (GA4) & Privacy-Conscious Telemetry Setup
**Project:** Vishwa K – Founder Website  
**Domain:** [https://founder.zinoingroup.in/](https://founder.zinoingroup.in/)  
**Website Owner:** Vishwa K (Founder & Developer at Zinoin Group)  
**Date:** November 13, 2026  
**Document Version:** 1.0.0 (Analytics Strategy)  

---

## 1. Executive Summary & Privacy Principles

This document specifies the Google Analytics 4 (GA4) telemetry architecture implemented on `founder.zinoingroup.in`. The tracking infrastructure is designed around a **privacy-first philosophy**:
* **Zero Personally Identifiable Information (PII):** Form field inputs (names, email addresses, phone numbers, and message bodies) are strictly excluded from event telemetry.
* **Non-Intrusive Engagement Tracking:** Telemetry is limited to high-intent visitor interactions (outbound professional links, project views, and form completion).
* **Tag Orchestration via GTM:** Events are dispatched to `window.dataLayer`, natively compatible with the existing Google Tag Manager container (`GTM-N4T5ZSJJ`).
* **Zero Fabricated IDs:** No fake or placeholder Measurement IDs are sent over the network, ensuring zero 404 or bad-request errors.

---

## 2. Event Tracking Taxonomy & Schema

The application code contains automated event dispatchers that trigger custom events into `window.dataLayer`:

```javascript
/* Native Helper Function in index.html */
function trackEvent(eventName, params = {}) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
        event: eventName,
        ...params
    });
    if (typeof window.gtag === 'function') {
        window.gtag('event', eventName, params);
    }
}
```

### Event Specifications:

| Event Name | Trigger Condition | Event Parameters | Privacy / PII Status |
| :--- | :--- | :--- | :---: |
| **`page_view`** | Automatic upon initial DOM paint | Standard GA4 session metadata | Clean |
| **`contact_section_view`** | User scrolls and views >= 30% of Contact section | `{ section: "contact" }` | Clean |
| **`social_click`** | User clicks LinkedIn, GitHub, or Instagram profile link | `{ platform: "linkedin" | "github" | "instagram", target_url: "..." }` | Clean |
| **`project_click`** | User clicks project external/modal link | `{ project_name: "Zinoin Group" | "CampusBridge" | "TNT Calendar", target_url: "..." }` | Clean |
| **`contact_form_interaction`** | User focuses on first input field | `{ action: "form_start" }` | Clean (No text values) |
| **`contact_form_interaction`** | Web3Forms returns HTTP 200 success | `{ action: "submit_success" }` | Clean (Zero message data) |
| **`contact_form_interaction`** | Web3Forms returns error or network failure | `{ action: "submit_error" }` | Clean |

---

## 3. Google Tag Manager (GTM) Container Configuration

The website includes Google Tag Manager with container ID `GTM-N4T5ZSJJ`.

### How to Connect GA4 via GTM:

1. Open [Google Tag Manager](https://tagmanager.google.com/).
2. Select container **GTM-N4T5ZSJJ**.
3. Create a **Google Tag (GA4 Configuration)**:
   * **Tag Type:** Google Tag
   * **Tag ID:** Enter your actual GA4 Measurement ID (`G-XXXXXXXXXX`).
   * **Triggering:** Initialization - All Pages (or All Pages).
4. Create **Custom Event Triggers**:
   * Create Trigger for `social_click` (Custom Event -> Event name: `social_click`).
   * Create Trigger for `project_click` (Custom Event -> Event name: `project_click`).
   * Create Trigger for `contact_section_view` (Custom Event -> Event name: `contact_section_view`).
   * Create Trigger for `contact_form_interaction` (Custom Event -> Event name: `contact_form_interaction`).
5. Create **GA4 Event Tags**:
   * Tag Type: Google Analytics: GA4 Event
   * Configuration Tag: None (use Measurement ID) or select the Google Tag created in Step 3.
   * Event Name: `{{Event}}`
   * Event Parameters: Map Data Layer Variables for `platform`, `target_url`, `project_name`, and `action`.
6. Click **Submit** -> **Publish** container.

---

## 4. Privacy & Consent Management

1. **IP Anonymization:** Google Analytics 4 automatically enables IP masking/anonymization by default, ensuring individual visitor IP addresses are never logged or stored.
2. **Form Data Privacy:** Form fields (`#contact-name`, `#contact-email`, `#contact-phone`, `#contact-message`) transmit directly to the encrypted Web3Forms submission endpoint and are **never** passed into `dataLayer` or Google Analytics.
3. **Cloudflare Web Analytics Alternative:**
   * In addition to GA4, the site includes Cloudflare Web Analytics (`beacon.min.js`), which is 100% cookieless and GDPR compliant out of the box without requiring a cookie consent banner.

---

## 5. Testing & Verification

1. In GTM, click **Preview** and enter `https://founder.zinoingroup.in/`.
2. Open Tag Assistant debug window.
3. Perform the following actions on the site:
   * Scroll down to the Contact section -> Verify `contact_section_view` fires.
   * Click on the LinkedIn icon in the hero section -> Verify `social_click` fires with `platform: "linkedin"`.
   * Click on the Zinoin Group project card -> Verify `project_click` fires with `project_name: "Zinoin Group"`.
   * Click into the name field on the contact form -> Verify `contact_form_interaction` fires with `action: "form_start"`.
4. In Google Analytics 4, open **Realtime Overview** to verify live event streams.
