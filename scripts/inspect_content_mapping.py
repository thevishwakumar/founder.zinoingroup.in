with open('CONTENT_MAPPING.md', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if 'jotform' in line.lower() or 'web3form' in line.lower() or 'contact' in line.lower():
            print(f"{idx+1}: {line.rstrip()}")
