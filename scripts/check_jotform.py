import glob, os

for fpath in glob.glob("*.md"):
    with open(fpath, encoding="utf-8", errors="ignore") as f:
        content = f.read()
        if "jotform" in content.lower():
            print(f"Found 'jotform' in {fpath}")
