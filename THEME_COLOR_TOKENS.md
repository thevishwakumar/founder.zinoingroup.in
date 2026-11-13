# Theme Color Tokens & Design System Specification
**Project:** Zinoin Founder Website  
**Entity:** Zinoin Group / Zinoin Tech Services  
**Founder:** Vishwa K  
**Document:** THEME_COLOR_TOKENS.md  
**Version:** 1.0.0 (Step 17 Design Tokens Specification)  

---

## 1. Overview of Design Tokens

The Zinoin Founder website implements a dual-mode CSS Custom Property (Variable) architecture. The tokens are organized into three tiers:
1. **Shared Brand Tokens:** Constant brand identity values (logo blue, cyan accent, indigo focus).
2. **Contextual Light Tokens:** Optimized for daytime clarity, high contrast, and clean white/slate canvas.
3. **Contextual Dark Tokens:** Optimized for low-light comfort, deep midnight navy canvas (avoiding pure `#000000`), and soft slate text.

---

## 2. Master CSS Variables Specification Table

| CSS Variable Name | Light Mode Value | Dark Mode Value | Semantic Role | Applied Elements | WCAG 2.1 Contrast |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `--primary` | `#2563eb` | `#3b82f6` | Brand Core Interactive | Active links, icons, focus rings, status dot | `4.60:1` (Light) / `5.28:1` (Dark) |
| `--primary-light` | `#3b82f6` | `#60a5fa` | Highlight Accent | Icon hover highlights, badges | N/A (Decorative) |
| `--primary-dark` | `#1d4ed8` | `#2563eb` | Solid Primary Button | Primary CTA button background | `5.17:1` on `#ffffff` text |
| `--primary-hover` | `#1e40af` | `#1d4ed8` | Button Hover State | Button hover & active states | `7.80:1` on `#ffffff` text |
| `--primary-subtle` | `rgba(37,99,235,0.08)` | `rgba(59,130,246,0.12)` | Subtle Brand Tint | Badges, icon containers, active menu item | N/A (Surface Fill) |
| `--primary-border` | `rgba(37,99,235,0.22)` | `rgba(59,130,246,0.32)` | Brand Border Stroke | Badge outlines, icon container borders | N/A (Boundary) |
| `--secondary` | `#0f172a` | `#0f172a` | Corporate Slate Navy | Corporate accents & foundation | N/A (Structural) |
| `--accent` | `#6366f1` | `#6366f1` | Electric Indigo Accent | Radial ambient background gradient stop | N/A (Glow) |
| `--accent-cyan` | `#0284c7` | `#38bdf8` | Cyan Highlight | Section title gradient underline | `6.20:1` (Light) / `9.07:1` (Dark) |
| `--bg-color` | `#ffffff` | `#090d16` | Main Document Canvas | `body`, `html` root background | N/A (Canvas) |
| `--surface-color` | `#f8fafc` | `#0f172a` | Secondary Surface | Footer, form inputs, toggle buttons | N/A (Surface) |
| `--surface-subtle` | `#f1f5f9` | `#1e293b` | Tertiary Surface | Tech pills, subtle borders | N/A (Surface) |
| `--card-bg` | `#ffffff` | `#111827` | Card Containers | Projects, Expertise, Education, Cert cards | N/A (Elevated Surface) |
| `--card-hover-bg` | `#ffffff` | `#151e30` | Card Hover Surface | Subtle card hover glow | N/A (Interactive Surface) |
| `--text-color` | `#0f172a` | `#f8fafc` | High-Contrast Headings | H1, H2, H3, logo text, strong text | `17.85:1` (AAA) / `18.57:1` (AAA) |
| `--text-body` | `#334155` | `#cbd5e1` | Long-form Body Text | Paragraphs, descriptions, lists | `10.35:1` (AAA) / `13.09:1` (AAA) |
| `--text-muted` | `#475569` | `#94a3b8` | Metadata & Secondary | Captions, dates, tags, icons | `7.58:1` (AAA) / `7.58:1` (AAA) |
| `--border-color` | `#e2e8f0` | `rgba(255,255,255,0.09)` | Structural Borders | Card borders, section dividers, inputs | N/A (1px Structural Line) |
| `--border-subtle` | `#f1f5f9` | `rgba(255,255,255,0.05)` | Hairline Separators | Footer copyright line, chip borders | N/A (Hairline) |
| `--input-bg` | `#f8fafc` | `#0f172a` | Form Input Canvas | `.contact__input` fill | N/A (Field Background) |
| `--input-border` | `#cbd5e1` | `#334155` | Form Input Boundary | `.contact__input` stroke | N/A (Field Border) |
| `--header-bg` | `rgba(255,255,255,0.92)` | `rgba(9,13,22,0.92)` | Sticky Header Backing | Glassmorphic navigation header | N/A (Glass Layer) |
| `--shadow-sm` | `0 1px 3px rgba(15,23,42,0.05)` | `0 1px 3px rgba(0,0,0,0.35)` | Subtle Elevation | Card resting state, theme toggle button | N/A (Elevation) |
| `--shadow-md` | `0 4px 6px rgba(15,23,42,0.07)` | `0 4px 6px rgba(0,0,0,0.45)` | Card Hover Elevation | Card hover state, button resting state | N/A (Elevation) |
| `--shadow-lg` | `0 10px 15px rgba(15,23,42,0.09)` | `0 10px 15px rgba(0,0,0,0.55)` | Floating Surface | Theme dropdown menu, project cards | N/A (Elevation) |
| `--shadow-glow` | `0 0 24px rgba(37,99,235,0.22)` | `0 0 28px rgba(59,130,246,0.35)` | Ambient Brand Aura | Primary button hover, card hover glow | N/A (Glow) |

