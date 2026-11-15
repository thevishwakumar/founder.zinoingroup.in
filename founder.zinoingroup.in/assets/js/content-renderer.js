/**
 * Vishwa K - Lightweight Content Management & Dynamic Renderer
 * Architecture: Progressive Enhancement / Safe Static Hydration
 * 
 * Features:
 * - 100% Vanilla JavaScript (Zero external dependencies)
 * - Safe DOM construction (Zero unsafe innerHTML injection of untrusted data)
 * - Strict schema validation with graceful fallbacks
 * - Rock-solid static HTML fallback if JSON fetch fails or JavaScript is disabled
 * - Reconnects scroll animations & telemetry observers dynamically
 */

(function (window, document) {
    'use strict';

    // Safe HTML Escaping Utility
    function escapeHTML(str) {
        if (str === null || str === undefined) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    // Helper: Safely create an element with attributes and children
    function el(tag, attributes = {}, ...children) {
        const element = document.createElement(tag);
        for (const [key, val] of Object.entries(attributes)) {
            if (val === null || val === undefined || val === false) continue;
            if (key === 'className') {
                element.className = val;
            } else if (key === 'style') {
                element.style.cssText = val;
            } else if (key.startsWith('on') && typeof val === 'function') {
                element.addEventListener(key.slice(2).toLowerCase(), val);
            } else if (key === 'dataset') {
                for (const [dKey, dVal] of Object.entries(val)) {
                    element.dataset[dKey] = dVal;
                }
            } else {
                element.setAttribute(key, val);
            }
        }
        for (const child of children) {
            if (child === null || child === undefined) continue;
            if (typeof child === 'string' || typeof child === 'number') {
                element.appendChild(document.createTextNode(String(child)));
            } else if (child instanceof Node) {
                element.appendChild(child);
            }
        }
        return element;
    }

    // Helper: Create an icon element with class
    function icon(className, ariaHidden = true) {
        return el('i', { className: className, 'aria-hidden': ariaHidden ? 'true' : 'false' });
    }

    // Skill to Context-Appropriate Boxicon Mapping
    const SKILL_ICON_MAP = {
        // Technology & Software Development
        'Frontend Development': 'bx bx-layout',
        'Generative AI & Prompt Engineering': 'bx bx-brain',
        'WordPress Development & Custom CMS': 'bx bxl-wordpress',
        'Data Analysis & Business Telemetry': 'bx bx-bar-chart-alt-2',
        'Full-Stack Web Development': 'bx bx-layer',
        'Python, Java & SQL Architecture': 'bx bxl-python',
        'React & Modern UI Frameworks': 'bx bxl-react',
        'Relational Databases (MySQL & PostgreSQL)': 'bx bxl-postgresql',
        'Developer Tools (Git, GitHub, VS Code, Postman)': 'bx bxl-git',
        'REST APIs & Cloudflare Serverless Architecture': 'bx bx-cloud',

        // Digital Marketing & Growth Strategy
        'Meta Ads & Facebook Ads Manager': 'bx bxl-meta',
        'Google Ads & PPC Advertising': 'bx bxl-google',
        'Social Media Marketing & Brand Reach': 'bx bx-share-alt',
        'Email Marketing & Automated Funnels': 'bx bx-envelope',
        'Marketing Strategy & Growth Strategy': 'bx bx-line-chart',
        'Digital Marketing & Multi-Channel Campaigns': 'bx bx-broadcast',
        'SEO Optimization & Entity Search': 'bx bx-search-alt',
        'Google Analytics 4 & Measurement': 'bx bx-pie-chart-alt',
        'Conversion Rate Optimization (CRO)': 'bx bx-trending-up',
        'Campaign Manager 360 & Ad Operations': 'bx bx-slider-alt',

        // Entrepreneurship & Business Management
        'Leadership & Team Management': 'bx bx-group',
        'Business Administration & Operations Management': 'bx bx-briefcase-alt',
        'Business Management & Executive Leadership': 'bx bx-crown',
        'Business Development & Partnerships': 'bx bx-network-chart',
        'Strategic Planning & Market Research': 'bx bx-compass',
        'Financial Planning & Financial Operations': 'bx bx-dollar-circle',
        'Risk Management & Banking Processes': 'bx bx-shield-quarter',
        'Innovation Thinking & Business Ideation': 'bx bx-bulb',
        'Commercial Client Software Delivery': 'bx bx-package',
        'Agile Project Scoping & Delivery': 'bx bx-task',

        // Cybersecurity & Systems Engineering
        'Network Security (TCP/IP, DNS, HTTP/HTTPS, SSH, VPN)': 'bx bx-shield-alt-2',
        'Packet Inspection & Analysis (Wireshark, Nmap, Tracer)': 'bx bx-radar',
        'Autonomous Cyber Defense & Deception Trap Networks': 'bx bx-shield-plus',
        'Vulnerability Assessment & Ethical Hacking': 'bx bx-bug',
        'Phishing Detection & Security Log Analysis': 'bx bx-file-find',
        'Identity & Access Management (RBAC & Auth)': 'bx bx-key',
        'Cloud Security (AWS IAM, VPC, Security Groups, KMS)': 'bx bx-lock-alt',
        'Linux Server Hardening & CLI Administration': 'bx bxl-tux',
        'AI Data Confidentiality & Compliance Shield (DLP)': 'bx bx-check-shield',
        'Security Risk Management (ISO 27001 Standards)': 'bx bx-award'
    };

    function getSkillIcon(skillName) {
        if (!skillName) return 'bx bx-check';
        const trimmed = skillName.trim();
        if (SKILL_ICON_MAP[trimmed]) return SKILL_ICON_MAP[trimmed];
        
        const lower = trimmed.toLowerCase();
        if (lower.includes('python')) return 'bx bxl-python';
        if (lower.includes('react')) return 'bx bxl-react';
        if (lower.includes('wordpress')) return 'bx bxl-wordpress';
        if (lower.includes('git')) return 'bx bxl-git';
        if (lower.includes('postgres') || lower.includes('sql') || lower.includes('database')) return 'bx bxl-postgresql';
        if (lower.includes('cloud') || lower.includes('api')) return 'bx bx-cloud';
        if (lower.includes('ai') || lower.includes('prompt') || lower.includes('brain')) return 'bx bx-brain';
        if (lower.includes('meta') || lower.includes('facebook')) return 'bx bxl-meta';
        if (lower.includes('google') || lower.includes('ppc')) return 'bx bxl-google';
        if (lower.includes('seo') || lower.includes('search')) return 'bx bx-search-alt';
        if (lower.includes('analytics') || lower.includes('telemetry')) return 'bx bx-pie-chart-alt';
        if (lower.includes('market') || lower.includes('funnel')) return 'bx bx-line-chart';
        if (lower.includes('security') || lower.includes('defense') || lower.includes('shield')) return 'bx bx-shield-quarter';
        if (lower.includes('hack') || lower.includes('vulnerability')) return 'bx bx-bug';
        if (lower.includes('packet') || lower.includes('network') || lower.includes('wireshark')) return 'bx bx-radar';
        if (lower.includes('linux')) return 'bx bxl-tux';
        if (lower.includes('leadership') || lower.includes('team') || lower.includes('management')) return 'bx bx-group';
        if (lower.includes('finance') || lower.includes('banking') || lower.includes('dollar')) return 'bx bx-dollar-circle';
        if (lower.includes('frontend') || lower.includes('ui') || lower.includes('web')) return 'bx bx-layout';
        return 'bx bx-check';
    }

    const ContentManager = {
        basePath: 'data/',
        manifest: {
            profile: 'profile.json',
            expertise: 'expertise.json',
            projects: 'projects.json',
            experience: 'experience.json',
            education: 'education.json',
            certifications: 'certifications.json',
            socialLinks: 'social-links.json'
        },
        cache: {},

        // Fetch JSON with validation and caching
        async fetchJSON(key) {
            const fileName = this.manifest[key];
            if (!fileName) throw new Error(`Unknown content manifest key: ${key}`);
            if (this.cache[key]) return this.cache[key];

            try {
                const response = await fetch(`${this.basePath}${fileName}`, {
                    headers: { 'Accept': 'application/json' },
                    cache: 'default'
                });
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status} while fetching ${fileName}`);
                }
                const data = await response.json();
                this.cache[key] = data;
                return data;
            } catch (err) {
                console.warn(`[ContentManager] Notice: Failed to load ${fileName} (${err.message}). Retaining pre-rendered static content.`);
                return null;
            }
        },

        // 1. Render Expertise Section
        renderExpertise(data, container) {
            if (!data || !Array.isArray(data.categories) || data.categories.length === 0) return false;
            
            const fragment = document.createDocumentFragment();
            data.categories.forEach(category => {
                // Validation: required fields
                if (!category.title) return;

                const card = el('div', { className: 'expertise__card scroll-animate' },
                    el('div', { className: 'expertise__icon', 'aria-hidden': 'true' },
                        icon(category.icon || 'bx bx-check')
                    ),
                    el('h3', { className: 'expertise__card-title' }, category.title)
                );

                if (Array.isArray(category.skills) && category.skills.length > 0) {
                    const ul = el('ul', { className: 'expertise__list' });
                    category.skills.forEach(skill => {
                        if (typeof skill === 'string' && skill.trim().length > 0) {
                            const trimmedSkill = skill.trim();
                            const skillIcon = getSkillIcon(trimmedSkill);
                            ul.appendChild(
                                el('li', { className: 'expertise__item' },
                                    icon(skillIcon, true),
                                    ' ',
                                    trimmedSkill
                                )
                            );
                        }
                    });
                    card.appendChild(ul);
                }

                fragment.appendChild(card);
            });

            container.innerHTML = '';
            container.appendChild(fragment);
            return true;
        },

        // 2. Render Projects Section
        renderProjects(data, container) {
            if (!data || !Array.isArray(data.projects) || data.projects.length === 0) return false;

            const fragment = document.createDocumentFragment();
            data.projects.forEach(project => {
                // Validation: required fields
                if (!project.title || !project.description) return;

                // Card Icon Header (Icons only, zero logos/images)
                const iconWrapper = el('div', { className: 'project__icon-wrapper' },
                    el('div', { className: 'project__icon-box' },
                        icon(project.icon || 'bx bx-code-alt')
                    )
                );

                if (project.badge) {
                    iconWrapper.appendChild(
                        el('span', {
                            className: 'project__badge-pill',
                            style: project.badgeStyle || ''
                        }, project.badge)
                    );
                }

                // Card Content Body
                const content = el('div', { className: 'project__content' },
                    el('h3', { className: 'project__title' }, project.title)
                );

                if (project.tagline) {
                    content.appendChild(el('p', { className: 'project__tagline' }, project.tagline));
                }

                content.appendChild(el('p', { className: 'project__desc' }, project.description));

                // Tech Pills
                if (Array.isArray(project.technologies) && project.technologies.length > 0) {
                    const tagsDiv = el('div', { className: 'project__tech-tags' });
                    project.technologies.forEach(tech => {
                        tagsDiv.appendChild(el('span', { className: 'tech-pill' }, tech));
                    });
                    content.appendChild(tagsDiv);
                }

                // Action Buttons
                if (Array.isArray(project.actions) && project.actions.length > 0) {
                    const actionsDiv = el('div', { className: 'project__actions' });
                    project.actions.forEach(action => {
                        if (action.type === 'link' && action.url) {
                            actionsDiv.appendChild(
                                el('a', {
                                    href: action.url,
                                    target: '_blank',
                                    rel: 'noopener noreferrer',
                                    className: `button button--small ${action.buttonClass || 'button--secondary'} project__link`,
                                    'aria-label': action.ariaLabel || action.label
                                },
                                    action.icon ? icon(action.icon) : null,
                                    action.icon ? ' ' : '',
                                    action.label
                                )
                            );
                        } else if (action.type === 'pill') {
                            actionsDiv.appendChild(
                                el('span', {
                                    className: 'tech-pill',
                                    style: action.pillStyle || ''
                                },
                                    action.icon ? icon(action.icon) : null,
                                    action.icon ? ' ' : '',
                                    action.label
                                )
                            );
                        }
                    });
                    content.appendChild(actionsDiv);
                }

                const card = el('div', { className: 'project__card scroll-animate' }, iconWrapper, content);
                fragment.appendChild(card);
            });

            container.innerHTML = '';
            container.appendChild(fragment);
            return true;
        },

        // 3. Render Experience Section
        renderExperience(data, container) {
            if (!data || !Array.isArray(data.experiences) || data.experiences.length === 0) return false;

            const fragment = document.createDocumentFragment();
            data.experiences.forEach((exp, index) => {
                if (!exp.role || !exp.company) return;

                const headerLeft = el('div', {},
                    el('h3', { className: 'experience__role-title' }, exp.role),
                    el('span', { className: 'experience__company' },
                        icon(exp.companyIcon || 'bx bx-building-house'),
                        ' ',
                        exp.company
                    )
                );

                const header = el('div', { className: 'experience__header' }, headerLeft);

                if (exp.period) {
                    header.appendChild(
                        el('span', {
                            className: 'experience__badge',
                            style: exp.badgeStyle || ''
                        },
                            icon('bx bx-time-five'),
                            ` ${exp.period}${exp.status ? ' · ' + exp.status : ''}`
                        )
                    );
                }

                const card = el('div', { className: 'experience__card' }, header);

                if (exp.description) {
                    card.appendChild(el('p', { className: 'experience__desc' }, exp.description));
                }

                // Bullets
                if (Array.isArray(exp.bullets) && exp.bullets.length > 0) {
                    const bulletsDiv = el('div', { className: 'experience__bullets' });
                    exp.bullets.forEach(b => {
                        const bulletText = typeof b === 'string' ? b : (b && b.text ? b.text : '');
                        const bulletIcon = (typeof b === 'object' && b && b.icon) ? b.icon : 'bx bx-check-shield';
                        if (bulletText) {
                            bulletsDiv.appendChild(
                                el('div', { className: 'experience__bullet-item' },
                                    icon(bulletIcon),
                                    el('span', {}, bulletText)
                                )
                            );
                        }
                    });
                    card.appendChild(bulletsDiv);
                }

                // Tech chips
                if (Array.isArray(exp.technologies) && exp.technologies.length > 0) {
                    const techDiv = el('div', { className: 'experience__tech-chips' });
                    exp.technologies.forEach(tech => {
                        techDiv.appendChild(el('span', { className: 'tech-pill' }, tech));
                    });
                    card.appendChild(techDiv);
                }

                const dotClass = (index === 0) ? 'experience__dot experience__dot--active' : 'experience__dot';
                const item = el('div', { className: 'experience__item scroll-animate' },
                    el('div', { className: dotClass, 'aria-hidden': 'true' }),
                    card
                );

                fragment.appendChild(item);
            });

            container.innerHTML = '';
            container.appendChild(fragment);
            return true;
        },

        // 4. Render Education Section
        renderEducation(data, container) {
            if (!data || !Array.isArray(data.education) || data.education.length === 0) return false;

            const fragment = document.createDocumentFragment();
            data.education.forEach(edu => {
                if (!edu.degree || !edu.institution) return;

                const cardHeader = el('div', { className: 'education__card-header' });
                if (edu.badge) {
                    cardHeader.appendChild(el('span', { className: 'education__badge' }, edu.badge));
                }
                if (edu.period) {
                    cardHeader.appendChild(
                        el('span', { className: 'education__date' },
                            icon(edu.dateIcon || 'bx bx-calendar'),
                            ' ',
                            edu.period
                        )
                    );
                }

                const card = el('div', { className: 'education__card scroll-animate' },
                    cardHeader,
                    el('h3', { className: 'education__title' }, edu.degree)
                );

                if (edu.field) {
                    card.appendChild(
                        el('p', { className: 'education__institution' },
                            icon(edu.fieldIcon || 'bx bx-certification'),
                            ' ',
                            edu.field
                        )
                    );
                }

                if (edu.institution) {
                    card.appendChild(
                        el('p', { className: 'education__location' },
                            icon(edu.institutionIcon || 'bx bx-building-house'),
                            ' ',
                            `${edu.institution}${edu.location ? ', ' + edu.location : ''}`
                        )
                    );
                }

                if (Array.isArray(edu.meta) && edu.meta.length > 0) {
                    const metaDiv = el('div', { className: 'education__meta' });
                    edu.meta.forEach(m => {
                        let metaIconClass = null;
                        const lbl = (m.label || '').toLowerCase();
                        if (lbl.includes('cgpa')) metaIconClass = 'bx bx-award';
                        else if (lbl.includes('coursework')) metaIconClass = 'bx bx-book-bookmark';
                        else if (lbl.includes('performance')) metaIconClass = 'bx bx-bar-chart-alt-2';

                        const itemDiv = el('div', { className: 'education__meta-item' });
                        if (metaIconClass) {
                            itemDiv.appendChild(icon(metaIconClass));
                            itemDiv.appendChild(document.createTextNode(' '));
                        }
                        itemDiv.appendChild(el('span', {}, m.label));
                        itemDiv.appendChild(document.createTextNode(' '));

                        if (m.isHighlight) {
                            itemDiv.appendChild(
                                el('strong', { className: 'education__status' },
                                    m.statusIcon ? icon(m.statusIcon) : null,
                                    m.statusIcon ? ' ' : '',
                                    m.value
                                )
                            );
                        } else {
                            itemDiv.appendChild(el('strong', {}, m.value));
                        }
                        metaDiv.appendChild(itemDiv);
                    });
                    card.appendChild(metaDiv);
                }

                fragment.appendChild(card);
            });

            container.innerHTML = '';
            container.appendChild(fragment);
            return true;
        },

        // 5. Render Certifications Section
        renderCertifications(data, container) {
            if (!data || !Array.isArray(data.certifications) || data.certifications.length === 0) return false;

            const fragment = document.createDocumentFragment();
            data.certifications.forEach(cert => {
                if (!cert.title || !cert.organization) return;

                const topDiv = el('div', {},
                    el('div', { className: 'certificate__org-badge' },
                        icon(cert.orgIcon || 'bx bx-award'),
                        ' ',
                        cert.organization
                    ),
                    el('h3', { className: 'certificate__card-title' }, cert.title)
                );

                const footerDiv = el('div', { className: 'certificate__footer' });
                if (cert.link && cert.link.url) {
                    footerDiv.appendChild(
                        el('a', {
                            href: cert.link.url,
                            target: '_blank',
                            rel: 'noopener noreferrer',
                            className: 'certificate__link',
                            title: cert.link.title || cert.title
                        },
                            cert.link.text || 'Verify Certificate',
                            ' ',
                            icon('bx bx-link-external')
                        )
                    );
                } else if (cert.footerLabel) {
                    footerDiv.appendChild(el('span', {}, cert.footerLabel));
                }

                if (cert.status) {
                    footerDiv.appendChild(
                        el('span', { className: 'certificate__status-verified' },
                            icon('bx bx-check-circle'),
                            ' ',
                            cert.status
                        )
                    );
                }

                const card = el('div', { className: 'certificate__card scroll-animate' }, topDiv, footerDiv);
                fragment.appendChild(card);
            });

            container.innerHTML = '';
            container.appendChild(fragment);
            return true;
        },

        // Reconnect observers after dynamic DOM re-rendering
        reconnectObservers() {
            // Reconnect Scroll Reveal
            if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
                const scrollElements = document.querySelectorAll('.scroll-animate:not(.show)');
                const revealObserver = new IntersectionObserver((entries, observer) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('show');
                            observer.unobserve(entry.target);
                        }
                    });
                }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

                scrollElements.forEach(el => revealObserver.observe(el));
            }

            // Reconnect Project Telemetry Click Listeners
            if (typeof window.trackEvent === 'function') {
                document.querySelectorAll('.project__link').forEach(link => {
                    link.addEventListener('click', function () {
                        const card = this.closest('.project__card');
                        const title = card ? card.querySelector('.project__title')?.textContent.trim() : 'Project';
                        window.trackEvent('project_click', {
                            project_name: title,
                            target_url: this.href
                        });
                    }, { passive: true });
                });
            }
        },

        // Orchestrator: Hydrate all repeatable sections
        async hydrateAll() {
            const targets = {
                expertise: document.querySelector('.expertise__grid'),
                projects: document.querySelector('.projects__grid'),
                experience: document.querySelector('.experience__timeline'),
                education: document.querySelector('.education__container'),
                certifications: document.querySelector('.certifications__grid')
            };

            const tasks = [
                { key: 'expertise', container: targets.expertise, fn: this.renderExpertise.bind(this) },
                { key: 'projects', container: targets.projects, fn: this.renderProjects.bind(this) },
                { key: 'experience', container: targets.experience, fn: this.renderExperience.bind(this) },
                { key: 'education', container: targets.education, fn: this.renderEducation.bind(this) },
                { key: 'certifications', container: targets.certifications, fn: this.renderCertifications.bind(this) }
            ];

            let reRendered = false;
            for (const task of tasks) {
                if (!task.container) continue;
                const data = await this.fetchJSON(task.key);
                if (data) {
                    const success = task.fn(data, task.container);
                    if (success) reRendered = true;
                }
            }

            if (reRendered) {
                this.reconnectObservers();
                document.dispatchEvent(new CustomEvent('content:hydrated', { detail: { timestamp: Date.now() } }));
            }
        }
    };

    // Expose ContentManager to global window for programmatic updates
    window.ContentManager = ContentManager;

    // Automatic Progressive Hydration when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () {
            ContentManager.hydrateAll();
        });
    } else {
        ContentManager.hydrateAll();
    }

})(window, document);
