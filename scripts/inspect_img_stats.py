import os
from PIL import Image, ImageStat

folder = r"founder.zinoingroup.in\assets\img\Vishwaimg"
for fname in sorted(os.listdir(folder)):
    fpath = os.path.join(folder, fname)
    if os.path.isfile(fpath):
        im = Image.open(fpath)
        stat = ImageStat.Stat(im)
        print(f"File: {fname} | Dimensions: {im.size} | Mean RGB: {stat.mean[:3]} | Format: {im.format}")

