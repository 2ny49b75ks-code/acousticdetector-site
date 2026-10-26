#!/usr/bin/env python3
"""Prépare les images du site Acoustic Detector (captures 1.2 en WebP, vignette du logo, image de partage).

Sources : ../../03-Screenshots-AppStore-1.2/{FR,EN}/*.png (captures 1242×2688 de l'app)
          ../../03-Partenaires/source/{logo.png, fonts/}
Lancer : python3 tools/prepare_assets.py   (nécessite Pillow)"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "public" / "assets" / "img"
ROOT = HERE.parent.parent
# langue du site → (dossier des captures 1.2/1.3, dossier des captures 1.4 / 1.4.1)
DIRS = {"fr": ("03-Screenshots-AppStore-1.2/FR", "fr"), "en": ("03-Screenshots-AppStore-1.2/EN", "en-US"),
        "es": ("03-Screenshots-AppStore-1.3/es", "es"), "de": ("03-Screenshots-AppStore-1.3/de", "de"),
        "pt": ("03-Screenshots-AppStore-1.3/pt-BR", "pt-BR"), "it": ("03-Screenshots-AppStore-1.3/it", "it"),
        "ja": ("03-Screenshots-AppStore-1.3/ja", "ja")}
SRC = HERE.parent.parent / "03-Partenaires" / "source"
OUT.mkdir(parents=True, exist_ok=True)

KEYS = {  # clé → fichier de capture
    "menu": "01_menu", "sono": "02_sonometre", "hist": "03_historique_graphique", "calc": "04_calculateurs",
    "wall": "05_double_cloison", "freq": "06_traitement_frequences", "noise": "07_carte_bruit",
    "lidar": "08_traitement_lidar", "room3d": "09_tableau_detail_3d", "table": "11_tableau",
}



def shot_file(lang, key):
    """menu et accordeur : captures les plus récentes (1.4 / 1.4.1) ; le reste : 1.2 (FR, EN) ou 1.3 (autres)."""
    base, d14 = DIRS[lang]
    if key == "menu":
        return ROOT / "03-Screenshots-AppStore-1.4" / d14 / "01_menu.png"
    if key == "tuner":
        return ROOT / "03-Screenshots-AppStore-1.4.1" / d14 / "accordeur.png"
    return ROOT / base / f"{KEYS[key]}.png"


for lang in DIRS:
    for key in list(KEYS) + ["tuner"]:
        f = shot_file(lang, key)
        if not f.exists():   # 03_historique et 09_tableau_detail_3d n'existent pas pour les langues 1.3
            continue
        im = Image.open(f).convert("RGB")
        im = im.resize((560, round(im.height * 560 / im.width)), Image.LANCZOS)
        im.save(OUT / f"s-{lang}-{key}.webp", "WEBP", quality=82, method=6)

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
    shot = Image.open(shot_file(lang, "freq")).convert("RGB")
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
    import sys
    sys.path.insert(0, str(HERE))
    from build import OG
    t_small, tag, foot = OG[lang]
    if lang == "ja":   # Orbitron et Inter n'ont pas les glyphes japonais
        ja = lambda size: ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", size)
        f_small, f_tag, f_foot = ja(24), ja(34), ja(24)
    else:
        f_small, f_tag, f_foot = font("Orbitron.ttf", 22, 500), font("Inter.ttf", 32, 500), font("Inter.ttf", 22, 400)
    d.text((64, 70), t_small, font=f_small, fill=(196, 180, 229))
    img.paste(logo.resize((110, 110), Image.LANCZOS), (64, 140), logo.resize((110, 110), Image.LANCZOS).split()[3])
    d.text((64, 275), "Acoustic", font=font("Orbitron.ttf", 78, 800), fill=(245, 242, 250))
    d.text((64, 365), "Detector", font=font("Orbitron.ttf", 78, 800), fill=(57, 255, 20))
    d.text((66, 455), tag, font=f_tag, fill=(196, 180, 229))
    d.text((66, 508), foot, font=f_foot, fill=(160, 140, 200))
    img.save(OUT / f"og-image-{lang}.png", optimize=True)


for _l in DIRS:
    og(_l)
print("images prêtes dans", OUT)
