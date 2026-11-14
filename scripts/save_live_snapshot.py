import urllib.request
import ssl
import os

url = "https://founder.zinoingroup.in/"
ctx = ssl.create_default_context()
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
)
with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
    content = resp.read()

with open("live_production_snapshot.html", "wb") as f:
    f.write(content)

print(f"Saved live production snapshot ({len(content):,} bytes) to live_production_snapshot.html")
