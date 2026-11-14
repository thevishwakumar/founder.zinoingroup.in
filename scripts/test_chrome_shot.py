import os, subprocess, tempfile

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

out_dir = r"C:\Users\Vishw\.gemini\antigravity\brain\0a3c84f3-2c5f-4937-afe8-95b977cc1af2"
user_data_dir = os.path.join(tempfile.gettempdir(), "chrome_anim_test")

out_file = os.path.join(out_dir, "desktop_1440_animated.png")
cmd = [
    chrome_path,
    "--headless=new",
    f"--user-data-dir={user_data_dir}",
    "--window-size=1440,900",
    f"--screenshot={out_file}",
    "--hide-scrollbars",
    "--disable-gpu",
    "http://localhost:8080/"
]
res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
if os.path.exists(out_file):
    print(f"Success! Captured desktop_1440_animated.png ({os.path.getsize(out_file)} bytes)")
else:
    print(f"Error: {res.stderr}")

