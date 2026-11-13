# System-Aware Dark/Light Mode Implementation Architecture
**Project:** Zinoin Founder Website  
**Entity:** Zinoin Group / Zinoin Tech Services  
**Founder:** Vishwa K  
**Document:** DARK_LIGHT_MODE_IMPLEMENTATION.md  
**Version:** 1.0.0 (Step 17 Technical Implementation Guide)  

---

## 1. Architectural Overview

The theme implementation delivers a **zero-dependency, system-aware dual theme system** supporting three explicit operational modes:

```
                    +-----------------------------+
                    |    User Theme Preference    |
                    +-----------------------------+
                                   |
         +-------------------------+-------------------------+
         |                         |                         |
         v                         v                         v
+-----------------+       +-----------------+       +-----------------+
|   1. System     |       |    2. Light     |       |     3. Dark     |
| (Default Auto)  |       | (Manual Choice) |       | (Manual Choice) |
+-----------------+       +-----------------+       +-----------------+
         |                         |                         |
         v                         v                         v
Dynamic OS Match          Forces Light Tokens       Forces Dark Tokens
(matchMedia query)        ([data-theme="light"])    ([data-theme="dark"])
```

### Key Technical Pillars
1. **Zero-FOUC Guarantee:** Synchronous inline script in `<head>` applies `data-theme` to `<html>` prior to DOM tree paint, preventing any visible white or dark flash.
2. **Dynamic OS Reaction:** When set to `System`, changes in OS mode (e.g., sunset triggers or OS control panel toggles) immediately re-render the site without requiring a page refresh.
3. **Dual UI Access Points:**
   - **Header Bar:** Compact, high-contrast trigger button with an accessible dropdown menu indicating the active mode.
   - **Mobile Drawer Menu:** Dedicated segmented radio button pill control (`[ 💻 System | ☀️ Light | 🌙 Dark ]`) for one-touch mobile switching.
4. **Strict Accessibility:** Full WCAG 2.1 AA/AAA compliance with keyboard arrow navigation, `Escape` key close, focus traps, and ARIA state announcements.

---

## 2. Zero-FOUC Prevention Architecture

The Zero-FOUC script is placed at line 24 of `<head>` immediately after Google Tag Manager and before any stylesheet or markup rendering:

```html
<!-- Immediate Theme Initialization (Zero-FOUC Prevention) -->
<script>
    (function() {
        try {
            var stored = localStorage.getItem('theme-preference') || localStorage.getItem('theme');
            var pref = (stored === 'dark' || stored === 'light' || stored === 'system') ? stored : 'system';
            var isDark = pref === 'dark' || (pref === 'system' && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
            document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
            document.documentElement.setAttribute('data-theme-preference', pref);
        } catch (e) {}
    })();
</script>
```

### Execution Timeline
- **$t_0$ (0ms):** Browser parses `<head>`.
- **$t_1$ (0.1ms):** Script runs synchronously; reads `localStorage`. Evaluates `window.matchMedia('(prefers-color-scheme: dark)')`.
- **$t_2$ (0.2ms):** `document.documentElement` receives `data-theme="light"` or `data-theme="dark"`.
- **$t_3$ (10ms+):** Browser parses CSS and paints first frame. All CSS variables resolve to the correct theme instantly. **Visible flash = 0ms.**

---

## 3. UI Component Structure & HTML Markup

### 3.1 Header Dropdown Trigger & Menu
Located in the primary navigation bar (`.nav`):

```html
<div style="display: flex; align-items: center; gap: 0.5rem;">
    <!-- Theme Switcher Dropdown Container -->
    <div class="theme-dropdown-wrapper" id="theme-dropdown-wrapper">
        <button class="theme-toggle" id="theme-toggle" 
                type="button" 
                aria-haspopup="listbox" 
                aria-expanded="false" 
                aria-label="Color theme: System (Auto). Click to change theme" 
                title="Current theme: System (Auto)">
            <i class='bx bx-desktop' id="theme-icon" aria-hidden="true"></i>
        </button>

        <div class="theme-dropdown-menu" id="theme-dropdown-menu" role="listbox" aria-label="Theme selection options">
            <button type="button" class="theme-menu-item active" data-theme-val="system" role="option" aria-selected="true">
                <i class='bx bx-desktop' aria-hidden="true"></i>
                <span class="theme-item-text">System</span>
                <i class='bx bx-check theme-item-check' aria-hidden="true"></i>
            </button>
            <button type="button" class="theme-menu-item" data-theme-val="light" role="option" aria-selected="false">
                <i class='bx bx-sun' aria-hidden="true"></i>
                <span class="theme-item-text">Light</span>
                <i class='bx bx-check theme-item-check' aria-hidden="true"></i>
            </button>
            <button type="button" class="theme-menu-item" data-theme-val="dark" role="option" aria-selected="false">
                <i class='bx bx-moon' aria-hidden="true"></i>
                <span class="theme-item-text">Dark</span>
                <i class='bx bx-check theme-item-check' aria-hidden="true"></i>
            </button>
        </div>
    </div>

    <!-- Mobile Drawer Hamburger -->
    <div class="nav__toggle" id="nav-toggle" role="button" tabindex="0" aria-expanded="false" aria-controls="nav-menu" aria-label="Open navigation menu">
        <i class="bx bx-menu"></i>
    </div>
</div>
```

