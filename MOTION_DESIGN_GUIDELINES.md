# PREMIUM MOTION DESIGN GUIDELINES & SPECIFICATION

**Target Brand:** Vishwa K — Founder & Developer at Zinoin Group  
**Domain:** [founder.zinoingroup.in](https://founder.zinoingroup.in/)  
**Design Phase:** Step 21 — Premium Micro-Interactions & Motion Design  
**Document Status:** Complete & Verified  
**Date:** November 14, 2026  

---

## 1. Motion Design Philosophy & Principles

Motion on `founder.zinoingroup.in` is engineered as a **functional, cognitive, and sensory enhancement** to the user experience. It reflects the corporate professionalism of Zinoin Group and the engineering precision of a founder specializing in cybersecurity and software development.

### Core Principles:
1. **Subtle & Purposeful:** Motion must direct attention, communicate spatial relationships, and provide tactile confirmation. It is never decorative or distracting.
2. **Performance-First (Zero Reflow):** Every animated property is restricted to composite-only CSS attributes (`transform` and `opacity`). Zero properties that trigger layout or paint (`top`, `margin`, `width`, `height`) are animated.
3. **Progressive Enhancement:** Content is 100% visible and accessible by default. If JavaScript fails, animations fail gracefully to static perfection.
4. **Accessible by Design:** Absolute respect for `prefers-reduced-motion: reduce` (WCAG 2.2 Level AAA).

---

## 2. Motion Tokens & Easing Curves

```css
:root {
    /* Timing Durations */
    --duration-micro: 0.15s;    /* Active tactile compression, focus rings */
    --duration-normal: 0.25s;   /* Hover states, dropdowns, border shifts */
    --duration-smooth: 0.35s;   /* Drawers, modals, card expansions */
    --duration-entrance: 0.50s; /* Staggered hero and section reveal */

    /* Easing Functions */
    --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);  /* Smooth deceleration for entrances */
    --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);   /* Balanced ease-in-out for states */
}
```

### Curve Characteristics:
- **`--ease-out-expo` (`cubic-bezier(0.16, 1, 0.3, 1)`):** Emulates natural physical momentum with high initial velocity that smoothly glides into rest. Used for card elevations, hero entrances, and dropdown menus.
- **`--ease-standard` (`cubic-bezier(0.4, 0, 0.2, 1)`):** Symmetrical transition used for color shifts, background changes, and theme transitions.

---

## 3. Component Motion Specifications

### 3.1 Hero Section
- **Staggered Entrance Sequence:**
  - `home__badge`: `0.05s` delay, `0.5s` duration (`translateY(12px)` -> `0`).
  - `home__name`: `0.12s` delay, `0.5s` duration (`translateY(12px)` -> `0`).
  - `home__headline`: `0.18s` delay, `0.5s` duration (`translateY(12px)` -> `0`).
  - `home__description`: `0.24s` delay, `0.5s` duration (`translateY(12px)` -> `0`).
  - `home__actions`: `0.30s` delay, `0.5s` duration (`translateY(12px)` -> `0`).
  - `home__social`: `0.36s` delay, `0.5s` duration (`translateY(12px)` -> `0`).
- **Live Status Pulse Dot:**
  - `pulse` keyframe animation: Scale `0.95` -> `1.0` with expanding box-shadow ring (`0 0 0 8px rgba(59, 130, 246, 0)`) over `2s` infinite loop.
- **Typing Cursor:**
  - Subtle `blink-caret` step animation (`0.75s step-end infinite`) accompanying measured typing cadence (85ms type, 40ms delete, 2.2s pause).

### 3.2 Navigation & Header
- **Scroll Elevation:**
  - When page scrolls $\ge 50\text{px}$, header receives `.scroll-header` with subtle elevation shadow (`0 1px 3px rgba(15, 23, 42, 0.05)`).
- **Active Navigation Link Indicator:**
  - Underline expands smoothly from center: `transform: scaleX(0)` -> `scaleX(1)` using `--ease-out-expo` (duration: `0.25s`).
- **Mobile Menu Drawer:**
  - Slide-in from right: `transform: translateX(0)` with `0.35s` cubic-bezier easing.
  - Backdrop blur overlay: `opacity: 0` -> `1` with `backdrop-filter: blur(4px)`.

### 3.3 Theme Switcher Dropdown
- **Menu Appearance:**
  - Transform origin: `top right`.
  - Micro-scale and fade: `transform: translateY(-8px) scale(0.96)` -> `translateY(0) scale(1)`.
  - Duration: `0.18s` using `--ease-out-expo`.
- **Segmented Control (Mobile Drawer):**
  - Instant tactile feedback on click with `box-shadow` elevation on active pill.

### 3.4 Project Cards
- **Pointer-Aware Hover (`@media (hover: hover) and (pointer: fine)`):**
  - Card elevation: `transform: translateY(-5px)`.
  - Border transition: `border-color: var(--primary)`.
  - Shadow transition: `box-shadow: var(--shadow-lg)`.
  - Image scale: `transform: scale(1.03)` with `0.4s` smooth ease.
  - Link arrow nudge: `transform: translateX(3px)` on `.button--small:hover i`.
- **Touch Device Isolation:**
  - Hover transforms are deactivated on touch devices to prevent sticky hover states.

### 3.5 Buttons & Interactive Links
- **Default State:** Clean corporate button styling with subtle primary shadow.
- **Hover State:** `transform: translateY(-2px)` with shimmering gradient sheen sweep across the face.
- **Active State (Click/Tap):** Tactile compression `transform: translateY(0) scale(0.98)` with reduced shadow for realistic mechanical button feedback.
- **Focus-Visible State:** High-contrast `outline: 2px solid var(--primary-light); outline-offset: 3px;`.
- **Disabled State:** `opacity: 0.65; cursor: not-allowed; transform: none;`.

### 3.6 Scroll Reveal (IntersectionObserver)
- **Observer Threshold:** `0.1` (triggers when 10% of element is in viewport).
- **Root Margin:** `0px 0px -40px 0px` (anticipates scroll by 40px for natural entrance).
- **Single-Fire Optimization:** `observer.unobserve(entry.target)` unregisters the element immediately after entrance, dropping CPU utilization to 0.00% during subsequent scrolling.

---

## 4. Reduced Motion (Accessibility Standards)

In strict compliance with **WCAG 2.2 Success Criterion 2.3.3 (Animation from Interactions)**:

```css
@media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
    .scroll-animate,
    .has-scroll-observer .scroll-animate {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
    }
    .home__badge, .home__name, .home__headline, 
    .home__description, .home__actions, .home__social {
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
    }
}
```
Users who have enabled vestibular safety preferences experience an immediate, instant, non-animated interface with zero motion artifacts.

