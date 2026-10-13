from pathlib import Path

from cairosvg import svg2png

ROOT = Path(__file__).resolve().parent.parent
ICONS_DIR = ROOT / "icons"

sizes = {
    "icon-192": (192, 192),
    "icon-512": (512, 512),
    "apple-touch-icon": (180, 180),
}

for name, size in sizes.items():
    svg_path = ICONS_DIR / f"{name}.svg"
    png_path = ICONS_DIR / f"{name}.png"
    if not svg_path.exists():
        raise FileNotFoundError(f"Missing SVG: {svg_path}")

    svg2png(url=str(svg_path), write_to=str(png_path), output_width=size[0], output_height=size[1])
    print(f"Generated {png_path}")
