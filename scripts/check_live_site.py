import urllib.request
import urllib.error
import ssl

url = "https://founder.zinoingroup.in/"
print(f"Connecting to live production: {url}")
try:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}
    )
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        print(f"Status Code: {resp.status}")
        print("Response Headers:")
        for k, v in resp.headers.items():
            if k.lower() in ['server', 'cf-ray', 'content-type', 'content-length', 'cache-control', 'x-content-type-options']:
                print(f"  {k}: {v}")
        body = resp.read().decode('utf-8', errors='ignore')
        print(f"Body length: {len(body)} characters")
        # Check title in live site
        import re
        t = re.search(r'<title>(.*?)</title>', body, re.IGNORECASE)
        if t:
            print(f"Live Title: {t.group(1)}")
except Exception as e:
    print(f"Live connection error: {e}")
