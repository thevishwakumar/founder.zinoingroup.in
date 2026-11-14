with open('founder.zinoingroup.in/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert '/*===== SCROLL REVEAL ANIMATIONS (PROGRESSIVE ENHANCEMENT) =====*/' in text
assert 'function setThemePreference(pref)' in text
assert '/* Subtle Hero Entrance Animation (Compositor-only, zero CLS) */' in text
assert '/*===== EXECUTIVE GALLERY =====*/' in text

print('All key targets verified in index.html!')

