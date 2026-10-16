#!/usr/bin/env python3
"""Prépare les images du site Acoustic Detector (captures 1.2 en WebP, vignette du logo, image de partage).

Sources : ../../03-Screenshots-AppStore-1.2/{FR,EN}/*.png (captures 1242×2688 de l'app)
          ../../03-Partenaires/source/{logo.png, fonts/}
Lancer : python3 tools/prepare_assets.py   (nécessite Pillow)"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "public" / "assets" / "img"
SHOTS = HERE.parent.parent / "03-Screenshots-AppStore-1.2"
SRC = HERE.parent.parent / "03-Partenaires" / "source"
OUT.mkdir(parents=True, exist_ok=True)

KEYS = {  # clé → fichier de capture
    "menu": "01_menu", "sono": "02_sonometre", "hist": "03_historique_graphique", "calc": "04_calculateurs",
    "wall": "05_double_cloison", "freq": "06_traitement_frequences", "noise": "07_carte_bruit",
    "lidar": "08_traitement_lidar", "room3d": "09_tableau_detail_3d", "table": "11_tableau",
}

for lang in ("FR", "EN"):
    for key, name in KEYS.items():
        im = Image.open(SHOTS / lang / f"{name}.png").convert("RGB")
        im = im.resize((560, round(im.height * 560 / im.width)), Image.LANCZOS)
        im.save(OUT / f"s-{lang.lower()}-{key}.webp", "WEBP", quality=82, method=6)

logo = Image.open(HERE.parent.parent / "01-Application-Xcode" / "AcousticDetector" / "AcousticDetector" / "Resources" / "Assets.xcassets" / "AppIcon.appiconset" / "AppIcon-1024.png").convert("RGBA")
logo.resize((96, 96), Image.LANCZOS).save(OUT / "logo-mark.png")
logo.resize((180, 180), Image.LANCZOS).save(OUT.parent / "apple-touch-icon.png")
logo.resize((48, 48), Image.LANCZOS).save(OUT.parent / "favicon-48.png")
logo.resize((512, 512), Image.LANCZOS).save(OUT / "logo-large.png")


def font(name, size, wght=None):
    f = ImageFont.truetype(str(SRC / "fonts" / name), size)
    if wght:
        try:
            f.set_variation_by_axes([wght])
        except Exception:
            pass
    return f


def og(lang):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), (30, 12, 54))
    px = img.load()
    for y in range(H):  # dégradé vertical mauve
        t = y / (H - 1)
        r, g, b = int(46 - 30 * t), int(20 - 12 * t), int(80 - 48 * t)
        for x in range(W):
            px[x, y] = (r, g, b)
    d = ImageDraw.Draw(img)
    # ondes décoratives
    import math
    for k, (amp, alpha) in enumerate([(14, 90), (9, 60)]):
        pts = [(x, 598 + amp * math.sin(x / 38 + k * 2) + 8 * math.sin(x / 13 + k)) for x in range(0, W + 8, 8)]
        d.line(pts, fill=(57, 255, 20), width=2)
    # téléphone à droite
    shot = Image.open(SHOTS / lang.upper() / "06_traitement_frequences.png").convert("RGB")
    ph = 640
    pw = round(shot.width * ph / shot.height)
    shot = shot.resize((pw, ph), Image.LANCZOS)
    mask = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, pw, ph), 46, fill=255)
    px0, py0 = 800, 60
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).rounded_rectangle((px0 - 6, py0 - 6, px0 + pw + 6, py0 + ph + 6), 52, outline=(57, 255, 20, 255), width=5)
    img.paste(Image.alpha_composite(img.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(10))).convert("RGB"))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((px0 - 6, py0 - 6, px0 + pw + 6, py0 + ph + 6), 52, outline=(57, 255, 20), width=4)
    img.paste(shot, (px0, py0), mask)
    # texte
    t_small = "APP IPHONE — GRATUITE" if lang == "fr" else "IPHONE APP — FREE"
    tag = "Écoutez. Analysez. Corrigez." if lang == "fr" else "Listen. Analyze. Correct."
    foot = "Sonomètre · RT60 · Carte du bruit · LiDAR" if lang == "fr" else "Sound meter · RT60 · Noise map · LiDAR"
    d.text((64, 70), t_small, font=font("Orbitron.ttf", 22, 500), fill=(196, 180, 229))
    img.paste(logo.resize((110, 110), Image.LANCZOS), (64, 140), logo.resize((110, 110), Image.LANCZOS).split()[3])
    d.text((64, 275), "Acoustic", font=font("Orbitron.ttf", 78, 800), fill=(245, 242, 250))
    d.text((64, 365), "Detector", font=font("Orbitron.ttf", 78, 800), fill=(57, 255, 20))
    d.text((66, 455), tag, font=font("Inter.ttf", 32, 500), fill=(196, 180, 229))
    d.text((66, 508), foot, font=font("Inter.ttf", 22, 400), fill=(160, 140, 200))
    img.save(OUT / f"og-image-{lang}.png", optimize=True)


og("fr")
og("en")
print("images prêtes dans", OUT)
