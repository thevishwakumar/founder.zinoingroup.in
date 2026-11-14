import re

def update_dropdown():
    html_path = 'founder.zinoingroup.in/index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New HTML for nav__list
    new_nav_list = """                <ul class="nav__list">
                    <li class="nav__item">
                        <a href="#home" class="nav__link active">Home</a>
                    </li>

                    <!-- Dropdown 1: About & Presence -->
                    <li class="nav__item nav__dropdown" id="nav-dropdown-about">
                        <button class="nav__link nav__dropdown-trigger" type="button" aria-haspopup="true" aria-expanded="false" aria-controls="dropdown-menu-about">
                            <span>About</span>
                            <i class='bx bx-chevron-down nav__dropdown-icon' aria-hidden="true"></i>
                        </button>
                        <div class="nav__dropdown-menu" id="dropdown-menu-about" role="menu" aria-label="About Submenu">
                            <a href="#about" class="nav__dropdown-item" role="menuitem">
                                <div class="nav__dropdown-item-icon">
                                    <i class='bx bx-user' aria-hidden="true"></i>
                                </div>
                                <div class="nav__dropdown-item-content">
                                    <span class="nav__dropdown-item-title">About Vishwa</span>
                                    <span class="nav__dropdown-item-desc">Founder background & executive vision</span>
                                </div>
                            </a>
                            <a href="#gallery" class="nav__dropdown-item" role="menuitem">
                                <div class="nav__dropdown-item-icon">
                                    <i class='bx bx-images' aria-hidden="true"></i>
                                </div>
                                <div class="nav__dropdown-item-content">
                                    <span class="nav__dropdown-item-title">Executive Presence</span>
                                    <span class="nav__dropdown-item-desc">Portraits, leadership & keynotes</span>
                                </div>
                            </a>
                        </div>
                    </li>

                    <li class="nav__item">
                        <a href="#expertise" class="nav__link">Expertise</a>
                    </li>

                    <li class="nav__item">
                        <a href="#projects" class="nav__link">Projects</a>
                    </li>

                    <!-- Dropdown 2: Credentials (Experience, Education, Certifications) -->
                    <li class="nav__item nav__dropdown" id="nav-dropdown-credentials">
                        <button class="nav__link nav__dropdown-trigger" type="button" aria-haspopup="true" aria-expanded="false" aria-controls="dropdown-menu-credentials">
                            <span>Credentials</span>
                            <i class='bx bx-chevron-down nav__dropdown-icon' aria-hidden="true"></i>
                        </button>
                        <div class="nav__dropdown-menu" id="dropdown-menu-credentials" role="menu" aria-label="Credentials Submenu">
                            <a href="#experience" class="nav__dropdown-item" role="menuitem">
                                <div class="nav__dropdown-item-icon">
                                    <i class='bx bx-briefcase-alt' aria-hidden="true"></i>
                                </div>
                                <div class="nav__dropdown-item-content">
                                    <span class="nav__dropdown-item-title">Experience</span>
                                    <span class="nav__dropdown-item-desc">Founder & CEO milestones</span>
                                </div>
                            </a>
                            <a href="#education" class="nav__dropdown-item" role="menuitem">
                                <div class="nav__dropdown-item-icon">
                                    <i class='bx bx-book-open' aria-hidden="true"></i>
                                </div>
                                <div class="nav__dropdown-item-content">
                                    <span class="nav__dropdown-item-title">Education</span>
                                    <span class="nav__dropdown-item-desc">B.E Cyber Security & academics</span>
                                </div>
                            </a>
                            <a href="#certifications" class="nav__dropdown-item" role="menuitem">
                                <div class="nav__dropdown-item-icon">
                                    <i class='bx bx-award' aria-hidden="true"></i>
                                </div>
                                <div class="nav__dropdown-item-content">
                                    <span class="nav__dropdown-item-title">Certifications</span>
                                    <span class="nav__dropdown-item-desc">40 verified credentials</span>
                                </div>
                            </a>
                        </div>
                    </li>

                    <li class="nav__item">
                        <a href="#contact" class="nav__link">Contact</a>
                    </li>
                </ul>"""

    nav_list_pattern = r'<ul class="nav__list">[\s\S]*?</ul>'
    assert re.search(nav_list_pattern, html), "Could not find nav__list in index.html"
    html = re.sub(nav_list_pattern, new_nav_list.replace('\\', '\\\\'), html, count=1)
    print("Replaced nav__list with dropdown menu structure!")

    # 2. Add Dropdown CSS styles
    dropdown_css = """
        /*===== EXECUTIVE DROPDOWN MENU STYLES =====*/
        .nav__dropdown {
            position: relative;
        }

        .nav__dropdown-trigger {
            background: none;
            border: none;
            cursor: pointer;
            font-family: inherit;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            color: var(--text-muted);
            font-weight: 500;
            font-size: var(--small-font-size);
            padding: 0.25rem 0;
            transition: color 0.2s var(--ease-standard);
        }

        .nav__dropdown-trigger:hover,
        .nav__dropdown-trigger.active,
        .nav__dropdown:hover .nav__dropdown-trigger {
            color: var(--primary);
        }

        .nav__dropdown-icon {
            font-size: 1.15rem;
            transition: transform 0.25s var(--ease-out-expo), color 0.2s ease;
        }

        /* Desktop Dropdown Styles */
        @media screen and (min-width: 992px) {
            .nav__dropdown:hover .nav__dropdown-icon,
            .nav__dropdown.show .nav__dropdown-icon {
                transform: rotate(180deg);
                color: var(--primary);
            }

            .nav__dropdown-menu {
                position: absolute;
                top: calc(100% + 14px);
                left: 50%;
                transform: translateX(-50%) translateY(-6px) scale(0.97);
                min-width: 290px;
                background: var(--card-bg);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-md);
                padding: 0.65rem;
                box-shadow: 0 16px 36px -8px rgba(15, 23, 42, 0.18), 0 0 0 1px var(--border-subtle);
                opacity: 0;
                visibility: hidden;
                pointer-events: none;
                transition: opacity 0.22s var(--ease-out-expo),
                            transform 0.25s var(--ease-out-expo),
                            visibility 0.22s;
                z-index: 250;
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
            }

            /* Invisible hover bridge */
            .nav__dropdown::after {
                content: "";
                position: absolute;
                top: 100%;
                left: 0;
                width: 100%;
                height: 16px;
            }

            .nav__dropdown:hover .nav__dropdown-menu,
            .nav__dropdown:focus-within .nav__dropdown-menu,
            .nav__dropdown.show .nav__dropdown-menu {
                opacity: 1;
                visibility: visible;
                pointer-events: auto;
                transform: translateX(-50%) translateY(0) scale(1);
            }

            .nav__dropdown-item {
                display: flex;
                align-items: center;
                gap: 0.85rem;
                padding: 0.65rem 0.85rem;
                border-radius: var(--radius-sm);
                transition: background 0.18s ease, transform 0.18s var(--ease-out-expo), border-color 0.18s ease;
                color: var(--text-color);
                text-decoration: none;
                border: 1px solid transparent;
            }

            .nav__dropdown-item:hover,
            .nav__dropdown-item:focus-visible,
            .nav__dropdown-item.active {
                background: var(--surface-color);
                border-color: var(--border-subtle);
                transform: translateX(3px);
            }

            .nav__dropdown-item.active .nav__dropdown-item-title {
                color: var(--primary);
            }

            .nav__dropdown-item-icon {
                width: 38px;
                height: 38px;
                border-radius: var(--radius-sm);
                background: var(--primary-subtle);
                color: var(--primary);
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 1.25rem;
                flex-shrink: 0;
                border: 1px solid var(--primary-border);
                transition: background 0.18s ease, color 0.18s ease, transform 0.18s var(--ease-out-expo);
            }

            .nav__dropdown-item:hover .nav__dropdown-item-icon {
                background: var(--primary);
                color: #ffffff;
                transform: scale(1.05);
            }

            .nav__dropdown-item-content {
                display: flex;
                flex-direction: column;
                gap: 0.15rem;
            }

            .nav__dropdown-item-title {
                font-size: var(--small-font-size);
                font-weight: 600;
                color: var(--text-color);
            }

            .nav__dropdown-item-desc {
                font-size: var(--smaller-font-size);
                color: var(--text-muted);
                line-height: 1.35;
            }
        }

        /* Mobile Drawer Dropdown Styles */
        @media screen and (max-width: 991px) {
            .nav__dropdown-trigger {
                width: 100%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                font-size: 1.05rem;
                font-weight: 600;
                color: var(--text-color);
                padding: 0.5rem 0;
                min-height: 44px;
            }

            .nav__dropdown-icon {
                font-size: 1.35rem;
                color: var(--text-muted);
                transition: transform 0.25s var(--ease-out-expo);
            }

            .nav__dropdown.open .nav__dropdown-icon {
                transform: rotate(180deg);
                color: var(--primary);
            }

            .nav__dropdown-menu {
                display: none;
                padding-left: 0.85rem;
                margin-top: 0.35rem;
                margin-bottom: 0.65rem;
                border-left: 2px solid var(--primary-border);
            }

            .nav__dropdown.open .nav__dropdown-menu {
                display: flex;
                flex-direction: column;
                gap: 0.35rem;
                animation: mobileSubmenuOpen 0.25s var(--ease-out-expo);
            }

            @keyframes mobileSubmenuOpen {
                from {
                    opacity: 0;
                    transform: translateY(-6px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            .nav__dropdown-item {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                padding: 0.55rem 0.65rem;
                border-radius: var(--radius-sm);
                color: var(--text-color);
                text-decoration: none;
                min-height: 44px;
                transition: background 0.15s ease, color 0.15s ease;
            }

            .nav__dropdown-item:hover,
            .nav__dropdown-item:active,
            .nav__dropdown-item.active {
                background: var(--surface-color);
                color: var(--primary);
            }

            .nav__dropdown-item-icon {
                font-size: 1.25rem;
                color: var(--primary);
                width: 28px;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .nav__dropdown-item-title {
                font-size: var(--small-font-size);
                font-weight: 600;
            }

            .nav__dropdown-item-desc {
                display: none;
            }
        }
"""
    if '.nav__dropdown' not in html:
        target_css = "/*===== THEME SWITCHER COMPONENT =====*/"
        assert target_css in html
        html = html.replace(target_css, dropdown_css + "\n        " + target_css, 1)
        print("Added dropdown CSS rules to index.html!")

    # 3. Add Dropdown JS behavior & update scrollActive
    dropdown_js = """
        /*===== DROPDOWN SUBMENU LOGIC (DESKTOP & MOBILE ACCORDION) =====*/
        const navDropdowns = document.querySelectorAll('.nav__dropdown');

        navDropdowns.forEach(dropdown => {
            const trigger = dropdown.querySelector('.nav__dropdown-trigger');
            const menu = dropdown.querySelector('.nav__dropdown-menu');

            if (!trigger || !menu) return;

            // Mobile accordion toggle
            trigger.addEventListener('click', function(e) {
                if (window.innerWidth < 992) {
                    e.preventDefault();
                    const isOpen = dropdown.classList.toggle('open');
                    trigger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
                }
            });

            // Keyboard accessibility
            trigger.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowDown') {
                    e.preventDefault();
                    dropdown.classList.add('show');
                    trigger.setAttribute('aria-expanded', 'true');
                    const firstItem = menu.querySelector('a');
                    if (firstItem) firstItem.focus();
                } else if (e.key === 'Escape') {
                    dropdown.classList.remove('show');
                    trigger.setAttribute('aria-expanded', 'false');
                }
            });

            dropdown.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    dropdown.classList.remove('show');
                    trigger.setAttribute('aria-expanded', 'false');
                    trigger.focus();
                }
            });
        });

        // Close dropdown when clicking outside on desktop
        document.addEventListener('click', function(e) {
            navDropdowns.forEach(dropdown => {
                if (!dropdown.contains(e.target)) {
                    dropdown.classList.remove('show');
                    dropdown.querySelector('.nav__dropdown-trigger')?.setAttribute('aria-expanded', 'false');
                }
            });
        });

        // Auto-close mobile drawer when any link is clicked
        const navClickLinks = document.querySelectorAll('.nav__link:not(.nav__dropdown-trigger), .nav__dropdown-item');
        navClickLinks.forEach(link => {
            link.addEventListener('click', () => {
                const navMenu = document.getElementById('nav-menu');
                if (navMenu) {
                    navMenu.classList.remove('show');
                    const navToggle = document.getElementById('nav-toggle');
                    if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
                }
            });
        });
"""

    if '/*===== DROPDOWN SUBMENU LOGIC' not in html:
        target_js = "/*===== SCROLL SECTIONS ACTIVE LINK (THROTTLED VIA REQUESTANIMATIONFRAME) =====*/"
        assert target_js in html
        html = html.replace(target_js, dropdown_js + "\n        " + target_js, 1)
        print("Added dropdown JavaScript handlers!")

    # 4. Update scrollActive to illuminate dropdown triggers when child sections are in view
    target_scroll_fn = """        function scrollActive() {
            const scrollY = window.pageYOffset;

            sections.forEach(current => {
                const sectionHeight = current.offsetHeight;
                const sectionTop = current.offsetTop - 100;
                const sectionId = current.getAttribute('id');
                const navAnchor = document.querySelector('.nav__menu a[href*=' + sectionId + ']');

                if (navAnchor) {
                    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                        navAnchor.classList.add('active');
                    } else {
                        navAnchor.classList.remove('active');
                    }
                }
            });
        }"""

    replacement_scroll_fn = """        function scrollActive() {
            const scrollY = window.pageYOffset;

            sections.forEach(current => {
                const sectionHeight = current.offsetHeight;
                const sectionTop = current.offsetTop - 120;
                const sectionId = current.getAttribute('id');
                const navAnchors = document.querySelectorAll('.nav__menu a[href*=' + sectionId + ']');

                navAnchors.forEach(navAnchor => {
                    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                        navAnchor.classList.add('active');
                        // Parent dropdown activation
                        const parentDropdown = navAnchor.closest('.nav__dropdown');
                        if (parentDropdown) {
                            parentDropdown.querySelector('.nav__dropdown-trigger')?.classList.add('active');
                        }
                    } else {
                        navAnchor.classList.remove('active');
                        const parentDropdown = navAnchor.closest('.nav__dropdown');
                        if (parentDropdown) {
                            const hasActiveChild = parentDropdown.querySelector('.nav__dropdown-menu a.active');
                            if (!hasActiveChild) {
                                parentDropdown.querySelector('.nav__dropdown-trigger')?.classList.remove('active');
                            }
                        }
                    }
                });
            });
        }"""

    if target_scroll_fn in html:
        html = html.replace(target_scroll_fn, replacement_scroll_fn, 1)
        print("Updated scrollActive function for dropdown support!")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with dropdown menu navigation!")

if __name__ == '__main__':
    update_dropdown()

