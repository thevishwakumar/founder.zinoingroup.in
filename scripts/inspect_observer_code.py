with open("founder.zinoingroup.in/index.html", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'IntersectionObserver' in line:
        print(f"IntersectionObserver at line {idx+1}")
        for j in range(max(0, idx-10), min(len(lines), idx+50)):
            print(f"{j+1}: {lines[j].rstrip()}")
        break

