for fn in ['REMAINING_OWNER_INPUT.md', 'RESUME_VERIFICATION_CHECKLIST.md']:
    try:
        with open(fn, encoding='utf-8') as f:
            print(f"=== {fn} ===")
            print(f.read()[:2000])
    except Exception as e:
        print(f"Error {fn}: {e}")