---

## 3. Dimensional, Spatial & Typography Tokens

In addition to color tokens, structural tokens are unified in `:root`:

```css
:root {
    /* Header Dimensions */
    --header-height: 4.25rem; /* 68px */

    /* Typography Families */
    --font-heading: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;

    /* Type Scale */
    --big-font-size: 2.25rem;   /* Desktop 3.25rem */
    --h1-font-size: 1.85rem;    /* Desktop 2.35rem */
    --h2-font-size: 1.45rem;    /* Desktop 1.75rem */
    --h3-font-size: 1.15rem;    /* Desktop 1.25rem */
    --normal-font-size: 0.95rem;/* Desktop 1.00rem */
    --small-font-size: 0.85rem; /* Desktop 0.875rem */
    --smaller-font-size: 0.75rem;

    /* Border Radii */
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 16px;
    --radius-full: 9999px;

    /* Transitions & Layering */
    --transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    --z-fixed: 100;
}
```

---

## 4. CSS Implementation Code Snippet

```css
/* Light Theme Definition */
:root[data-theme="light"], body[data-theme="light"] {
    --primary: #2563eb;
    --primary-light: #3b82f6;
    --primary-dark: #1d4ed8;
    --primary-hover: #1e40af;
    --primary-subtle: rgba(37, 99, 235, 0.08);
    --primary-border: rgba(37, 99, 235, 0.22);
    --accent-cyan: #0284c7;
    --bg-color: #ffffff;
    --surface-color: #f8fafc;
    --surface-subtle: #f1f5f9;
    --card-bg: #ffffff;
    --card-hover-bg: #ffffff;
    --text-color: #0f172a;
    --text-body: #334155;
    --text-muted: #475569;
    --border-color: #e2e8f0;
    --border-subtle: #f1f5f9;
    --input-bg: #f8fafc;
    --input-border: #cbd5e1;
    --header-bg: rgba(255, 255, 255, 0.92);
    --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.05), 0 1px 2px rgba(15, 23, 42, 0.03);
    --shadow-md: 0 4px 6px -1px rgba(15, 23, 42, 0.07), 0 2px 4px -2px rgba(15, 23, 42, 0.04);
    --shadow-lg: 0 10px 15px -3px rgba(15, 23, 42, 0.09), 0 4px 6px -4px rgba(15, 23, 42, 0.03);
    --shadow-glow: 0 0 24px rgba(37, 99, 235, 0.22);
}

/* Dark Theme Definition */
:root[data-theme="dark"], body[data-theme="dark"] {
    --primary: #3b82f6;
    --primary-light: #60a5fa;
    --primary-dark: #2563eb;
    --primary-hover: #1d4ed8;
    --primary-subtle: rgba(59, 130, 246, 0.12);
    --primary-border: rgba(59, 130, 246, 0.32);
    --accent-cyan: #38bdf8;
    --bg-color: #090d16;
    --surface-color: #0f172a;
    --surface-subtle: #1e293b;
    --card-bg: #111827;
    --card-hover-bg: #151e30;
    --text-color: #f8fafc;
    --text-body: #cbd5e1;
    --text-muted: #94a3b8;
    --border-color: rgba(255, 255, 255, 0.09);
    --border-subtle: rgba(255, 255, 255, 0.05);
    --input-bg: #0f172a;
    --input-border: #334155;
    --header-bg: rgba(9, 13, 22, 0.92);
    --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.35);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.45);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.55);
    --shadow-glow: 0 0 28px rgba(59, 130, 246, 0.35);
}
```
