from pathlib import Path
from PIL import Image, ImageOps

dataset = Path("data/beethoven_data")
source = dataset / "silhouettes"
destination = dataset / "masks"

destination.mkdir(exist_ok=True)

for file in sorted(source.glob("*.pgm")):
    with Image.open(file) as img:
        mask = img.convert("L")

        # PGM: black = object
        # COLMAP: black = excluded
        mask = ImageOps.invert(mask)

        # Corresponding image: 0000.png
        # COLMAP mask: 0000.png.png
        output = destination / f"{file.stem}.png.png"
        mask.save(output)

print("Masks prepared.")