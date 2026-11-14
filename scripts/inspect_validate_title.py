with open("scripts/validate_site.py", encoding="utf-8") as f:
    for line in f:
        if "title" in line.lower():
            print(line.rstrip())
