import json, glob, os

for fpath in sorted(glob.glob("founder.zinoingroup.in/data/*.json")):
    fname = os.path.basename(fpath)
    with open(fpath, encoding="utf-8") as f:
        data = json.load(f)
    print(f"=== {fname} ===")
    if isinstance(data, list):
        print(f"List with {len(data)} items:")
        for item in data[:3]:
            print(" ", item.get("title") or item.get("name") or item.get("category") or item.get("platform") or str(item)[:60])
    elif isinstance(data, dict):
        print("Dict keys:", list(data.keys()))
        for k in ["fullName", "headline", "verified", "contact"]:
            if k in data:
                print(f"  {k}: {data[k]}")
