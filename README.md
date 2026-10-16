# Site Acoustic Detector

Site statique (FR + EN) d'Acoustic Detector, publié sur Netlify : https://acousticdetector.netlify.app

- `public/` : le site tel que publié (généré, mais versionné pour que Netlify n'ait rien à compiler)
- `tools/prepare_assets.py` : captures de l'app → WebP, logo, images de partage (nécessite Pillow)
- `tools/build.py` : génère les pages HTML à partir du texte (FR/EN) qui s'y trouve
- `netlify.toml` : indique à Netlify de publier `public/`

Mettre à jour : modifier `tools/build.py`, lancer `python3 tools/build.py`, puis commit + push (Netlify republie seul).
Pour changer la palette : variables au début de `public/assets/css/style.css`.
