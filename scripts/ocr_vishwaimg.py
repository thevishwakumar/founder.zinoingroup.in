try:
    import pytesseract
    from PIL import Image
    import os

    folder = r"founder.zinoingroup.in\assets\img\Vishwaimg"
    for fname in sorted(os.listdir(folder)):
        fpath = os.path.join(folder, fname)
        if os.path.isfile(fpath) and fname.endswith('.png'):
            text = pytesseract.image_to_string(Image.open(fpath))
            print(f"=== {fname} ===")
            print(text.strip())
except Exception as e:
    print(f"pytesseract error or not installed: {e}")

