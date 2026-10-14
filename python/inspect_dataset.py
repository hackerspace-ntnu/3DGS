from pathlib import Path
from PIL import Image
img_path = "data/beethoven_data/images"
folder = Path(img_path)
images = sorted(folder.glob("*.png"))

resolutions = set()

for path in images:
    with Image.open(path) as img:
        resolutions.add(img.size)

print("Number of images:", len(images))
print("Resolutions:", resolutions)
# This is a simple script for counting the images in a image set and identifying their resolution