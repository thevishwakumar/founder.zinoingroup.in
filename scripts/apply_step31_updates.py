import re

with open("founder.zinoingroup.in/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS for project icon wrapper & gallery
project_css_old = """.project__card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            overflow: hidden;
            transition: border-color 0.25s var(--ease-standard), box-shadow 0.25s var(--ease-standard), transform 0.25s var(--ease-out-expo);
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            height: 100%;
        }"""

project_css_new = """.project__card {
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            overflow: hidden;
            transition: border-color 0.25s var(--ease-standard), box-shadow 0.25s var(--ease-standard), transform 0.25s var(--ease-out-expo);
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .project__icon-wrapper {
            position: relative;
            width: 100%;
            padding: 1.75rem 1.5rem 1rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.08) 0%, rgba(14, 165, 233, 0.03) 100%);
            border-bottom: 1px solid var(--border-color);
        }

        .project__icon-box {
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
        }

        .project__badge-pill {
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            color: #ffffff;
            font-size: var(--smaller-font-size);
            font-weight: 700;
            padding: 4px 10px;
            border-radius: var(--radius-full);
            letter-spacing: 0.05em;
        }

        /*===== GALLERY SECTION =====*/
        .gallery__container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        .gallery__card {
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
        }

        .gallery__img-box {
            position: relative;
            width: 100%;
            height: 340px;
            overflow: hidden;
            background: var(--surface-color);
        }

        .gallery__img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: top center;
            transition: transform 0.4s var(--ease-out-expo);
            will-change: transform;
        }

        .gallery__badge {
            position: absolute;
            top: 12px;
            left: 12px;
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            color: #ffffff;
            font-size: var(--smaller-font-size);
            font-weight: 700;
            padding: 4px 10px;
            border-radius: var(--radius-full);
            letter-spacing: 0.05em;
        }

        .gallery__caption {
            padding: 1.25rem 1.5rem;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }

        .gallery__title {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-color);
            margin-bottom: 0.35rem;
        }

        .gallery__desc {
            font-size: var(--small-font-size);
            color: var(--text-muted);
            line-height: 1.55;
            margin: 0;
        }"""

if project_css_old in html:
    html = html.replace(project_css_old, project_css_new)
    print("Updated project and gallery CSS")

# 2. Update Header & Nav
nav_logo_old = """<span class="nav__logo-text">Vishwa K</span>
                    <span class="nav__logo-badge">Founder</span>"""
nav_logo_new = """<span class="nav__logo-text">Vishwa Kumar</span>
                    <span class="nav__logo-badge">Founder & CEO</span>"""
if nav_logo_old in html:
    html = html.replace(nav_logo_old, nav_logo_new)
    print("Updated nav logo text and badge")

# Add Gallery to nav list
nav_item_about = """<li class="nav__item">
                        <a href="#about" class="nav__link">About</a>
                    </li>"""
nav_item_about_new = """<li class="nav__item">
                        <a href="#about" class="nav__link">About</a>
                    </li>
                    <li class="nav__item">
                        <a href="#gallery" class="nav__link">Presence</a>
                    </li>"""
if nav_item_about in html and '#gallery' not in html:
    html = html.replace(nav_item_about, nav_item_about_new)
    print("Added Presence to nav menu")

# 3. Update Hero Section
hero_old = """<div class="home__badge">
                    <span class="pulse-dot" aria-hidden="true"></span> Founder & Developer at Zinoin Group
                </div>
                <h1 class="home__name" id="hero-name">Vishwa K</h1>
                <div class="home__headline">
                    Founder. Developer.<br />
                    <span class="typing-container">
                        <span class="typing-text">Technology Enthusiast.</span>
                    </span>
                </div>
                <p class="home__description">
                    I build digital solutions and explore the intersection of technology, cybersecurity, and entrepreneurship.
                </p>"""

hero_new = """<div class="home__badge">
                    <span class="pulse-dot" aria-hidden="true"></span> Founder & CEO · Zinoin Group (Est. Aug 2025)
                </div>
                <h1 class="home__name" id="hero-name">Vishwa Kumar</h1>
                <div class="home__headline">
                    Founder & CEO.<br />
                    <span class="typing-container">
                        <span class="typing-text">Technology Entrepreneur.</span>
                    </span>
                </div>
                <p class="home__description">
                    Founder & CEO at Zinoin Group (established August 2025). Building enterprise software solutions, performance marketing funnels, and exploring cybersecurity engineering.
                </p>"""

if hero_old in html:
    html = html.replace(hero_old, hero_new)
    print("Updated Hero section")

# 4. Update About Section
about_old = """            <div class="about__container bd-grid">
                <div class="about__img-wrapper scroll-animate">
                    <picture>
                        <source srcset="assets/img/about.webp" type="image/webp">
                        <img src="assets/img/about.jpg" alt="Vishwa K — Founder & Developer at Zinoin Group, portrait photograph" class="about__img" width="400" height="400" loading="lazy" decoding="async">
                    </picture>
                </div>

                <div class="scroll-animate">
                    <h3 class="about__subtitle">Technology · Entrepreneurship · Cybersecurity</h3>
                    <p class="about__text">
                        I'm Vishwa K (also known as Vishwa Kumar), Founder & Developer at Zinoin Group, with a core focus on cybersecurity engineering, technology innovation, software and web development, and digital entrepreneurship.
                    </p>
                    <p class="about__text">
                        My journey combines business thinking with technology-driven problem-solving. I enjoy exploring new ideas, developing digital platforms, understanding business needs, and turning concepts into practical solutions.
                    </p>
                    <p class="about__text">
                        Through my work and learning journey, I continue to explore web development, digital marketing, cybersecurity, and emerging technologies.
                    </p>
                    <p class="about__text">
                        I believe in building solutions that are practical, scalable, and meaningful.
                    </p>

                    <div class="about__badges">
                        <div class="about__badge-item">
                            <i class='bx bx-briefcase-alt-2' aria-hidden="true"></i>
                            <div>
                                <span class="about__badge-label">Role</span>
                                <span class="about__badge-val">Founder & Developer</span>
                            </div>
                        </div>
                        <div class="about__badge-item">
                            <i class='bx bx-building-house' aria-hidden="true"></i>
                            <div>
                                <span class="about__badge-label">Organization</span>
                                <span class="about__badge-val">Zinoin Group</span>
                            </div>
                        </div>
                        <div class="about__badge-item">
                            <i class='bx bx-map-pin' aria-hidden="true"></i>
                            <div>
                                <span class="about__badge-label">Location</span>
                                <span class="about__badge-val">Tamil Nadu, India</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""

about_new = """            <div class="about__container bd-grid">
                <div class="about__img-wrapper scroll-animate">
                    <picture>
                        <source srcset="assets/img/vishwa-executive-standing.webp" type="image/webp">
                        <img src="assets/img/Vishwaimg/Screenshot_2026_1114_085830.png" alt="Vishwa Kumar — Founder & CEO at Zinoin Group, executive portrait" class="about__img" width="400" height="500" loading="lazy" decoding="async">
                    </picture>
                </div>

                <div class="scroll-animate">
                    <h3 class="about__subtitle">Technology · Entrepreneurship · Cybersecurity · Marketing</h3>
                    <p class="about__text">
                        I'm Vishwa Kumar (also known as Vishwa K), Founder & CEO at Zinoin Group, established in August 2025. My core focus spans cybersecurity engineering, full-stack software development, performance digital marketing, and venture building.
                    </p>
                    <p class="about__text">
                        My journey combines commercial strategic thinking with hands-on technical architecture. From building enterprise AI retrieval systems like DocuMind to delivering production e-commerce platforms and multi-channel marketing campaigns, I engineer practical solutions that bridge technology and business growth.
                    </p>
                    <p class="about__text">
                        Currently pursuing my engineering degree in Cyber Security at Sri Sai Ranganathan Engineering College, Coimbatore, I combine rigorous computer science fundamentals with real-world venture operations.
                    </p>
                    <p class="about__text">
                        I believe in building scalable digital infrastructure, maintaining defensive security hygiene, and delivering measurable commercial impact.
                    </p>

                    <div class="about__badges">
                        <div class="about__badge-item">
                            <i class='bx bx-briefcase-alt-2' aria-hidden="true"></i>
                            <div>
                                <span class="about__badge-label">Role</span>
                                <span class="about__badge-val">Founder & CEO</span>
                            </div>
                        </div>
                        <div class="about__badge-item">
                            <i class='bx bx-building-house' aria-hidden="true"></i>
                            <div>
                                <span class="about__badge-label">Organization</span>
                                <span class="about__badge-val">Zinoin Group (Est. Aug 2025)</span>
                            </div>
                        </div>
                        <div class="about__badge-item">
                            <i class='bx bx-map-pin' aria-hidden="true"></i>
                            <div>
                                <span class="about__badge-label">Location</span>
                                <span class="about__badge-val">Tamil Nadu, India</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""

if about_old in html:
    html = html.replace(about_old, about_new)
    print("Updated About section")

# 5. Insert Gallery Section after About
gallery_section = """
        <!--===== EXECUTIVE GALLERY =====-->
        <section class="gallery section" id="gallery" aria-labelledby="gallery-heading">
            <h2 class="section-title" id="gallery-heading">Executive Presence</h2>

            <div class="gallery__container bd-grid">
                <!-- 1. CEO Office Suite -->
                <div class="gallery__card scroll-animate">
                    <div class="gallery__img-box">
                        <picture>
                            <source srcset="assets/img/vishwa-ceo-full.webp" type="image/webp">
                            <img src="assets/img/Vishwaimg/Screenshot_2026_1114_091424.png" alt="Vishwa Kumar, Founder & CEO at Zinoin Group in executive office suite" class="gallery__img" width="718" height="1096" loading="lazy" decoding="async">
                        </picture>
                        <span class="gallery__badge">Founder & CEO</span>
                    </div>
                    <div class="gallery__caption">
                        <h3 class="gallery__title">Executive Office Suite</h3>
                        <p class="gallery__desc">Zinoin Group executive operations and strategic venture leadership.</p>
                    </div>
                </div>

                <!-- 2. Corporate Leadership -->
                <div class="gallery__card scroll-animate">
                    <div class="gallery__img-box">
                        <picture>
                            <source srcset="assets/img/vishwa-executive-standing.webp" type="image/webp">
                            <img src="assets/img/Vishwaimg/Screenshot_2026_1114_085830.png" alt="Vishwa Kumar, executive leadership portrait" class="gallery__img" width="798" height="1002" loading="lazy" decoding="async">
                        </picture>
                        <span class="gallery__badge">Leadership</span>
                    </div>
                    <div class="gallery__caption">
                        <h3 class="gallery__title">Corporate Leadership</h3>
                        <p class="gallery__desc">Driving software engineering, performance marketing, and digital infrastructure.</p>
                    </div>
                </div>

                <!-- 3. Executive Workspace -->
                <div class="gallery__card scroll-animate">
                    <div class="gallery__img-box">
                        <picture>
                            <source srcset="assets/img/vishwa-executive-seated.webp" type="image/webp">
                            <img src="assets/img/Vishwaimg/Screenshot_2026_1114_085759.png" alt="Vishwa Kumar at executive workspace desk" class="gallery__img" width="946" height="742" loading="lazy" decoding="async">
                        </picture>
                        <span class="gallery__badge">Workspace</span>
                    </div>
                    <div class="gallery__caption">
                        <h3 class="gallery__title">Development & Strategy Desk</h3>
                        <p class="gallery__desc">Hands-on architecture of AI knowledge systems and commercial platforms.</p>
                    </div>
                </div>

                <!-- 4. Business Strategy Keynote -->
                <div class="gallery__card scroll-animate">
                    <div class="gallery__img-box">
                        <picture>
                            <source srcset="assets/img/vishwa-business-strategy.webp" type="image/webp">
                            <img src="assets/img/Vishwaimg/Screenshot_2026_1114_090009.png" alt="Vishwa Kumar presenting business strategy and digital growth" class="gallery__img" width="667" height="370" loading="lazy" decoding="async">
                        </picture>
                        <span class="gallery__badge">Strategy</span>
                    </div>
                    <div class="gallery__caption">
                        <h3 class="gallery__title">Business Strategy & Growth</h3>
                        <p class="gallery__desc">Presenting digital innovation, client growth funnels, and enterprise execution.</p>
                    </div>
                </div>

                <!-- 5. Vision & Innovation -->
                <div class="gallery__card scroll-animate">
                    <div class="gallery__img-box">
                        <picture>
                            <source srcset="assets/img/vishwa-window-skyline.webp" type="image/webp">
                            <img src="assets/img/Vishwaimg/Screenshot_2026_1114_085900.png" alt="Vishwa Kumar, digital innovation and vision portrait" class="gallery__img" width="622" height="671" loading="lazy" decoding="async">
                        </picture>
                        <span class="gallery__badge">Innovation</span>
                    </div>
                    <div class="gallery__caption">
                        <h3 class="gallery__title">Vision & Innovation</h3>
                        <p class="gallery__desc">Bridging cybersecurity engineering with commercial tech solutions.</p>
                    </div>
                </div>
            </div>
        </section>
"""

if 'id="gallery"' not in html:
    html = html.replace('</section>\n\n        <!--===== EXPERTISE =====-->', '</section>\n' + gallery_section + '\n        <!--===== EXPERTISE =====-->')
    print("Inserted Gallery section after About")

# 6. Update Footer Tagline
footer_old = """<div class="footer__brand">
                <p class="footer__title">Vishwa K</p>
                <p class="footer__tagline">Founder & Developer · Zinoin Group</p>
            </div>"""

footer_new = """<div class="footer__brand">
                <p class="footer__title">Vishwa Kumar</p>
                <p class="footer__tagline">Founder & CEO · Zinoin Group (Est. Aug 2025)</p>
            </div>"""

if footer_old in html:
    html = html.replace(footer_old, footer_new)
    print("Updated footer brand and tagline")

# Add gallery to footer quick links
footer_links_old = """<li><a href="#about" class="footer__nav-link">About</a></li>"""
footer_links_new = """<li><a href="#about" class="footer__nav-link">About</a></li>
                    <li><a href="#gallery" class="footer__nav-link">Presence</a></li>"""
if footer_links_old in html and 'href="#gallery" class="footer__nav-link"' not in html:
    html = html.replace(footer_links_old, footer_links_new)
    print("Added Presence to footer nav links")

with open("founder.zinoingroup.in/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html successfully!")