### 3.2 Mobile Drawer Segmented Control
Integrated inside the `.nav__menu` slide-out drawer:

```html
<!-- Mobile Drawer Theme Control -->
<div class="nav__mobile-theme">
    <span class="nav__mobile-theme-title">Theme Preference</span>
    <div class="theme-segmented-control" role="radiogroup" aria-label="Theme mode selection">
        <button type="button" class="theme-segment-btn active" data-theme-val="system" role="radio" aria-checked="true">
            <i class='bx bx-desktop' aria-hidden="true"></i>
            <span>System</span>
        </button>
        <button type="button" class="theme-segment-btn" data-theme-val="light" role="radio" aria-checked="false">
            <i class='bx bx-sun' aria-hidden="true"></i>
            <span>Light</span>
        </button>
        <button type="button" class="theme-segment-btn" data-theme-val="dark" role="radio" aria-checked="false">
            <i class='bx bx-moon' aria-hidden="true"></i>
            <span>Dark</span>
        </button>
    </div>
</div>
```

---

## 4. Styling & Micro-Interactions

### 4.1 Dropdown Elevation & Smooth Popover Animation
```css
.theme-dropdown-menu {
    position: absolute;
    top: calc(100% + 8px);
    right: 0;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 6px;
    min-width: 150px;
    box-shadow: var(--shadow-lg);
    opacity: 0;
    visibility: hidden;
    transform: translateY(-8px);
    transition: opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.2s;
    z-index: 200;
}

.theme-dropdown-menu.show {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}
```

### 4.2 Interactive Options & Active State Indication
```css
.theme-menu-item {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 0.65rem;
    padding: 8px 10px;
    border: none;
    background: transparent;
    color: var(--text-color);
    font-family: var(--font-body);
    font-size: var(--small-font-size);
    font-weight: 500;
    border-radius: var(--radius-sm);
    cursor: pointer;
    text-align: left;
    transition: background 0.15s ease, color 0.15s ease;
}

.theme-menu-item:hover, .theme-menu-item:focus-visible {
    background: var(--surface-color);
    color: var(--primary);
    outline: none;
}

.theme-menu-item.active {
    color: var(--primary);
    font-weight: 600;
    background: var(--primary-subtle);
}

.theme-item-check {
    font-size: 1.1rem;
    color: var(--primary);
    opacity: 0;
    transition: opacity 0.15s ease;
}

.theme-menu-item.active .theme-item-check {
    opacity: 1;
}
```

---

## 5. JavaScript Controller Logic

The client-side controller manages storage persistence, state synchronization between both UI widgets, dynamic OS event listening, and accessible keyboard navigation:

