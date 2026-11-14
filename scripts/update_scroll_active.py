with open('founder.zinoingroup.in/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        function scrollActive() {
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
            isScrollSpyTicking = false;
        }"""

replacement = """        function scrollActive() {
            const scrollY = window.pageYOffset;

            sections.forEach(current => {
                const sectionHeight = current.offsetHeight;
                const sectionTop = current.offsetTop - 120;
                const sectionId = current.getAttribute('id');
                const navAnchors = document.querySelectorAll('.nav__menu a[href*=' + sectionId + ']');

                navAnchors.forEach(navAnchor => {
                    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                        navAnchor.classList.add('active');
                        // Highlight parent dropdown trigger if inside a dropdown
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
            isScrollSpyTicking = false;
        }"""

assert target in text, "Target scrollActive not found!"
text = text.replace(target, replacement, 1)

with open('founder.zinoingroup.in/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Successfully updated scrollActive for dropdowns!")

