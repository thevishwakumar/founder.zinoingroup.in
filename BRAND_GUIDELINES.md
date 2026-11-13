# Zinoin Group Brand & Design System Guidelines
**Project:** Zinoin Founder Website  
**Entity:** Zinoin Group / Zinoin Tech Services  
**Founder:** Vishwa K  
**Document Version:** 1.0.0 (Brand Audit & Specifications)  

---

## 1. Logo Asset Inspection & Verification

The official Zinoin Group corporate logo assets were directly inspected from local archives (`zinoingroup.in.zip` and root vector/raster files).

### 1.1 Inspected Logo Variants
1. **`main logo.png` (Primary Web Asset):**
   * **Location:** `zinoingroup.in/images/main logo.png`
   * **Dimensions:** 497 × 557 px
   * **Format:** 32-bit RGBA (True transparency)
   * **Visual Form:** Geometric, multifaceted isometric tech emblem composed of interlocking hexagonal facets and network vertices, symbolizing structural security, data interconnectedness, and digital architecture.
2. **`main logo.webp` (Compressed Web Asset):**
   * **Dimensions:** 497 × 557 px | Size: 31.4 KB
   * **Optimization:** High-fidelity WebP format for fast web delivery.
3. **`zinoin tech.png` (Master Hi-Res Asset):**
   * **Dimensions:** 1056 × 1076 px
   * **Application:** High-resolution print, presentation headers, and large-scale media.

---

## 2. Official Corporate Color Palette

Color analysis of the logo pixels (over 106,800 visible pixels) and the verified corporate stylesheet (`zinoin.css`) establishes the definitive palette:

```
[ Primary Blue ]      #3b82f6 / #1f72aa    (Core Brand / Identity)
[ Primary Dark ]      #2563eb / #1d70a6    (Interactive / Active States)
[ Secondary Navy ]    #0f172a              (Corporate Authority / Dark Mode Background)
[ Electric Accent ]   #6366f1              (Focus / Gradients / Highlights)
[ Cyan Accent ]       #38bdf8 / #3199c8    (Secondary Logo Gradient)
[ Light Background ]  #ffffff              (Clean Canvas)
[ Light Surface ]     #f8fafc              (Card & Section Surface)
[ Text Main ]         #1e293b              (High-contrast Slate)
[ Text Muted ]        #64748b              (Subtle Body Copy)
[ Border Light ]      #e2e8f0              (Crisp Separation)
[ Border Dark ]       rgba(255,255,255,0.08) (Subtle Dark Mode Lines)
```

### 2.1 CSS Variables Implementation
```css
:root {
    /* Brand Color Scheme */
    --primary: #3b82f6;
    --primary-dark: #2563eb;
    --secondary: #0f172a;
    --accent: #6366f1;
    --accent-cyan: #38bdf8;
    
    /* Light Theme Surfaces & Text */
    --bg-color: #ffffff;
    --surface-color: #f8fafc;
    --card-bg: #ffffff;
    --text-color: #1e293b;
    --text-muted: #64748b;
    --border-color: #e2e8f0;
    
    /* Shadows & Glows */
    --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    --shadow-glow: 0 0 20px rgba(59, 130, 246, 0.35);

    /* Typography & Hierarchy */
    --font-heading: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    
    /* Dimensional Radii */
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 20px;
    --radius-full: 9999px;
    
    /* Transitions */
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Dark Theme Variables */
[data-theme="dark"] {
    --bg-color: #090d16;
    --surface-color: #0f172a;
    --card-bg: #131c2e;
    --text-color: #f1f5f9;
    --text-muted: #94a3b8;
    --border-color: rgba(255, 255, 255, 0.08);
    --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
    --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
    --shadow-glow: 0 0 25px rgba(59, 130, 246, 0.45);
}
```

---

## 3. Typography Hierarchy

The corporate standard established by Zinoin Group uses two modern sans-serif typefaces that pair technical precision with executive presence:

* **Primary Heading Typeface:** `Outfit` (Google Fonts)
  * Geometric, clean, wide aperture.
  * Weights: `600 (SemiBold)` for H2, H3 section headers; `700 (Bold)` for H1 Hero title.
* **Primary Body Typeface:** `Inter` (Google Fonts)
  * Industry benchmark for interface readability and micro-typography.
  * Weights: `400 (Regular)` for body copy; `500 (Medium)` for metadata tags; `600 (SemiBold)` for action buttons.
* **Fallbacks:** System font stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif`).

---

## 4. UI Component Design Specifications

### 4.1 Executive Navigation Bar
* **Position:** Fixed top with glassmorphic backing (`backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); background-color: rgba(255, 255, 255, 0.85);` in light mode; `rgba(9, 13, 22, 0.85)` in dark mode).
* **Emblem Integration:** Height 34px, accompanied by "Vishwa K" in 600 weight and a subtle "Founder" pill badge (`background: rgba(59, 130, 246, 0.1); color: var(--primary); font-size: 0.75rem; padding: 2px 8px; border-radius: 9999px;`).
* **Active Indicator:** Subtle bottom border glow (`box-shadow: 0 2px 0 var(--primary)`).

### 4.2 Hero Section Styling
* **Status Badge:**
  * Animated pulsing green/blue dot (`pulse-dot`) signaling active leadership and engineering initiatives.
* **Button Hierarchy:**
  * Primary Button: Solid `--primary` with subtle hover lift (`transform: translateY(-2px); box-shadow: var(--shadow-glow);`).
  * Secondary Button: Ghost border with transparent fill and subtle hover fill.

### 4.3 Project & Venture Cards
* **Structure:** Clean white or deep slate container with a 1px border.
* **Card Header:** Domain pill badge (e.g., `Cybersecurity / AI`, `Identity Governance`) on the left, executive role (e.g., `Founder & Developer`, `Lead Architect`) on the right.
* **Tech Stack Chips:** Subtly tinted badges (`background: var(--surface-color); border: 1px solid var(--border-color); font-size: 0.8rem;`) demonstrating architectural depth without visual noise.

### 4.4 Accessibility & Contrast Conformance
* All body copy meets **WCAG 2.1 AA** contrast requirements (minimum 4.5:1 ratio against light and dark backgrounds).
* Interactive focus states provide visible 2px outlines with 2px offset for keyboard navigation compliance.

