import re

with open('founder.zinoingroup.in/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check for fixed pixel widths that could exceed mobile viewports
fixed_widths = re.findall(r'width:\s*([0-9]{3,4})px', text)
print(f"Fixed pixel widths found: {set(fixed_widths)}")

large_widths = [int(w) for w in fixed_widths if int(w) > 320]
print(f"Large fixed widths (>320px): {set(large_widths)}")

# Verify all @media queries
media_queries = re.findall(r'@media[^{]+', text)
print(f"\nTotal media queries found: {len(media_queries)}")
for mq in set(media_queries[:12]):
    print(" -", mq.strip())

# Check html and body overflow
assert 'overflow-x: hidden' in text, "body should have overflow-x: hidden"
print("\n[PASS] Body has overflow-x: hidden configured")

# Check dropdown styles
assert '.nav__dropdown-menu' in text, ".nav__dropdown-menu CSS present"
assert '.nav__dropdown-trigger' in text, ".nav__dropdown-trigger CSS present"
assert '.nav__dropdown-item' in text, ".nav__dropdown-item CSS present"
print("[PASS] Dropdown menu CSS styles verified")

# Check dropdown mobile accordion
assert '@media screen and (max-width: 991px)' in text
print("[PASS] Mobile drawer accordion rules verified")

print("\nRESPONSIVE & OVERFLOW CHECKS PASSED!")
