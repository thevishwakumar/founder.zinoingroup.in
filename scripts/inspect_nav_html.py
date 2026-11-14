with open("founder.zinoingroup.in/index.html", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if '<nav class="nav' in line:
        print(f"Nav at line {idx+1}")
        for j in range(idx, min(len(lines), idx+40)):
            print(f"{j+1}: {lines[j].rstrip()}")
        break

