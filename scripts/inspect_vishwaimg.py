import os
from PIL import Image

folder = r"founder.zinoingroup.in\assets\img\Vishwaimg"
for fname in os.listdir(folder):
    fpath = os.path.join(folder, fname)
    if os.path.isfile(fpath):
        try:
            im = Image.open(fpath)
            print(f"{fname}: format={im.format}, size={im.size}, mode={im.mode}")
        except Exception as e:
            print(f"{fname}: error {e}")

