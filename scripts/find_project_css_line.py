with open("founder.zinoingroup.in/index.html", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        if ".project__card" in line:
            print(f"Line {idx+1}: {line.rstrip()}")

