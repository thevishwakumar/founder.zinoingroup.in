import subprocess, time, json, os

script = """
const puppeteer = require('puppeteer'); // if node/puppeteer was present
"""
# Since we don't use node/puppeteer, we can use headless chrome via CLI flags:
# chrome --headless=new --dump-dom --window-size=1920,1080 http://localhost:8080/
print("Checking Chrome availability...")
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

print(f"Chrome exists: {os.path.exists(chrome_path)} at {chrome_path}")
