"""Compose the hero collage from client photos: arch-topped rounded cards with soft shadows on transparency."""
import sys
from PIL import Image, ImageDraw, ImageFilter

SRC, OUT = sys.argv[1], sys.argv[2]
S = 2  # supersample for smooth edges
W, H = 1200, 940

def card_mask(w, h, r, arch):
    m = Image.new("L", (w * S, h * S), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, w * S - 1, h * S - 1], radius=r * S, fill=255)
    if arch:  # large curved top-right corner, like the original site's arch frames
        R = int(w * 0.62) * S
        d.rectangle([w * S - R, 0, w * S, R], fill=0)
        d.pieslice([w * S - 2 * R, 0, w * S, 2 * R], 270, 360, fill=255)
        d.rectangle([w * S - R, R, w * S, R + r * S], fill=255)
    return m.resize((w, h), Image.LANCZOS)

def fit(img, w, h, focus=0.22):
    iw, ih = img.size
    s = max(w / iw, h / ih)
    img = img.resize((round(iw * s), round(ih * s)), Image.LANCZOS)
    x = (img.width - w) // 2
    y = int((img.height - h) * focus)
    return img.crop((x, y, x + w, y + h))

canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
orbits = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
od = ImageDraw.Draw(orbits)
cx, cy = 595 * S, 470 * S
for r, a in ((300, 90), (440, 60), (570, 40)):
    od.ellipse([cx - r * S, cy - r * S, cx + r * S, cy + r * S], outline=(115, 90, 229, a), width=3 * S)
for (dx, dy, rr) in ((cx + 300 * S, cy - 40 * S, 9), (cx - 440 * S, cy + 120 * S, 8), (cx + 120 * S, cy + 545 * S, 7)):
    od.ellipse([dx - rr * S, dy - rr * S, dx + rr * S, dy + rr * S], fill=(115, 90, 229, 160))
canvas.alpha_composite(orbits.resize((W, H), Image.LANCZOS))
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# (file, x, y, w, h, arch, ring colour)
cards = [
    ("ig-04", 40, 110, 300, 390, True, (115, 90, 229)),
    ("ig-09", 70, 540, 270, 350, False, None),
    ("ig-05", 380, 160, 430, 610, True, None),
    ("ig-01", 850, 40, 300, 390, False, None),
    ("ig-12", 850, 470, 310, 400, True, (115, 90, 229)),
]
for name, x, y, w, h, arch, ring in cards:
    img = fit(Image.open(f"{SRC}/{name}.webp").convert("RGB"), w, h)
    m = card_mask(w, h, 34, arch)
    # shadow
    sh = Image.new("RGBA", (w, h), (20, 20, 19, 70))
    sh.putalpha(m.point(lambda v: v * 70 // 255))
    shadow.alpha_composite(sh, (x, y + 22))
    tile = img.convert("RGBA"); tile.putalpha(m)
    if ring:  # thin brand-colour outline
        ring_img = Image.new("RGBA", (w + 12, h + 12), ring + (255,))
        ring_img.putalpha(card_mask(w + 12, h + 12, 38, arch))
        canvas.alpha_composite(ring_img, (x - 6, y - 6))
    canvas.alpha_composite(tile, (x, y))

shadow = shadow.filter(ImageFilter.GaussianBlur(26))
out = Image.alpha_composite(shadow, canvas)
out.save(OUT, "WEBP", quality=88)
print(out.size)
