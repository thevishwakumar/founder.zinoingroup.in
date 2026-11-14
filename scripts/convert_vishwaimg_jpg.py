import os
from PIL import Image

folder = r"founder.zinoingroup.in\assets\img\Vishwaimg"
out_folder = r"founder.zinoingroup.in\assets\img"

mapping = {
    "Screenshot_2026_1114_091424.png": "vishwa-ceo-full.jpg",
    "Screenshot_2026_1114_085830.png": "vishwa-executive-standing.jpg",
    "Screenshot_2026_1114_085759.png": "vishwa-executive-seated.jpg",
    "Screenshot_2026_1114_090009.png": "vishwa-business-strategy.jpg",
    "Screenshot_2026_1114_085900.png": "vishwa-window-skyline.jpg"
}

for src_name, dest_name in mapping.items():
    src_path = os.path.join(folder, src_name)
    dest_path = os.path.join(out_folder, dest_name)
    if os.path.exists(src_path):
        im = Image.open(src_path).convert("RGB")
        im.save(dest_path, "JPEG", quality=85, optimize=True)
        size_kb = os.path.getsize(dest_path) / 1024
        print(f"Created {dest_name}: {size_kb:.1f} KB")

