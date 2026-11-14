import re

def apply_animations():
    # 1. Update index.html
    html_path = 'founder.zinoingroup.in/index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # A. Add --ease-smooth and --duration-reveal to :root if not present
    if '--duration-reveal:' not in html:
        target = "--ease-standard: cubic-bezier(0.4, 0, 0.2, 1);"
        replacement = "--ease-standard: cubic-bezier(0.4, 0, 0.2, 1);\n            --ease-smooth: cubic-bezier(0.2, 0.8, 0.2, 1);\n            --duration-reveal: 0.65s;"
        assert target in html, "Target for :root easing not found"
        html = html.replace(target, replacement, 1)

    # B. Add theme-transitioning styles
    theme_trans_css = """
        /* Smooth Theme Switch Cross-Fade */
        html.theme-transitioning,
        html.theme-transitioning *,
        html.theme-transitioning *::before,
        html.theme-transitioning *::after {
            transition: background-color 0.28s var(--ease-standard),
                        border-color 0.28s var(--ease-standard),
                        color 0.28s var(--ease-standard),
                        box-shadow 0.28s var(--ease-standard) !important;
        }
"""
    if 'html.theme-transitioning' not in html:
        target = "/* Fallback: when OS prefers dark and user has not set explicit light theme */"
        assert target in html
        html = html.replace(target, theme_trans_css + "        " + target, 1)

    # C. Section title hover underline expansion
    target_sect_title = """.section-title::after {
            content: "";
            position: absolute;
            width: 48px;
            height: 3.5px;
            left: 50%;
            transform: translateX(-50%);
            bottom: -10px;
            background: linear-gradient(90deg, var(--primary), var(--accent-cyan));
            border-radius: var(--radius-full);
        }"""
    replacement_sect_title = """.section-title::after {
            content: "";
            position: absolute;
            width: 48px;
            height: 3.5px;
            left: 50%;
            transform: translateX(-50%);
            bottom: -10px;
            background: linear-gradient(90deg, var(--primary), var(--accent-cyan));
            border-radius: var(--radius-full);
            transition: width 0.35s var(--ease-out-expo);
        }

        @media (hover: hover) and (pointer: fine) {
            .section-title:hover::after {
                width: 76px;
            }
        }"""
    if target_sect_title in html:
        html = html.replace(target_sect_title, replacement_sect_title, 1)

    # D. Nav links hover underline subtle hint
    target_nav_after = """.nav__link::after {
                content: "";
                position: absolute;
                bottom: -6px;
                left: 0;
                width: 100%;
                height: 2px;
                background-color: var(--primary);
                border-radius: var(--radius-full);
                transform: scaleX(0);
                transform-origin: center;
                transition: transform 0.25s var(--ease-out-expo), opacity 0.25s ease;
                opacity: 0;
            }

            .nav__link.active::after {
                transform: scaleX(1);
                opacity: 1;
            }"""
    replacement_nav_after = """.nav__link::after {
                content: "";
                position: absolute;
                bottom: -6px;
                left: 0;
                width: 100%;
                height: 2px;
                background-color: var(--primary);
                border-radius: var(--radius-full);
                transform: scaleX(0);
                transform-origin: center;
                transition: transform 0.25s var(--ease-out-expo), opacity 0.25s ease;
                opacity: 0;
            }

            @media (hover: hover) and (pointer: fine) {
                .nav__link:hover::after {
                    transform: scaleX(0.7);
                    opacity: 0.55;
                }
            }

            .nav__link.active::after {
                transform: scaleX(1);
                opacity: 1;
            }"""
    if target_nav_after in html:
        html = html.replace(target_nav_after, replacement_nav_after, 1)

    # E. Status badge shimmer & hover
    target_badge = """.home__badge {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            background: var(--primary-subtle);
            border: 1px solid var(--primary-border);
            color: var(--primary);
            padding: 0.4rem 1rem;
            border-radius: var(--radius-full);
            font-size: var(--small-font-size);
            font-weight: 600;
            margin-bottom: 1.5rem;
            animation: heroFadeUp 0.5s var(--ease-out-expo) 0.05s backwards;
        }"""
    replacement_badge = """.home__badge {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            background: var(--primary-subtle);
            border: 1px solid var(--primary-border);
            color: var(--primary);
            padding: 0.4rem 1rem;
            border-radius: var(--radius-full);
            font-size: var(--small-font-size);
            font-weight: 600;
            margin-bottom: 1.5rem;
            animation: heroFadeUp 0.5s var(--ease-out-expo) 0.05s backwards;
            position: relative;
            overflow: hidden;
            transition: border-color 0.25s ease, box-shadow 0.25s ease, transform 0.25s var(--ease-out-expo);
        }

        @media (hover: hover) and (pointer: fine) {
            .home__badge:hover {
                transform: translateY(-1px);
                border-color: var(--primary);
                box-shadow: 0 4px 14px rgba(37, 99, 235, 0.16);
            }
        }

        .home__badge::after {
            content: "";
            position: absolute;
            top: 0;
            left: -120%;
            width: 60%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.16), transparent);
            transform: skewX(-20deg);
            animation: badgeShimmer 6s infinite ease-in-out;
            pointer-events: none;
        }

        @keyframes badgeShimmer {
            0%, 75% { left: -120%; }
            100% { left: 220%; }
        }"""
    if target_badge in html:
        html = html.replace(target_badge, replacement_badge, 1)

    # F. About section aura breath keyframes
    target_about_aura = """.about__img-wrapper::before {
            content: "";
            position: absolute;
            inset: -10px;
            border-radius: var(--radius-lg);
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(99, 102, 241, 0.08));
            z-index: 0;
            filter: blur(6px);
        }"""
    replacement_about_aura = """.about__img-wrapper::before {
            content: "";
            position: absolute;
            inset: -10px;
            border-radius: var(--radius-lg);
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.24), rgba(99, 102, 241, 0.1));
            z-index: 0;
            filter: blur(8px);
            animation: auraBreath 6s ease-in-out infinite alternate;
        }

        @keyframes auraBreath {
            0% {
                opacity: 0.7;
                filter: blur(8px);
                transform: scale(0.98);
            }
            100% {
                opacity: 1;
                filter: blur(14px);
                transform: scale(1.02);
            }
        }"""
    if target_about_aura in html:
        html = html.replace(target_about_aura, replacement_about_aura, 1)

    # G. Gallery card hover & zoom
    target_gallery = """.gallery__card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: transform 0.25s var(--ease-out-expo), border-color 0.25s var(--ease-standard), box-shadow 0.25s var(--ease-standard);
            display: flex;
            flex-direction: column;
        }

        @media (hover: hover) and (pointer: fine) {
            .gallery__card:hover {
                transform: translateY(-4px);
                border-color: var(--primary);
                box-shadow: var(--shadow-lg);
            }
            .gallery__card:hover .gallery__img {
                transform: scale(1.03);
            }
        }"""
    replacement_gallery = """.gallery__card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            transition: transform 0.35s var(--ease-out-expo), border-color 0.25s var(--ease-standard), box-shadow 0.35s var(--ease-out-expo);
            display: flex;
            flex-direction: column;
            will-change: transform, box-shadow;
        }

        @media (hover: hover) and (pointer: fine) {
            .gallery__card:hover {
                transform: translateY(-6px);
                border-color: var(--primary-light);
                box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.22), 0 0 20px rgba(37, 99, 235, 0.16);
            }
            .gallery__card:hover .gallery__img {
                transform: scale(1.05);
            }
        }"""
    if target_gallery in html:
        html = html.replace(target_gallery, replacement_gallery, 1)

    # H. Project card & icon box hover & translation
    target_project_icon = """.project__icon-box {
            width: 52px;
            height: 52px;
            border-radius: var(--radius-md);
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.85rem;
            color: var(--primary);
            box-shadow: var(--shadow-sm);
            transition: transform 0.25s var(--ease-out-expo), color 0.25s ease, border-color 0.25s ease;
        }

        .project__card:hover .project__icon-box {
            transform: translateY(-2px) scale(1.05);
            color: var(--accent);
            border-color: var(--primary);
        }"""
    replacement_project_icon = """.project__icon-box {
            width: 52px;
            height: 52px;
            border-radius: var(--radius-md);
            background: var(--surface-color);
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.85rem;
            color: var(--primary);
            box-shadow: var(--shadow-sm);
            transition: transform 0.35s var(--ease-out-expo), box-shadow 0.35s var(--ease-out-expo), color 0.25s ease, border-color 0.25s ease, background 0.25s ease;
        }

        .project__card:hover .project__icon-box {
            transform: translateY(-3px) scale(1.08);
            color: var(--accent);
            border-color: var(--primary);
            box-shadow: 0 8px 18px rgba(37, 99, 235, 0.25);
        }

        .project__link i {
            transition: transform 0.25s var(--ease-out-expo);
        }

        .project__card:hover .project__link i {
            transform: translateX(3px);
        }"""
    if target_project_icon in html:
        html = html.replace(target_project_icon, replacement_project_icon, 1)

    # I. Clean up duplicate project card hover block from line 1720
    target_dup_hover = """        @media (hover: hover) and (pointer: fine) {
            .project__card:hover {
                transform: translateY(-5px);
                border-color: var(--primary);
                box-shadow: var(--shadow-lg);
            }

            .project__card:hover .project__img {
                transform: scale(1.03);
            }

            .button--small:hover i {
                transform: translateX(3px);
            }
        }"""
    replacement_dup_hover = """        @media (hover: hover) and (pointer: fine) {
            .project__card:hover {
                transform: translateY(-6px);
                border-color: var(--primary-light);
                box-shadow: 0 16px 36px -10px rgba(37, 99, 235, 0.18), var(--shadow-md);
            }

            .button--small:hover i {
                transform: translateX(3px);
            }
        }"""
    if target_dup_hover in html:
        html = html.replace(target_dup_hover, replacement_dup_hover, 1)

    # J. Expertise card hover
    target_exp_hover = """.expertise__card:hover {
            transform: translateY(-4px);
            border-color: var(--primary);
            box-shadow: var(--shadow-md);
        }

        .expertise__icon {
            width: 48px;
            height: 48px;
            border-radius: var(--radius-md);
            background: var(--primary-subtle);
            color: var(--primary);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1.25rem;
            transition: var(--transition);
            border: 1px solid var(--primary-border);
        }

        .expertise__card:hover .expertise__icon {
            background: var(--primary);
            color: #ffffff;
        }"""
    replacement_exp_hover = """.expertise__card {
            transition: transform 0.35s var(--ease-out-expo), border-color 0.25s var(--ease-standard), box-shadow 0.35s var(--ease-out-expo);
            will-change: transform, box-shadow;
        }

        .expertise__card:hover {
            transform: translateY(-5px);
            border-color: var(--primary-light);
            box-shadow: 0 16px 32px -8px rgba(37, 99, 235, 0.16), var(--shadow-md);
        }

        .expertise__icon {
            width: 48px;
            height: 48px;
            border-radius: var(--radius-md);
            background: var(--primary-subtle);
            color: var(--primary);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1.25rem;
            transition: transform 0.35s var(--ease-out-expo), background 0.25s ease, color 0.25s ease;
            border: 1px solid var(--primary-border);
        }

        .expertise__card:hover .expertise__icon {
            background: var(--primary);
            color: #ffffff;
            transform: scale(1.08) rotate(3deg);
        }"""
    if target_exp_hover in html:
        html = html.replace(target_exp_hover, replacement_exp_hover, 1)

    # K. Certificate card hover
    target_cert = """.certificate__card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            transition: var(--transition);
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
        }"""
    replacement_cert = """.certificate__card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            transition: transform 0.35s var(--ease-out-expo), border-color 0.25s var(--ease-standard), box-shadow 0.35s var(--ease-out-expo);
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
            will-change: transform, box-shadow;
        }

        @media (hover: hover) and (pointer: fine) {
            .certificate__card:hover {
                transform: translateY(-4px);
                border-color: var(--primary-light);
                box-shadow: 0 14px 28px -6px rgba(37, 99, 235, 0.14), var(--shadow-md);
            }
            .certificate__card:hover .certificate__icon {
                transform: scale(1.1);
            }
        }

        .certificate__icon {
            font-size: 1.75rem;
            color: var(--primary);
            line-height: 1;
            transition: transform 0.3s var(--ease-out-expo);
        }"""
    if target_cert in html:
        html = html.replace(target_cert, replacement_cert, 1)

    # L. Experience active dot & card hover
    target_dot = """.experience__dot {
            position: absolute;
            left: -2rem;
            top: 22px;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: var(--card-bg);
            border: 3px solid var(--primary);
            box-shadow: 0 0 0 4px var(--primary-subtle);
            z-index: 2;
            transition: var(--transition);
        }

        .experience__item:hover .experience__dot {
            background: var(--primary);
            box-shadow: 0 0 0 6px var(--primary-subtle);
            transform: scale(1.15);
        }"""
    replacement_dot = """.experience__dot {
            position: absolute;
            left: -2rem;
            top: 22px;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: var(--card-bg);
            border: 3px solid var(--primary);
            box-shadow: 0 0 0 4px var(--primary-subtle);
            z-index: 2;
            transition: transform 0.3s var(--ease-out-expo), background 0.25s ease, box-shadow 0.3s ease;
        }

        .experience__dot--active {
            background: var(--primary);
            box-shadow: 0 0 0 4px var(--primary-subtle), 0 0 12px rgba(37, 99, 235, 0.5);
            animation: dotGlow 2.5s infinite ease-in-out;
        }

        @keyframes dotGlow {
            0%, 100% {
                box-shadow: 0 0 0 4px var(--primary-subtle), 0 0 8px rgba(37, 99, 235, 0.4);
            }
            50% {
                box-shadow: 0 0 0 7px var(--primary-subtle), 0 0 16px rgba(37, 99, 235, 0.7);
            }
        }

        .experience__item:hover .experience__dot {
            background: var(--primary);
            box-shadow: 0 0 0 6px var(--primary-subtle);
            transform: scale(1.2);
        }"""
    if target_dot in html:
        html = html.replace(target_dot, replacement_dot, 1)

    # M. Scroll reveal and cascading stagger delays
    target_scroll_reveal = """        /*===== SCROLL REVEAL ANIMATIONS (PROGRESSIVE ENHANCEMENT) =====*/
        /* Default state: fully visible if JavaScript is disabled or fails */
        .scroll-animate {
            opacity: 1;
            transform: none;
        }

        /* Armed state: active only when IntersectionObserver is initialized */
        .has-scroll-observer .scroll-animate {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.55s var(--ease-out-expo), transform 0.55s var(--ease-out-expo);
            will-change: opacity, transform;
        }

        .has-scroll-observer .scroll-animate.show {
            opacity: 1;
            transform: translateY(0);
        }

        /* Respect Reduced Motion (WCAG 2.2 Level AAA) */
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
            .home__badge, .home__name, .home__headline, .home__description, .home__actions, .home__social {
                animation: none !important;
                opacity: 1 !important;
                transform: none !important;
            }
        }"""
    replacement_scroll_reveal = """        /*===== SCROLL REVEAL ANIMATIONS (PROGRESSIVE ENHANCEMENT) =====*/
        /* Default state: fully visible if JavaScript is disabled or fails */
        .scroll-animate {
            opacity: 1;
            transform: none;
        }

        /* Armed state: active only when IntersectionObserver is initialized */
        .has-scroll-observer .scroll-animate {
            opacity: 0;
            transform: translateY(24px);
            transition: opacity var(--duration-reveal) var(--ease-out-expo),
                        transform var(--duration-reveal) var(--ease-out-expo);
            will-change: opacity, transform;
        }

        .has-scroll-observer .scroll-animate.show {
            opacity: 1;
            transform: translateY(0);
        }

        /* Cascading Micro-stagger Transitions for Grid Elements */
        .gallery__container > .scroll-animate:nth-child(1) { transition-delay: 0.04s; }
        .gallery__container > .scroll-animate:nth-child(2) { transition-delay: 0.10s; }
        .gallery__container > .scroll-animate:nth-child(3) { transition-delay: 0.16s; }
        .gallery__container > .scroll-animate:nth-child(4) { transition-delay: 0.22s; }
        .gallery__container > .scroll-animate:nth-child(5) { transition-delay: 0.28s; }

        .expertise__grid > .scroll-animate:nth-child(1) { transition-delay: 0.04s; }
        .expertise__grid > .scroll-animate:nth-child(2) { transition-delay: 0.10s; }
        .expertise__grid > .scroll-animate:nth-child(3) { transition-delay: 0.16s; }
        .expertise__grid > .scroll-animate:nth-child(4) { transition-delay: 0.22s; }

        .projects__grid > .scroll-animate:nth-child(3n+1) { transition-delay: 0.04s; }
        .projects__grid > .scroll-animate:nth-child(3n+2) { transition-delay: 0.10s; }
        .projects__grid > .scroll-animate:nth-child(3n) { transition-delay: 0.16s; }

        .certifications__grid > .scroll-animate:nth-child(3n+1) { transition-delay: 0.04s; }
        .certifications__grid > .scroll-animate:nth-child(3n+2) { transition-delay: 0.08s; }
        .certifications__grid > .scroll-animate:nth-child(3n) { transition-delay: 0.12s; }

        .experience__timeline > .scroll-animate:nth-child(1) { transition-delay: 0.05s; }
        .experience__timeline > .scroll-animate:nth-child(2) { transition-delay: 0.12s; }
        .experience__timeline > .scroll-animate:nth-child(3) { transition-delay: 0.19s; }

        .education__container > .scroll-animate:nth-child(1) { transition-delay: 0.05s; }
        .education__container > .scroll-animate:nth-child(2) { transition-delay: 0.12s; }

        /* Respect Reduced Motion (WCAG 2.2 Level AAA) */
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
                transition-delay: 0s !important;
            }
            .home__badge, .home__name, .home__headline, .home__description, .home__actions, .home__social {
                animation: none !important;
                opacity: 1 !important;
                transform: none !important;
            }
            .about__img-wrapper::before,
            .home__badge::after,
            .experience__dot--active,
            .pulse-dot {
                animation: none !important;
            }
        }"""
    if target_scroll_reveal in html:
        html = html.replace(target_scroll_reveal, replacement_scroll_reveal, 1)

    # N. JavaScript: Smooth theme preference transition
    target_theme_func = """        function setThemePreference(pref) {
            var validPref = (pref === 'dark' || pref === 'light' || pref === 'system') ? pref : 'system';
            try {
                localStorage.setItem(THEME_STORAGE_KEY, validPref);
                localStorage.setItem(LEGACY_STORAGE_KEY, validPref);
            } catch (e) {}
            applyTheme(validPref);
        }"""
    replacement_theme_func = """        function setThemePreference(pref) {
            var validPref = (pref === 'dark' || pref === 'light' || pref === 'system') ? pref : 'system';
            try {
                localStorage.setItem(THEME_STORAGE_KEY, validPref);
                localStorage.setItem(LEGACY_STORAGE_KEY, validPref);
            } catch (e) {}
            if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
                document.documentElement.classList.add('theme-transitioning');
                window.clearTimeout(window.__themeTransitionTimeout);
                window.__themeTransitionTimeout = window.setTimeout(function() {
                    document.documentElement.classList.remove('theme-transitioning');
                }, 320);
            }
            applyTheme(validPref);
        }"""
    if target_theme_func in html:
        html = html.replace(target_theme_func, replacement_theme_func, 1)

    # O. Update static HTML fallback for first experience dot to have experience__dot--active
    target_static_dot = '<div class="experience__dot" aria-hidden="true"></div>\n                        <div class="experience__card">'
    replacement_static_dot = '<div class="experience__dot experience__dot--active" aria-hidden="true"></div>\n                        <div class="experience__card">'
    if target_static_dot in html:
        html = html.replace(target_static_dot, replacement_static_dot, 1)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html successfully updated with smooth professional animations!")

    # 2. Update content-renderer.js for dynamic experience dot
    renderer_path = 'founder.zinoingroup.in/assets/js/content-renderer.js'
    with open(renderer_path, 'r', encoding='utf-8') as f:
        js = f.read()

    target_js_dot = """                const item = el('div', { className: 'experience__item scroll-animate' },
                    el('div', { className: 'experience__dot', 'aria-hidden': 'true' }),
                    card
                );"""
    replacement_js_dot = """                const dotClass = (index === 0) ? 'experience__dot experience__dot--active' : 'experience__dot';
                const item = el('div', { className: 'experience__item scroll-animate' },
                    el('div', { className: dotClass, 'aria-hidden': 'true' }),
                    card
                );"""
    # Check if data.experiences.forEach has index
    if 'data.experiences.forEach(exp => {' in js:
        js = js.replace('data.experiences.forEach(exp => {', 'data.experiences.forEach((exp, index) => {', 1)
    if target_js_dot in js:
        js = js.replace(target_js_dot, replacement_js_dot, 1)

    with open(renderer_path, 'w', encoding='utf-8') as f:
        f.write(js)
    print("content-renderer.js successfully updated with dynamic experience active dot!")

if __name__ == '__main__':
    apply_animations()