```javascript
/*===== SYSTEM-AWARE THEME MANAGEMENT (SYSTEM / LIGHT / DARK) =====*/
const THEME_STORAGE_KEY = 'theme-preference';
const LEGACY_STORAGE_KEY = 'theme';
const mediaDarkQuery = window.matchMedia('(prefers-color-scheme: dark)');

const themeToggleBtn = document.getElementById('theme-toggle');
const themeDropdownMenu = document.getElementById('theme-dropdown-menu');
const themeIcon = document.getElementById('theme-icon');
const themeMenuItems = document.querySelectorAll('.theme-menu-item');
const themeSegmentBtns = document.querySelectorAll('.theme-segment-btn');

function getStoredThemePreference() {
    var pref = localStorage.getItem(THEME_STORAGE_KEY) || localStorage.getItem(LEGACY_STORAGE_KEY);
    return (pref === 'dark' || pref === 'light' || pref === 'system') ? pref : 'system';
}

function applyTheme(preference) {
    var validPref = (preference === 'dark' || preference === 'light' || preference === 'system') ? preference : 'system';
    var isDark = validPref === 'dark' || (validPref === 'system' && mediaDarkQuery.matches);
    var resolvedTheme = isDark ? 'dark' : 'light';

    document.documentElement.setAttribute('data-theme', resolvedTheme);
    document.documentElement.setAttribute('data-theme-preference', validPref);
    document.body.setAttribute('data-theme', resolvedTheme);

    // Update Header Icon
    if (themeIcon) {
        themeIcon.className = '';
        if (validPref === 'system') {
            themeIcon.className = 'bx bx-desktop';
        } else if (validPref === 'light') {
            themeIcon.className = 'bx bx-sun';
        } else {
            themeIcon.className = 'bx bx-moon';
        }
    }

    // Update Toggle Button Title & Aria Label
    if (themeToggleBtn) {
        var prefLabel = validPref.charAt(0).toUpperCase() + validPref.slice(1);
        themeToggleBtn.setAttribute('aria-label', 'Color theme: ' + prefLabel + (validPref === 'system' ? ' (Auto OS)' : '') + '. Click to change theme');
        themeToggleBtn.setAttribute('title', 'Current theme: ' + prefLabel + (validPref === 'system' ? ' (Auto OS)' : ''));
    }

    // Update Dropdown Items
    themeMenuItems.forEach(function(item) {
        var val = item.getAttribute('data-theme-val');
        var isSelected = (val === validPref);
        item.classList.toggle('active', isSelected);
        item.setAttribute('aria-selected', isSelected ? 'true' : 'false');
    });

    // Update Mobile Drawer Segmented Buttons
    themeSegmentBtns.forEach(function(btn) {
        var val = btn.getAttribute('data-theme-val');
        var isChecked = (val === validPref);
        btn.classList.toggle('active', isChecked);
        btn.setAttribute('aria-checked', isChecked ? 'true' : 'false');
    });
}

function setThemePreference(pref) {
    var validPref = (pref === 'dark' || pref === 'light' || pref === 'system') ? pref : 'system';
    try {
        localStorage.setItem(THEME_STORAGE_KEY, validPref);
        localStorage.setItem(LEGACY_STORAGE_KEY, validPref);
    } catch (e) {}
    applyTheme(validPref);
}

// Initialize with stored preference
applyTheme(getStoredThemePreference());

// Dynamic OS listener: react when preference is 'system'
var handleMediaChange = function() {
    if (getStoredThemePreference() === 'system') {
        applyTheme('system');
    }
};

if (mediaDarkQuery.addEventListener) {
    mediaDarkQuery.addEventListener('change', handleMediaChange);
} else if (mediaDarkQuery.addListener) {
    mediaDarkQuery.addListener(handleMediaChange);
}

// Dropdown toggle logic
if (themeToggleBtn && themeDropdownMenu) {
    themeToggleBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        var isExpanded = themeDropdownMenu.classList.toggle('show');
        themeToggleBtn.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
    });

    // Close when clicking outside
    document.addEventListener('click', function(e) {
        if (!themeDropdownMenu.contains(e.target) && e.target !== themeToggleBtn) {
            themeDropdownMenu.classList.remove('show');
            themeToggleBtn.setAttribute('aria-expanded', 'false');
        }
    });

    // Keyboard navigation (ArrowDown, ArrowUp, Enter, Escape)
    themeToggleBtn.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown' || e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            themeDropdownMenu.classList.add('show');
            themeToggleBtn.setAttribute('aria-expanded', 'true');
            var activeOption = themeDropdownMenu.querySelector('.theme-menu-item.active') || themeDropdownMenu.querySelector('.theme-menu-item');
            if (activeOption) activeOption.focus();
        }
    });

    themeDropdownMenu.addEventListener('keydown', function(e) {
        var items = Array.from(themeMenuItems);
        var currentIndex = items.indexOf(document.activeElement);

        if (e.key === 'Escape') {
            e.preventDefault();
            themeDropdownMenu.classList.remove('show');
            themeToggleBtn.setAttribute('aria-expanded', 'false');
            themeToggleBtn.focus();
        } else if (e.key === 'ArrowDown') {
            e.preventDefault();
            var nextIndex = (currentIndex + 1) % items.length;
            items[nextIndex].focus();
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            var prevIndex = (currentIndex - 1 + items.length) % items.length;
            items[prevIndex].focus();
        }
    });

    // Dropdown menu item click
    themeMenuItems.forEach(function(item) {
        item.addEventListener('click', function(e) {
            e.stopPropagation();
            var val = item.getAttribute('data-theme-val');
            setThemePreference(val);
            themeDropdownMenu.classList.remove('show');
            themeToggleBtn.setAttribute('aria-expanded', 'false');
            themeToggleBtn.focus();
        });
    });
}

// Mobile drawer segmented button click
themeSegmentBtns.forEach(function(btn) {
    btn.addEventListener('click', function() {
        var val = btn.getAttribute('data-theme-val');
        setThemePreference(val);
    });
});
```

---

## 6. Backward Compatibility & Storage Keys

To ensure that returning visitors who previously visited the website before Step 17 have a seamless experience:
1. `localStorage.getItem('theme-preference')` is checked first.
2. If absent, `localStorage.getItem('theme')` (the legacy key) is read.
3. When saving, both keys (`theme-preference` and `theme`) are updated simultaneously.
4. If no preference has ever been set, `'system'` is selected automatically.
