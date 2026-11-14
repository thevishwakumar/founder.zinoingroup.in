import os

docs = [
    "PRODUCTION_DEPLOYMENT_REPORT.md",
    "LIVE_WEBSITE_VERIFICATION.md",
    "PRODUCTION_PERFORMANCE_REPORT.md",
    "ROLLBACK_GUIDE.md",
    "FINAL_PROJECT_HANDOVER.md"
]

for doc in docs:
    exists = os.path.exists(doc)
    print(f"{doc}: exists={exists}")
