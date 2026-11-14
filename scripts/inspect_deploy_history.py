for fn in ['CLOUDFLARE_DEPLOYMENT_GUIDE.md', 'DEPLOYMENT_HISTORY.md']:
    try:
        with open(fn, encoding='utf-8') as f:
            print(f"=== {fn} ===")
            print(f.read()[:2000])
    except Exception as e:
        print(f"Error {fn}: {e}")
