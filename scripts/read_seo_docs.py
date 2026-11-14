for fn in ['PERSONAL_BRAND_KEYWORD_STRATEGY.md', 'STRUCTURED_DATA_VALIDATION.md', 'GOOGLE_SEARCH_CONSOLE_GUIDE.md']:
    try:
        with open(fn, encoding='utf-8') as f:
            print(f"=== {fn} ===")
            print(f.read()[:1500])
    except Exception as e:
        print(f"Error {fn}: {e}")
