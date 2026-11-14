import os, subprocess, time

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

out_dir = r"C:\Users\Vishw\.gemini\antigravity\brain\0a3c84f3-2c5f-4937-afe8-95b977cc1af2"

viewports = [
    ("desktop_1440_animated", 1440, 900),
    ("phone_390_animated", 390, 844)
]

for name, w, h in viewports:
    out_file = os.path.join(out_dir, f"{name}.png")
    cmd = [
        chrome_path,
        "--headless=new",
        f"--window-size={w},{h}",
        f"--screenshot={out_file}",
        "--hide-scrollbars",
        "--disable-gpu",
        "http://localhost:8080/"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_file):
        print(f"Captured {name}: {os.path.getsize(out_file)} bytes at {out_file}")
    else:
        print(f"Failed to capture {name}: {res.stderr}")

