with open("founder.zinoingroup.in/index.html", encoding="utf-8") as f:
    lines = f.readlines()

for idx in range(35, 120):
    print(f"{idx+1}: {lines[idx].rstrip()}")
