import re

with open('founder.zinoingroup.in/index.html', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'id="contact"' in line or 'id=\'contact\'' in line or 'name="contact"' in line:
        print(f"Contact section starts at line {idx+1}")
        for j in range(max(0, idx-5), min(len(lines), idx+65)):
            print(f"{j+1}: {lines[j].rstrip()}")
        break
