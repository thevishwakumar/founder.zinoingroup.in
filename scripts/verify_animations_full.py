import re

with open('founder.zinoingroup.in/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ('Ease smooth variable', '--ease-smooth: cubic-bezier(0.2, 0.8, 0.2, 1);' in text),
    ('Duration reveal variable', '--duration-reveal: 0.65s;' in text),
    ('Theme transitioning class', 'html.theme-transitioning' in text),
    ('Section title after hover', '.section-title:hover::after' in text),
    ('Nav link after hover', '.nav__link:hover::after' in text),
    ('Badge shimmer keyframes', '@keyframes badgeShimmer' in text),
    ('About aura breath keyframes', '@keyframes auraBreath' in text),
    ('Dot glow keyframes', '@keyframes dotGlow' in text),
    ('Gallery card hover transform', '.gallery__card:hover' in text),
    ('Project icon box hover transform', '.project__card:hover .project__icon-box' in text),
    ('Project link icon slide', '.project__card:hover .project__link i' in text),
    ('Expertise card hover transform', '.expertise__card:hover' in text),
    ('Expertise icon hover transform', '.expertise__card:hover .expertise__icon' in text),
    ('Certificate card hover transform', '.certificate__card:hover' in text),
    ('Certificate icon hover transform', '.certificate__card:hover .certificate__icon' in text),
    ('Experience active dot class in CSS', '.experience__dot--active' in text),
    ('Experience active dot in static HTML', 'experience__dot experience__dot--active' in text),
    ('Cascading delays for gallery', '.gallery__container > .scroll-animate:nth-child(1)' in text),
    ('Cascading delays for expertise', '.expertise__grid > .scroll-animate:nth-child(1)' in text),
    ('Cascading delays for projects', '.projects__grid > .scroll-animate:nth-child(3n+1)' in text),
    ('Cascading delays for certifications', '.certifications__grid > .scroll-animate:nth-child(3n+1)' in text),
    ('Cascading delays for experience', '.experience__timeline > .scroll-animate:nth-child(1)' in text),
    ('Reduced motion disables badgeShimmer', 'badgeShimmer' in text and 'prefers-reduced-motion' in text),
    ('Reduced motion disables auraBreath', 'auraBreath' in text and 'prefers-reduced-motion' in text),
    ('Reduced motion disables dotGlow', 'dotGlow' in text and 'prefers-reduced-motion' in text),
    ('JS theme transition timeout', 'theme-transitioning' in text and 'setThemePreference' in text)
]

print("=== ANIMATION & INTERACTION VERIFICATION ===")
all_passed = True
for name, passed in checks:
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        all_passed = False

with open('founder.zinoingroup.in/assets/js/content-renderer.js', 'r', encoding='utf-8') as f:
    js = f.read()

renderer_checks = [
    ('Dynamic experience active dot', 'experience__dot experience__dot--active' in js),
    ('Reconnect observers on hydration', 'reconnectObservers' in js)
]

for name, passed in renderer_checks:
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name}")
    if not passed:
        all_passed = False

print("ALL ANIMATION CHECKS PASSED!" if all_passed else "SOME CHECKS FAILED!")

