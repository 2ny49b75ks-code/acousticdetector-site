#!/usr/bin/env python3
"""Génère le site Acoustic Detector (FR + EN) dans public/, sur le modèle du site SITE DIM :
fr/ et en/ (accueil, fonctionnalités, téléchargement, contact, confidentialité), assets/,
sitemap.xml, robots.txt, redirection de langue à la racine.

Les anciennes adresses (support.html, support-en.html, privacy.html, privacy-en.html, en.html) sont
conservées : elles étaient déjà publiées.

Lancer :  python3 tools/prepare_assets.py   (une fois, ou après de nouvelles captures)
          python3 tools/build.py            (après toute modification du texte), puis commit + push."""
import importlib
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parent.parent / "public"
SITE = "https://acousticdetector.netlify.app"
EMAIL = "j_david@live.ca"
APPSTORE_BASE = "https://apps.apple.com/ca/app/acoustic-detector/id6810440422"
APPSTORE = {"fr": APPSTORE_BASE + "?l=fr-CA", "en": APPSTORE_BASE + "?l=en-CA"}
LANGS = ["fr", "en", "es", "de", "pt", "it", "ja"]   # ordre du sélecteur de langue
EXTRA = ["es", "de", "pt", "it", "ja"]                # langues dont le texte est dans tools/i18n/<lang>.py
LABELS = {"fr": "FR", "en": "EN"}
HREFLANGS = {"fr": "fr", "en": "en"}
LOCALES = {"fr": "fr_CA", "en": "en_CA"}
TODAY = date.today().isoformat()

JDG_APPS = {
    "fr": '<div class="jdg-apps" style="margin-top:18px;padding-top:14px;border-top:1px solid rgba(127,127,127,.3);font-size:.88em;line-height:1.8;text-align:center"><strong>Les autres apps de JDG inc., Québec :</strong> <a href="https://camordtu.netlify.app/">CaMordTu</a> <span style="opacity:.75">(guide de pêche au Québec)</span> · <a href="https://sitedim.netlify.app/fr/index.html">SITE DIM</a> <span style="opacity:.75">(relevé de chantier en réalité augmentée)</span> · <a href="https://appmycreation.com/">MY CREATION</a> <span style="opacity:.75">(vos œuvres en relief 3D et en réalité augmentée)</span> · <a href="https://tricolab.netlify.app/fr/index.html">Tricolab</a> <span style="opacity:.75">(tricot, crochet et scrapbook)</span> · <a href="https://fortchateau.netlify.app/fr/index.html">Fort et Château</a> <span style="opacity:.75">(forts et châteaux du monde)</span></div>',
    "en": '<div class="jdg-apps" style="margin-top:18px;padding-top:14px;border-top:1px solid rgba(127,127,127,.3);font-size:.88em;line-height:1.8;text-align:center"><strong>More apps by JDG inc., Quebec:</strong> <a href="https://camordtu.netlify.app/en.html">CaMordTu</a> <span style="opacity:.75">(Quebec fishing guide)</span> · <a href="https://sitedim.netlify.app/en/index.html">SITE DIM</a> <span style="opacity:.75">(AR construction measuring)</span> · <a href="https://appmycreation.com/index-en.html">MY CREATION</a> <span style="opacity:.75">(your artwork in 3D relief and AR)</span> · <a href="https://tricolab.netlify.app/en/index.html">Tricolab</a> <span style="opacity:.75">(knitting, crochet and scrapbooking)</span> · <a href="https://fortchateau.netlify.app/en/index.html">Fort et Château</a> <span style="opacity:.75">(forts and castles of the world)</span></div>',
}

FILES = {
    "home": {"fr": "index.html", "en": "index.html"},
    "features": {"fr": "fonctionnalites.html", "en": "features.html"},
    "download": {"fr": "telechargement.html", "en": "download.html"},
    "contact": {"fr": "contact.html", "en": "contact.html"},
    "privacy": {"fr": "confidentialite.html", "en": "privacy.html"},
}
NAV_ORDER = ["home", "features", "download", "contact"]
# (fichier racine, langue, page) : anciennes adresses déjà diffusées
LEGACY = [("support.html", "fr", "contact"), ("support-en.html", "en", "contact"),
          ("privacy.html", "fr", "privacy"), ("privacy-en.html", "en", "privacy")]

T = {
    "fr": {
        "nav": {"home": "Accueil", "features": "Fonctionnalités", "download": "Téléchargement", "contact": "Contact", "privacy": "Confidentialité"},
        "cta": "Télécharger", "store": "Télécharger sur l'App Store", "menu": "Menu", "locale": "fr_CA", "alt_locale": "en_CA",
        "footer": "© 2026 JDG inc. — Québec, Canada. Acoustic Detector est une marque de JDG inc.",
        "more": "Voir les fonctionnalités",
    },
    "en": {
        "nav": {"home": "Home", "features": "Features", "download": "Download", "contact": "Contact", "privacy": "Privacy"},
        "cta": "Download", "store": "Download on the App Store", "menu": "Menu", "locale": "en_CA", "alt_locale": "fr_CA",
        "footer": "© 2026 JDG inc. — Quebec, Canada. Acoustic Detector is a trademark of JDG inc.",
        "more": "See all features",
    },
}

# ============================================================== contenu
HOME = {
    "fr": dict(
        title="Acoustic Detector — Sonomètre, RT60 et traitement acoustique",
        desc="App iPhone gratuite : sonomètre, analyseur, RT60 par bande d'octave, carte du bruit, double cloison et scan LiDAR de la pièce. Hors ligne, FR/EN.",
        eyebrow="Mesure sonore et traitement acoustique",
        h1="Écoutez. Analysez. Corrigez.",
        lead="Acoustic Detector transforme votre iPhone en outil d'acoustique. Mesurez le bruit, analysez le spectre, scannez une pièce au LiDAR, puis découvrez où elle résonne et combien de mousse acoustique ajouter. Gratuite, 100 % hors ligne, en 7 langues.",
        meta=[("iOS 17+", "requis"), ("", "iPhone"), ("7 langues", "FR · EN · ES · DE · PT · IT · JA"), ("Gratuite", "achat unique facultatif")],
        hero_alt="Réverbération d'une pièce par bande d'octave, comparée à la cible de 0,50 seconde",
        new_badge="Nouveauté", new_h="Version 1.4.1 : un accordeur gratuit, plus stable et plus précis",
        new_lead="Acoustic Detector ajoute un accordeur gratuit pour guitare, ukulélé, violon et plus, et parle maintenant français, anglais, espagnol, allemand, portugais, italien et japonais.",
        new=["Accordeur gratuit : guitare (5 accordages), ukulélé, violon, alto, violoncelle, mandoline, banjo, et mode chromatique pour la voix",
             "Version 1.4.1 : lecture plus stable qui ignore les mesures aberrantes, aiguille plus précise, indicateur du niveau du signal, ukulélé baryton",
             "Notes en Do Ré Mi ou en C D E selon la langue, aiguille précise, vibration quand c'est juste",
             "7 langues, au choix dans le menu principal",
             "Version 1.2 : le RT60 par bande d'octave, de 125 Hz à 4 kHz, avec votre cible",
             "Absorption des matériaux : la courbe de chaque surface de la pièce",
             "Cartographie du bruit : mesurez à plusieurs endroits et obtenez une carte de chaleur",
             "Double cloison : fréquence de résonance et isolement par fréquence",
             "L'app est gratuite : sonomètre, analyseur, tableau des mesures et export PDF inclus ; Traitement et Calculateurs avec un achat unique"],
        new_status="Version 1.4.1 disponible sur l'App Store.",
        callout="<p><strong>Un outil indicatif, honnêtement présenté.</strong> Le micro de l'iPhone n'est pas un instrument certifié : les valeurs affichées sont des estimations, clairement identifiées comme telles, avec un étalonnage manuel facultatif pour affiner la précision. Acoustic Detector ne remplace pas un instrument calibré pour une conformité réglementaire officielle.</p>",
        what_eyebrow="Ce que fait Acoustic Detector", what_h="Un seul appareil pour mesurer et corriger",
        what=[("Sonomètre en direct", "Niveau en dB en temps réel, avec minimum, moyenne et maximum, étalonnage du micro et historique en couleurs.", ""),
              ("Analyseur de spectre", "Analyse des fréquences en direct, avec détection d'un son pur : fréquence, période et longueur d'onde.", ""),
              ("Traitement d'une pièce", "Le temps de réverbération (RT60) comparé à la cible de votre usage, et la quantité de mousse acoustique à ajouter.", ""),
              ("Scan LiDAR", "Sur iPhone Pro, balayez la pièce : dimensions et surface de chaque mur se remplissent toutes seules.", ""),
              ("Carte du bruit", "Mesurez le niveau à plusieurs endroits et repérez les zones calmes et bruyantes sur une carte de chaleur.", ""),
              ("Accordeur", "Guitare, ukulélé, violon, alto, violoncelle, mandoline, banjo, ou n'importe quelle note et votre voix : l'aiguille et les cents en direct.", "Nouveau"),
              ("Calculateurs", "Somme de sources sonores, pression acoustique, fréquence et longueur d'onde, et calcul de double cloison.", "")],
        shots_eyebrow="Aperçu", shots_h="Sobre, précis, prêt pour le terrain",
        shots=[("menu", "Menu principal", "Menu"), ("tuner", "Accordeur de guitare avec aiguille et cents", "Accordeur"), ("sono", "Sonomètre et étalonnage du micro", "Sonomètre"),
               ("freq", "Réverbération par fréquence et absorption des matériaux", "RT60 par fréquence"),
               ("noise", "Carte de chaleur du bruit d'une pièce", "Carte du bruit"), ("wall", "Calcul de double cloison", "Double cloison"),
               ("lidar", "Scan de pièce par LiDAR", "Scan LiDAR"), ("table", "Tableau des mesures", "Tableau")],
        who_eyebrow="Pour qui", who_h="Du chantier au studio",
        who=[("Entrepreneurs et techniciens", "Mesurez le bruit d'un lieu, vérifiez une cloison, estimez le traitement d'une pièce avant de soumissionner."),
             ("Studios, musiciens, audio", "Calculez la réverbération d'une salle, repérez les graves problématiques, estimez la mousse à ajouter."),
             ("Maison et bureau", "Cinéma maison, bureau à la maison, salle de réunion : trouvez où ça résonne et quoi y faire.")],
        nums=[("5", "Modes de mesure"), ("6", "Bandes d'octave"), ("10", "Matériaux acoustiques"), ("100 %", "Hors ligne")],
        price_eyebrow="Prix", price_h="Gratuite, avec un achat unique facultatif",
        plans=[("Gratuit", "0 $", ["Sonomètre en direct et étalonnage", "Analyseur de spectre", "Accordeur (guitare, violon, voix et plus)", "Tableau des mesures", "Export PDF avec graphiques"], False),
               ("Complet", "4,99 $ CA, achat unique", ["Tout le gratuit", "Traitement : RT60, absorption, scan LiDAR, carte du bruit", "Calculateurs : sources, pression, ondes, double cloison", "Pas d'abonnement"], True)],
        price_note="Le prix est affiché par l'App Store selon votre pays. Si vous aviez acheté l'app avant qu'elle devienne gratuite, tout reste débloqué automatiquement.",
        cta_h="Prêt à écouter votre pièce ?", cta_p="Acoustic Detector est disponible sur l'App Store, pour iPhone. Gratuite, avec un achat unique facultatif.",
    ),
    "en": dict(
        title="Acoustic Detector — Sound Meter, RT60 and Room Acoustics",
        desc="Free iPhone app: sound meter, spectrum analyzer, RT60 by octave band, noise map, double-wall calculator and LiDAR room scan. Works offline, EN/FR.",
        eyebrow="Sound measurement and acoustic treatment",
        h1="Listen. Analyze. Correct.",
        lead="Acoustic Detector turns your iPhone into an acoustics toolkit. Measure noise, analyze the spectrum, scan a room with LiDAR, then find out where it resonates and how much acoustic foam to add. Free, 100% offline, in 7 languages.",
        meta=[("iOS 17+", "required"), ("", "iPhone"), ("7 languages", "EN · FR · ES · DE · PT · IT · JA"), ("Free", "optional one-time purchase")],
        hero_alt="A room's reverberation by octave band, compared with the 0.50-second target",
        new_badge="What's new", new_h="Version 1.4.1: a free tuner, more stable and more precise",
        new_lead="Acoustic Detector adds a free tuner for guitar, ukulele, violin and more, and now speaks English, French, Spanish, German, Portuguese, Italian and Japanese.",
        new=["Free tuner: guitar (5 tunings), ukulele, violin, viola, cello, mandolin, banjo, and a chromatic mode for voice",
             "Version 1.4.1: a steadier reading that ignores stray measurements, a more precise needle, a signal level meter, baritone ukulele",
             "Note names as Do Re Mi or C D E depending on the language, a precise needle, a vibration when in tune",
             "7 languages, selectable from the main menu",
             "Version 1.2: RT60 per octave band, from 125 Hz to 4 kHz, against your target",
             "Material absorption: the curve of every surface in the room",
             "Noise map: measure at several spots and get a heat map",
             "Double wall: resonance frequency and insulation by frequency",
             "The app is free: sound meter, analyzer, measurements table and PDF export included; Treatment and Calculators with a one-time purchase"],
        new_status="Version 1.4.1 available on the App Store.",
        callout="<p><strong>An indicative tool, honestly presented.</strong> The iPhone's microphone is not a certified instrument: values shown are estimates, clearly labeled as such, with optional manual calibration to sharpen accuracy. Acoustic Detector does not replace a calibrated instrument for official regulatory compliance.</p>",
        what_eyebrow="What Acoustic Detector does", what_h="One device to measure and correct",
        what=[("Live sound meter", "Real-time dB level with minimum, average and maximum, microphone calibration and a color-coded history.", ""),
              ("Spectrum analyzer", "Live frequency analysis with pure-tone detection: frequency, period and wavelength.", ""),
              ("Room treatment", "Reverberation time (RT60) against the target for your use case, and how much acoustic foam to add.", ""),
              ("LiDAR scan", "On iPhone Pro, sweep the room: dimensions and the area of every wall fill in by themselves.", ""),
              ("Noise map", "Measure the level at several spots and see the calm and noisy zones on a heat map.", ""),
              ("Tuner", "Guitar, ukulele, violin, viola, cello, mandolin, banjo, or any note and your voice: a needle and live cents.", "New"),
              ("Calculators", "Sum of sound sources, sound pressure, frequency and wavelength, and a double-wall calculator.", "")],
        shots_eyebrow="Preview", shots_h="Clean, precise, ready for the field",
        shots=[("menu", "Main menu", "Menu"), ("tuner", "Guitar tuner with needle and cents", "Tuner"), ("sono", "Sound meter and mic calibration", "Sound meter"),
               ("freq", "Reverberation by frequency and material absorption", "RT60 by frequency"),
               ("noise", "Noise heat map of a room", "Noise map"), ("wall", "Double-wall calculator", "Double wall"),
               ("lidar", "LiDAR room scan", "LiDAR scan"), ("table", "Measurements table", "Table")],
        who_eyebrow="Who it's for", who_h="From the job site to the studio",
        who=[("Contractors and technicians", "Measure a site's noise, check a partition, estimate a room's treatment before you quote."),
             ("Studios, musicians, audio", "Calculate a room's reverberation, spot the problem bass frequencies, estimate the foam to add."),
             ("Home and office", "Home theater, home office, meeting room: find where it resonates and what to do about it.")],
        nums=[("5", "Measurement modes"), ("6", "Octave bands"), ("10", "Acoustic materials"), ("100%", "Offline")],
        price_eyebrow="Price", price_h="Free, with one optional purchase",
        plans=[("Free", "$0", ["Live sound meter and calibration", "Spectrum analyzer", "Tuner (guitar, violin, voice and more)", "Measurements table", "PDF export with charts"], False),
               ("Complete", "CA$4.99, one-time purchase", ["Everything in Free", "Treatment: RT60, absorption, LiDAR scan, noise map", "Calculators: sources, pressure, waves, double wall", "No subscription"], True)],
        price_note="The price is shown by the App Store for your country. If you bought the app before it became free, everything stays unlocked automatically.",
        cta_h="Ready to listen to your room?", cta_p="Acoustic Detector is available on the App Store, for iPhone. Free, with one optional purchase.",
    ),
}

FEATURES = {
    "fr": dict(
        title="Fonctionnalités — Acoustic Detector",
        desc="Sonomètre, analyseur, RT60 par bande d'octave, absorption, carte du bruit, scan LiDAR, double cloison et rapports PDF : tout ce que fait Acoustic Detector.",
        eyebrow="Fonctionnalités", h1="Tout ce qu'il faut pour mesurer et corriger une pièce",
        lead="Le micro et la caméra de l'iPhone, utilisés pour mesurer, calculer et documenter l'acoustique d'un lieu — sans quitter l'application, sans connexion.",
        m_eyebrow="Mesurer", m_h="Gratuit : de quoi mesurer au quotidien",
        measure=[("Sonomètre en direct", "Niveau en dB en temps réel, avec minimum, moyenne et maximum, et deux styles de graphique (Festival, Studio)."),
                 ("Étalonnage du micro", "Comparez avec un sonomètre de référence et ajustez : chaque mesure indique si elle est étalonnée ou estimée."),
                 ("Analyseur de spectre", "Analyse des fréquences en direct (FFT) et classification du son : pur, complexe ou bruit."),
                 ("Son pur", "Pour un son pur, la fréquence, la période et la longueur d'onde sont calculées pour vous."),
                 ("Historique en couleurs", "Chaque session s'enregistre avec sa courbe : vert, jaune ou rouge selon le niveau."),
                 ("Tableau des mesures", "Le journal de toutes vos mesures, avec filtre, tri et export en rapport PDF avec graphiques.")],
        s_eyebrow="En détail", s_h="Chaque outil, de près",
        spots=[
            ("tuner", "Accordeur", "Accordez à l'oreille, ou laissez l'aiguille faire le travail.",
             ["Guitare (5 accordages), ukulélé (dont Sol grave et baryton), violon, alto, violoncelle, mandoline et banjo", "Mode chromatique pour la voix et n'importe quelle note", "Aiguille avec cents en direct et réglette de précision de ±10 cents, vibration quand c'est juste", "Lecture stabilisée qui ignore les mesures aberrantes, avec indicateur du niveau du signal", "Fréquence de référence réglable de 430 à 450 Hz, et gratuit"]),
            ("sono", "Sonomètre, étalonnage et historique", "Le sonomètre le plus simple à ouvrir sur le terrain.",
             ["Niveau en direct, minimum, moyenne et maximum", "Étalonnage du micro sur un instrument de référence, avec l'état d'étalonnage noté sur chaque mesure", "Historique des sessions avec leur courbe en couleurs", "Partage de l'image ou ajout au tableau des mesures"]),
            ("freq", "Réverbération par fréquence", "Savoir où la pièce pose problème, pas seulement si elle en pose un.",
             ["RT60 par bande d'octave, de 125 Hz à 4 kHz, comparé à la cible de votre usage (bureau, studio, salle de réunion, cinéma maison)", "Les bandes au-dessus de la cible sont signalées, avec un conseil pour les graves", "Courbes d'absorption de chaque matériau de la pièce, parmi 10 matériaux", "Modèle de Sabine et coefficients typiques : une estimation indicative"]),
            ("lidar", "Du scan à la mousse à ajouter", "Scannez la pièce, laissez l'app faire les calculs.",
             ["Sur iPhone Pro (LiDAR), un balayage remplit les dimensions et la surface de chaque mur", "Sans LiDAR, entrez les dimensions à la main : tout le reste fonctionne", "Schéma 3D isométrique de la pièce, repris dans le tableau et le rapport PDF", "La quantité de mousse acoustique à ajouter pour atteindre la cible", "Mesure du RT60 en direct avec une courte salve de bruit"]),
            ("noise", "Cartographie du bruit", "Voir où ça fait du bruit dans une pièce, d'un coup d'œil.",
             ["Touchez le plan de la pièce et mesurez cinq secondes à chaque endroit", "Carte de chaleur des zones calmes et bruyantes", "Niveau le plus calme, moyenne (Leq) et niveau le plus bruyant", "Enregistrée au tableau des mesures et dans le rapport PDF"]),
            ("calc", "Calculateurs acoustiques", "Les formules du métier, sans papier ni calculatrice.",
             ["Somme de sources sonores : combien de dB ensemble", "Niveau de pression acoustique à partir de la pression en pascals", "Fréquence, période et longueur d'onde", "Chaque résultat s'ajoute au tableau en un toucher"]),
            ("wall", "Double cloison", "Estimer l'isolement d'une paroi avant de la construire.",
             ["Calcul masse-ressort-masse à partir de la masse de chaque paroi et de la profondeur de la cavité", "Fréquence de résonance et isolement par bande d'octave", "Avec ou sans laine minérale, et parois désolidarisées en option", "Estimation indicative, pas un indice Rw/STC certifié"]),
            ("table", "Tableau des mesures et rapports PDF", "Tout ce que vous mesurez reste rangé et se partage.",
             ["Chaque mesure s'ajoute à un tableau central, filtrable par type", "Rapport PDF avec graphiques et schéma 3D de la pièce", "Enregistrement d'un graphique dans Photos, ou partage par les outils d'iOS", "Tout reste sur votre appareil : aucun compte, aucun serveur"]),
        ],
        cmp_h="Gratuit ou Acoustic Detector Complet", cmp_cols=("", "Gratuit", "Complet"),
        cmp=[("Sonomètre en direct et étalonnage", "✓", "✓"), ("Analyseur de spectre", "✓", "✓"), ("Accordeur", "✓", "✓"), ("Tableau des mesures et export PDF", "✓", "✓"),
             ("RT60 de la pièce et mousse à ajouter", "—", "✓"), ("RT60 par bande d'octave et absorption", "—", "✓"), ("Scan LiDAR de la pièce", "—", "✓"),
             ("Cartographie du bruit", "—", "✓"), ("Calculateurs et double cloison", "—", "✓")],
        cmp_note="« Acoustic Detector Complet » est un achat unique de 4,99 $ CA, sans abonnement.",
    ),
    "en": dict(
        title="Features — Acoustic Detector",
        desc="Sound meter, analyzer, RT60 by octave band, absorption, noise map, LiDAR scan, double-wall calculator and PDF reports: everything Acoustic Detector does.",
        eyebrow="Features", h1="Everything you need to measure and correct a room",
        lead="The iPhone's microphone and camera, used to measure, calculate and document a space's acoustics — without leaving the app, without a connection.",
        m_eyebrow="Measure", m_h="Free: what you need to measure every day",
        measure=[("Live sound meter", "Real-time dB level with minimum, average and maximum, and two chart styles (Festival, Studio)."),
                 ("Microphone calibration", "Compare with a reference meter and adjust: every measurement says whether it is calibrated or estimated."),
                 ("Spectrum analyzer", "Live frequency analysis (FFT) and sound classification: pure tone, complex or noise."),
                 ("Pure tone", "For a pure tone, frequency, period and wavelength are calculated for you."),
                 ("Color-coded history", "Each session is saved with its curve: green, yellow or red depending on the level."),
                 ("Measurements table", "A log of everything you measure, with filter, sort and export to a PDF report with charts.")],
        s_eyebrow="In detail", s_h="Every tool, up close",
        spots=[
            ("tuner", "Tuner", "Tune by ear, or let the needle do the work.",
             ["Guitar (5 tunings), ukulele (including low-G and baritone), violin, viola, cello, mandolin and banjo", "Chromatic mode for voice and any note", "A needle with live cents and a ±10-cent fine-tuning strip, with a vibration when in tune", "A steadied reading that ignores stray measurements, with a signal level meter", "Reference pitch adjustable from 430 to 450 Hz, and free"]),
            ("sono", "Sound meter, calibration and history", "The simplest sound meter to open in the field.",
             ["Live level, minimum, average and maximum", "Microphone calibration against a reference instrument, with the calibration state noted on every measurement", "Session history with its color-coded curve", "Share the image or add it to the measurements table"]),
            ("freq", "Reverberation by frequency", "Know where the room has a problem, not just whether it has one.",
             ["RT60 per octave band, from 125 Hz to 4 kHz, against the target for your use case (office, studio, meeting room, home theater)", "Bands above the target are flagged, with a tip for the bass", "Absorption curves for every material in the room, from 10 materials", "Sabine model and typical coefficients: an indicative estimate"]),
            ("lidar", "From scan to foam to add", "Scan the room, let the app do the math.",
             ["On iPhone Pro (LiDAR), one sweep fills in the dimensions and the area of every wall", "Without LiDAR, enter the dimensions by hand: everything else works", "3D isometric room diagram, carried into the table and the PDF report", "How much acoustic foam to add to reach the target", "Live RT60 measurement with a short noise burst"]),
            ("noise", "Noise map", "See where a room is noisy at a glance.",
             ["Tap the room plan and measure five seconds at each spot", "Heat map of the calm and noisy zones", "Quietest level, average (Leq) and loudest level", "Saved to the measurements table and the PDF report"]),
            ("calc", "Acoustic calculators", "The trade's formulas, with no paper or calculator.",
             ["Sum of sound sources: how many dB together", "Sound pressure level from pressure in pascals", "Frequency, period and wavelength", "Every result is added to the table with one tap"]),
            ("wall", "Double wall", "Estimate a partition's insulation before you build it.",
             ["Mass-spring-mass calculation from each leaf's mass and the cavity depth", "Resonance frequency and insulation per octave band", "With or without mineral wool, and decoupled leaves as an option", "Indicative estimate, not a certified Rw/STC rating"]),
            ("table", "Measurements table and PDF reports", "Everything you measure stays organized and shareable.",
             ["Every measurement is added to a central table, filterable by type", "PDF report with charts and the room's 3D diagram", "Save a chart to Photos, or share it with iOS's tools", "Everything stays on your device: no account, no server"]),
        ],
        cmp_h="Free or Acoustic Detector Complete", cmp_cols=("", "Free", "Complete"),
        cmp=[("Live sound meter and calibration", "✓", "✓"), ("Spectrum analyzer", "✓", "✓"), ("Tuner", "✓", "✓"), ("Measurements table and PDF export", "✓", "✓"),
             ("Room RT60 and foam to add", "—", "✓"), ("RT60 per octave band and absorption", "—", "✓"), ("LiDAR room scan", "—", "✓"),
             ("Noise map", "—", "✓"), ("Calculators and double wall", "—", "✓")],
        cmp_note="\"Acoustic Detector Complete\" is a one-time CA$4.99 purchase, with no subscription.",
    ),
}

DOWNLOAD = {
    "fr": dict(
        title="Téléchargement — Acoustic Detector",
        desc="Téléchargez Acoustic Detector sur l'App Store pour iPhone. Gratuite, avec un achat unique facultatif.",
        eyebrow="Téléchargement", h1="Acoustic Detector sur l'App Store",
        lead="Une application native iOS, conçue pour être utilisée directement sur le terrain : au chantier, au studio ou à la maison.",
        req_eyebrow="Configuration requise", req_h="Vérifiez la compatibilité de votre appareil",
        specs=[("Système", "iOS 17+"), ("Appareil", "iPhone"), ("Prix", "Gratuite"), ("Achat unique", "4,99 $ CA")],
        req_note="Acoustic Detector fonctionne sur tout iPhone sous iOS 17 ou plus récent. Le scan de pièce par LiDAR demande un iPhone Pro équipé d'un capteur LiDAR (iPhone 12 Pro et plus récent) ; sur les autres iPhone, les dimensions de la pièce s'entrent à la main.",
        sheet_eyebrow="Fiche technique", sheet_h="Informations sur l'application",
        sheet=[("Éditeur", "JDG inc., Québec, Canada"), ("Identifiant", "JDG-inc.AcousticDetector"), ("Langues", "Français, anglais, espagnol, allemand, portugais (Brésil), italien, japonais"), ("Exports", "Rapport PDF avec graphiques, partage d'image")],
        faq_eyebrow="Questions fréquentes", faq_h="Avant de télécharger",
        faq=[("Mon appareil est-il compatible ?", "Si votre iPhone tourne sous iOS 17 ou plus récent, il est compatible. Le LiDAR n'est pas requis : il ajoute seulement le scan automatique de la pièce."),
             ("Combien ça coûte ?", "L'app est gratuite. L'achat unique facultatif « Acoustic Detector Complet » (4,99 $ CA) débloque Traitement et Calculateurs, sans abonnement."),
             ("L'application fonctionne-t-elle hors ligne ?", "Oui. Les mesures et les calculs se font sur l'appareil, sans compte ni serveur. Seuls l'achat et la restauration passent par l'App Store."),
             ("Les mesures sont-elles précises ?", "Le micro de l'iPhone donne une estimation, pas une mesure certifiée. Un étalonnage manuel facultatif permet d'affiner le résultat."),
             ("Dans quelle langue ?", "En français, anglais, espagnol, allemand, portugais (Brésil), italien et japonais, au choix dans le menu principal."),
             ("Comment obtenir de l'aide ?", f'Écrivez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a> ou consultez la page <a href="contact.html">Contact</a>.')],
        cta_h="Prêt à commencer ?", cta_p="Acoustic Detector est disponible sur l'App Store.",
    ),
    "en": dict(
        title="Download — Acoustic Detector",
        desc="Download Acoustic Detector on the App Store for iPhone. Free, with one optional purchase.",
        eyebrow="Download", h1="Acoustic Detector on the App Store",
        lead="A native iOS app, built to be used right in the field: on the job site, in the studio or at home.",
        req_eyebrow="Requirements", req_h="Check your device's compatibility",
        specs=[("System", "iOS 17+"), ("Device", "iPhone"), ("Price", "Free"), ("One-time purchase", "CA$4.99")],
        req_note="Acoustic Detector runs on any iPhone with iOS 17 or later. The LiDAR room scan needs an iPhone Pro with a LiDAR sensor (iPhone 12 Pro and later); on other iPhones, you enter the room's dimensions by hand.",
        sheet_eyebrow="Technical sheet", sheet_h="App information",
        sheet=[("Publisher", "JDG inc., Quebec, Canada"), ("Identifier", "JDG-inc.AcousticDetector"), ("Languages", "English, French, Spanish, German, Portuguese (Brazil), Italian, Japanese"), ("Exports", "PDF report with charts, image sharing")],
        faq_eyebrow="Frequently asked questions", faq_h="Before you download",
        faq=[("Is my device compatible?", "If your iPhone runs iOS 17 or later, it is compatible. LiDAR is not required: it only adds the automatic room scan."),
             ("How much does it cost?", "The app is free. The optional one-time \"Acoustic Detector Complete\" purchase (CA$4.99) unlocks Treatment and Calculators, with no subscription."),
             ("Does it work offline?", "Yes. Measurements and calculations happen on the device, with no account or server. Only the purchase and restore go through the App Store."),
             ("Are the measurements accurate?", "The iPhone's microphone gives an estimate, not a certified measurement. Optional manual calibration lets you sharpen the result."),
             ("Which languages?", "English, French, Spanish, German, Portuguese (Brazil), Italian and Japanese, selectable from the main menu."),
             ("How do I get help?", f'Email us at <a href="mailto:{EMAIL}">{EMAIL}</a> or visit the <a href="contact.html">Contact</a> page.')],
        cta_h="Ready to start?", cta_p="Acoustic Detector is available on the App Store.",
    ),
}

CONTACT = {
    "fr": dict(
        title="Contact et assistance — Acoustic Detector", desc="Aide, questions fréquentes, achat et restauration, presse : écrivez-nous au sujet de l'app Acoustic Detector. Chaque message reçoit une réponse.",
        eyebrow="Contact", h1="Contact et assistance",
        lead="Une question, un bogue à signaler ou une suggestion ? Chaque message est lu et reçoit une réponse personnelle.",
        blocks=[("Assistance et questions", "Précisez si possible votre modèle d'iPhone et votre version d'iOS.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector">{EMAIL}</a>'),
                ("Presse et médias", "Un dossier de presse (présentation, fonctionnalités, fiche technique) est disponible en français et en anglais sur demande.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector%20-%20Presse">{EMAIL}</a>'),
                ("Éditeur", "Acoustic Detector est conçue et développée par JDG inc.", "JDG inc. — Québec, Canada"),
                ("Application", "Disponible sur l'App Store pour iPhone sous iOS 17+.", '<a href="telechargement.html">Voir la page de téléchargement</a>')],
        faq_h="Questions fréquentes",
        faq=[("Les mesures en décibels sont-elles calibrées ?", "Non, pas par défaut. Acoustic Detector utilise le microphone intégré de l'iPhone pour estimer le niveau sonore — c'est indicatif, pas un instrument certifié. Le mode Sonomètre offre un étalonnage manuel optionnel contre un instrument de référence pour ajuster la précision."),
             ("Le scan de pièce par LiDAR fonctionne-t-il sur tous les iPhone ?", "Non, seulement sur les modèles Pro équipés d'un capteur LiDAR (iPhone 12 Pro et plus récent). Sur les autres iPhone, les dimensions de la pièce s'entrent manuellement dans le mode Traitement — toutes les fonctionnalités de calcul restent disponibles."),
             ("Le calcul de réverbération (RT60) est-il exact ?", "Le mode Traitement offre deux estimations : un calcul théorique (formule de Sabine, basé sur vos dimensions et matériaux, par bande d'octave) et une mesure en direct par salve de bruit. Les deux sont des approximations utiles pour orienter un traitement acoustique, pas des mesures de laboratoire."),
             ("Mes mesures sont-elles envoyées quelque part ?", 'Non. Aucune donnée ne quitte votre appareil. Voir notre <a href="confidentialite.html">politique de confidentialité</a>.'),
             ("L'app est-elle offerte en anglais et dans d'autres langues ?", "Oui. Acoustic Detector parle 7 langues (français, anglais, espagnol, allemand, portugais, italien et japonais) — un bouton de langue dans le menu principal bascule l'interface, indépendamment de la langue réglée sur votre iPhone."),
             ("Y a-t-il un abonnement ?", "Non. Acoustic Detector se télécharge gratuitement : le sonomètre, l'analyseur, l'accordeur, le tableau des mesures et l'export PDF sont inclus. Traitement et Calculateurs se débloquent avec un achat unique (4,99 $ CA), sans abonnement. Les mises à jour sont incluses. Si vous aviez acheté l'app avant qu'elle devienne gratuite, tout reste débloqué automatiquement."),
             ("Comment restaurer mon achat ?", "Sur un nouvel iPhone ou après une réinstallation, ouvrez Traitement ou Calculateurs et touchez « Restaurer mes achats », avec le même identifiant Apple que pour l'achat."),
             ("L'app existe-t-elle sur Android ?", "Pas pour l'instant — Acoustic Detector est offerte sur iPhone (iOS 17 ou plus récent).")],
        cta_h="Une question avant de télécharger ?", cta_p="Écrivez-nous — on répond directement, sans détour.",
    ),
    "en": dict(
        title="Contact and support — Acoustic Detector", desc="Help, FAQ, purchase and restore, press: write to us about the Acoustic Detector app. Every message gets a reply.",
        eyebrow="Contact", h1="Contact and support",
        lead="A question, a bug to report or a suggestion? Every message is read and gets a personal reply.",
        blocks=[("Support and questions", "If you can, tell us your iPhone model and your iOS version.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector">{EMAIL}</a>'),
                ("Press and media", "A bilingual press kit (overview, features, technical sheet) is available on request.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector%20-%20Press">{EMAIL}</a>'),
                ("Publisher", "Acoustic Detector is designed and developed by JDG inc.", "JDG inc. — Quebec, Canada"),
                ("App", "Available on the App Store for iPhone with iOS 17+.", '<a href="download.html">See the download page</a>')],
        faq_h="Frequently asked questions",
        faq=[("Are the decibel readings calibrated?", "Not by default. Acoustic Detector uses the iPhone's built-in microphone to estimate the sound level — it is indicative, not a certified instrument. The Sound Meter mode offers optional manual calibration against a reference instrument to fine-tune accuracy."),
             ("Does the LiDAR room scan work on every iPhone?", "No, only on Pro models with a LiDAR sensor (iPhone 12 Pro and later). On other iPhones, you enter the room's dimensions manually in Treatment mode — every calculation feature remains available."),
             ("Is the reverberation (RT60) calculation exact?", "Treatment mode offers two estimates: a theoretical calculation (Sabine formula, based on your dimensions and materials, per octave band) and a live measurement using a noise burst. Both are useful approximations to guide acoustic treatment, not laboratory measurements."),
             ("Are my measurements sent anywhere?", 'No. No data ever leaves your device. See our <a href="privacy.html">privacy policy</a>.'),
             ("Is the app available in French and other languages?", "Yes. Acoustic Detector speaks 7 languages (English, French, Spanish, German, Portuguese, Italian and Japanese) — a language button in the main menu switches the interface, independently of your iPhone's language."),
             ("Is there a subscription?", "No. Acoustic Detector is free to download: the sound meter, analyzer, tuner, measurements table and PDF export are included. Treatment and Calculators unlock with a one-time purchase (CA$4.99), no subscription. Updates are included. If you bought the app before it became free, everything stays unlocked automatically."),
             ("How do I restore my purchase?", "On a new iPhone or after reinstalling, open Treatment or Calculators and tap “Restore Purchases”, using the same Apple ID as for the purchase."),
             ("Is the app available on Android?", "Not at the moment — Acoustic Detector is available on iPhone (iOS 17 or later).")],
        cta_h="A question before you download?", cta_p="Write to us — we answer directly, no detours.",
    ),
}

PRIVACY = {
    "fr": dict(
        title="Politique de confidentialité — Acoustic Detector", desc="Acoustic Detector ne collecte, ne transmet et ne partage aucune donnée personnelle : aucun compte, aucun serveur, aucun traceur.",
        eyebrow="Confidentialité", h1="Politique de confidentialité", updated="Dernière mise à jour : 2 octobre 2026",
        note="<p><strong>En résumé :</strong> Acoustic Detector ne collecte, ne transmet et ne partage aucune donnée personnelle. L'app fonctionne entièrement hors ligne, sans compte, sans serveur et sans service tiers.</p>",
        sections=[
            ("Microphone", "<p>L'app utilise le microphone de votre appareil pour les fonctions Sonomètre, Analyseur et la mesure de réverbération (RT60) du mode Traitement. Le son capté est traité entièrement sur votre appareil, en temps réel, pour calculer un niveau sonore ou un spectre de fréquences. Aucun enregistrement audio n'est sauvegardé, transmis ou partagé — seules les valeurs numériques calculées (dB, Hz, secondes) peuvent être enregistrées localement si vous choisissez d'ajouter une mesure au tableau.</p>"),
            ("Caméra et LiDAR", "<p>Sur les iPhone Pro, le mode Traitement offre un scan de pièce optionnel par caméra et LiDAR (via RoomPlan et ARKit d'Apple) pour mesurer automatiquement les dimensions d'une pièce. Ce scan est traité entièrement sur votre appareil — aucune image, vidéo ou donnée de scan n'est envoyée où que ce soit. Seules les dimensions et superficies calculées sont conservées, localement, si vous choisissez de les utiliser.</p>"),
            ("Données enregistrées localement", "<p>Les mesures que vous choisissez de sauvegarder (sessions du Sonomètre, entrées du tableau des mesures) sont stockées uniquement dans l'espace de stockage privé de l'app sur votre appareil. Ces données ne quittent jamais votre appareil, sauf si vous choisissez explicitement de les exporter (rapport PDF, partage d'image) via les fonctions natives de partage d'iOS — vous contrôlez alors vous-même la destination.</p>"),
            ("Photothèque", "<p>Si vous choisissez d'enregistrer un graphique ou un rapport dans votre photothèque, l'app demande une autorisation d'ajout limitée à cette seule action. Elle ne consulte pas et n'accède pas au reste de votre photothèque.</p>"),
            ("Achat intégré", "<p>Traitement et Calculateurs se débloquent avec un achat unique, traité entièrement par Apple (App Store). Le développeur ne reçoit ni vos informations de paiement ni votre identité : l'app demande seulement à Apple si l'achat est actif sur votre identifiant Apple.</p>"),
            ("Aucun suivi, aucun tiers", "<ul><li>Aucun compte utilisateur, aucune identification requise.</li><li>Aucun serveur distant ; aucune connexion n'est requise pour utiliser l'app (seuls l'achat et la restauration passent par l'App Store).</li><li>Aucun outil d'analyse, de publicité ou de suivi tiers n'est intégré à l'app.</li><li>Aucune donnée n'est vendue, partagée ou monétisée de quelque façon que ce soit.</li></ul>"),
            ("Contact", f'<p>Pour toute question relative à cette politique de confidentialité, écrivez-nous à <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
        ]),
    "en": dict(
        title="Privacy policy — Acoustic Detector", desc="Acoustic Detector does not collect, transmit or share any personal data: no account, no server, no trackers.",
        eyebrow="Privacy", h1="Privacy policy", updated="Last updated: October 2, 2026",
        note="<p><strong>In short:</strong> Acoustic Detector does not collect, transmit, or share any personal data. The app works entirely offline, with no account, no server, and no third-party service.</p>",
        sections=[
            ("Microphone", "<p>The app uses your device's microphone for the Sound Meter, Spectrum Analyzer, and the reverberation (RT60) measurement in Room Treatment mode. Captured sound is processed entirely on your device, in real time, to compute a sound level or frequency spectrum. No audio recording is ever saved, transmitted, or shared — only the calculated numeric values (dB, Hz, seconds) may be saved locally if you choose to add a measurement to the table.</p>"),
            ("Camera and LiDAR", "<p>On iPhone Pro models, Room Treatment offers an optional camera and LiDAR room scan (via Apple's RoomPlan and ARKit) to automatically measure a room's dimensions. This scan is processed entirely on your device — no image, video, or scan data is ever sent anywhere. Only the calculated dimensions and surface areas are kept, locally, if you choose to use them.</p>"),
            ("Locally saved data", "<p>Measurements you choose to save (Sound Meter sessions, entries in the measurement table) are stored only in the app's private storage on your device. This data never leaves your device unless you explicitly choose to export it (PDF report, image share) via iOS's native sharing features — you control the destination yourself.</p>"),
            ("Photo library", "<p>If you choose to save a chart or report to your photo library, the app requests an add-only permission limited to that single action. It does not browse or access the rest of your photo library.</p>"),
            ("In-app purchase", "<p>Treatment and Calculators unlock with a one-time purchase, handled entirely by Apple (App Store). The developer receives neither your payment details nor your identity: the app only asks Apple whether the purchase is active on your Apple ID.</p>"),
            ("No tracking, no third parties", "<ul><li>No user account, no sign-in required.</li><li>No remote server; no network connection is required to use the app (only the purchase and restore go through the App Store).</li><li>No analytics, advertising, or third-party tracking tool is embedded in the app.</li><li>No data is ever sold, shared, or monetized in any way.</li></ul>"),
            ("Contact", f'<p>For any question about this privacy policy, write to us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
        ]),
}

# ============================================================== langues supplémentaires (tools/i18n/<lang>.py)
HERO = {
    "fr": dict(title="RT60 PAR BANDE D'OCTAVE", target="CIBLE 0,50 s", axis="FRÉQUENCE (Hz)", calc="RT60 CALCULÉ", result="0,77 s", note="Estimation indicative · modèle de Sabine", dec=","),
    "en": dict(title="RT60 PER OCTAVE BAND", target="TARGET 0.50 s", axis="FREQUENCY (Hz)", calc="CALCULATED RT60", result="0.77 s", note="Indicative estimate · Sabine model", dec="."),
}
OG = {
    "fr": ("APP IPHONE — GRATUITE", "Écoutez. Analysez. Corrigez.", "Sonomètre · RT60 · Carte du bruit · LiDAR · Accordeur"),
    "en": ("IPHONE APP — FREE", "Listen. Analyze. Correct.", "Sound meter · RT60 · Noise map · LiDAR · Tuner"),
}
for _l in EXTRA:
    _m = importlib.import_module(f"i18n.{_l}")
    T[_l] = {**_m.T, "locale": _m.LOCALE}
    HOME[_l], FEATURES[_l], DOWNLOAD[_l], CONTACT[_l], PRIVACY[_l] = _m.HOME, _m.FEATURES, _m.DOWNLOAD, _m.CONTACT, _m.PRIVACY
    JDG_APPS[_l], HERO[_l], OG[_l] = _m.JDG, _m.HERO, _m.OG
    LABELS[_l], HREFLANGS[_l], LOCALES[_l] = _m.LABEL, _m.HREFLANG, _m.LOCALE
    APPSTORE[_l] = APPSTORE_BASE + "?l=" + _m.STORE_L
    for _k in FILES:
        FILES[_k][_l] = FILES[_k]["en"]
T["fr"]["locale"], T["en"]["locale"] = "fr_CA", "en_CA"


# ============================================================== visuel d'accueil
def hero_svg(lang):
    hx = HERO[lang]
    dec = lambda v: f"{v:.1f}".replace(".", hx["dec"])
    vals = [2.9, 1.6, 1.0, 0.6, 0.5, 0.4]
    names = ["125", "250", "500", "1k", "2k", "4k"]
    base, top = 330, 110
    k = (base - top) / 3.0
    bw, gap, x0 = 38, 14, 51
    parts = []
    for g in range(4):
        y = base - g * k
        parts.append(f'<line x1="36" y1="{y:.1f}" x2="364" y2="{y:.1f}" stroke="#C4B4E5" stroke-opacity=".20"/>')
        parts.append(f'<text x="28" y="{y + 3.5:.1f}" text-anchor="end" fill="#C4B4E5" fill-opacity=".6" font-size="10">{g}</text>')
    for i, v in enumerate(vals):
        x = x0 + i * (bw + gap)
        h = v * k
        col = "#FF3355" if v > 0.5 else "#39FF14"
        parts.append(f'<rect x="{x}" y="{base - h:.1f}" width="{bw}" height="{h:.1f}" rx="3" fill="{col}"/>')
        parts.append(f'<text x="{x + bw / 2}" y="{base - h - 7:.1f}" text-anchor="middle" fill="#fff" font-size="12">{dec(v)}</text>')
        parts.append(f'<text x="{x + bw / 2}" y="{base + 19}" text-anchor="middle" fill="#C4B4E5" font-size="11">{names[i]}</text>')
    ty = base - 0.5 * k
    parts.append(f'<line x1="36" y1="{ty:.1f}" x2="364" y2="{ty:.1f}" stroke="#fff" stroke-opacity=".75" stroke-dasharray="6 5"/>')
    title, target, axis, calc, result, note = hx["title"], hx["target"], hx["axis"], hx["calc"], hx["result"], hx["note"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" font-family="ui-monospace, Menlo, Consolas, monospace" role="img" aria-label="{title}">
<text x="36" y="56" fill="#C4B4E5" font-size="13" letter-spacing="2">{title}</text>
<line x1="36" y1="92" x2="66" y2="92" stroke="#fff" stroke-opacity=".75" stroke-dasharray="6 5"/>
<text x="74" y="96" fill="#fff" fill-opacity=".85" font-size="11" letter-spacing="1">{target}</text>
{"".join(parts)}
<text x="200" y="372" text-anchor="middle" fill="#C4B4E5" fill-opacity=".6" font-size="10" letter-spacing="1.5">{axis}</text>
<rect x="105" y="398" width="190" height="64" rx="8" fill="#1E0C36" stroke="#39FF14" stroke-width="1.5"/>
<text x="200" y="419" text-anchor="middle" fill="#C4B4E5" font-size="10" letter-spacing="2">{calc}</text>
<text x="200" y="449" text-anchor="middle" fill="#fff" font-size="28" font-weight="500">{result}</text>
<text x="200" y="487" text-anchor="middle" fill="#C4B4E5" fill-opacity=".6" font-size="10">{note}</text>
</svg>
'''


# ============================================================== gabarit
def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def page(lang, key, title, desc, body, depth=1, jsonld=None):
    """depth=1 : fichier dans fr/ ou en/ ; depth=0 : ancienne adresse à la racine."""
    t = T[lang]
    up = "../" if depth else ""
    own = "" if depth else f"{lang}/"
    nav = "".join(f'<li><a href="{own}{FILES[k][lang]}"{" aria-current=\"page\"" if k == key else ""}>{t["nav"][k]}</a></li>' for k in NAV_ORDER)
    foot = "".join(f'<li><a href="{own}{FILES[k][lang]}">{t["nav"][k]}</a></li>' for k in NAV_ORDER + ["privacy"])
    sw = ""
    for l in LANGS:
        href = (FILES[key][l] if l == lang else f"../{l}/{FILES[key][l]}") if depth else f"{l}/{FILES[key][l]}"
        sw += f'<a href="{href}" hreflang="{HREFLANGS[l]}" lang="{HREFLANGS[l]}"{" class=\"active\"" if l == lang else ""}>{LABELS[l]}</a>'
    path = lambda l: f"{SITE}/{l}/{'' if key == 'home' else FILES[key][l]}"
    canon = path(lang)
    alts = "".join(f'<link rel="alternate" hreflang="{HREFLANGS[l]}" href="{path(l)}">\n' for l in LANGS)
    alt_loc = "".join(f'<meta property="og:locale:alternate" content="{LOCALES[l]}">\n' for l in LANGS if l != lang)
    og = f"{SITE}/assets/img/og-image-{lang}.png"
    ld = f'<script type="application/ld+json">\n{json.dumps(jsonld, ensure_ascii=False, indent=2)}\n</script>\n' if jsonld else ""
    cta = f'<a href="{own}{FILES["download"][lang]}" class="btn btn--primary btn--sm">{t["cta"]}</a>'
    return f"""<!DOCTYPE html>
<html lang="{HREFLANGS[lang]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alts}<link rel="alternate" hreflang="x-default" href="{path('fr')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Acoustic Detector">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t['locale']}">
{alt_loc}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{og}">
<meta name="theme-color" content="#1E0C36">
<meta name="author" content="JDG inc.">
<meta name="apple-itunes-app" content="app-id=6810440422">
{ld}<link rel="icon" type="image/png" sizes="48x48" href="{up}assets/favicon-48.png">
<link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/css/style.css">
</head>
<body>

<header class="site-header">
  <div class="container site-header__row">
    <a href="{own}index.html" class="brand"><img src="{up}assets/img/logo-mark.png" alt="" class="brand-mark" width="38" height="38">Acoustic Detector</a>
    <nav class="main-nav" id="main-nav" aria-label="{t['menu']}">
      <ul class="main-nav__links">{nav}</ul>
    </nav>
    <div class="header-actions">
      <div class="lang-switch">{sw}</div>
      {cta}
      <button class="nav-toggle" aria-label="{t['menu']}" aria-expanded="false" aria-controls="main-nav"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>

<main>
{body}
</main>

<footer class="site-footer">
  <div class="container">
    <div class="site-footer__row">
      <a href="{own}index.html" class="site-footer__brand"><img src="{up}assets/img/logo-mark.png" alt="" class="brand-mark" width="30" height="30">Acoustic Detector</a>
      <nav><ul>{foot}</ul></nav>
    </div>
    {JDG_APPS[lang]}
    <div class="site-footer__meta">{t['footer']}</div>
  </div>
</footer>

<script src="{up}assets/js/main.js"></script>
</body>
</html>
"""


def store_button(lang):
    return f'<a href="{APPSTORE[lang]}" class="btn btn--primary" target="_blank" rel="noopener">{T[lang]["store"]}</a>'


def shot(lang, key, alt, cls="phone", depth=1):
    up = "../" if depth else ""
    return f'<img src="{up}assets/img/s-{lang}-{key}.webp" alt="{esc(alt)}" width="280" height="606" loading="lazy" class="{cls}">'


def cta_band(lang, h, p, extra=""):
    return f'<section><div class="container"><div class="cta-band"><h2>{h}</h2><p>{p}</p>{extra or store_button(lang)}</div></div></section>'


def jsonld(lang):
    h = HOME[lang]
    return {
        "@context": "https://schema.org", "@type": "MobileApplication", "name": "Acoustic Detector",
        "operatingSystem": "iOS 17+", "applicationCategory": "UtilitiesApplication",
        "url": f"{SITE}/{lang}/", "description": h["desc"], "inLanguage": [HREFLANGS[l] for l in LANGS],
        "image": f"{SITE}/assets/img/logo-large.png", "installUrl": APPSTORE[lang], "sameAs": [APPSTORE_BASE],
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "CAD"},
        "publisher": {"@type": "Organization", "name": "JDG inc.",
                      "address": {"@type": "PostalAddress", "addressRegion": "QC", "addressCountry": "CA"}},
    }


# ============================================================== pages
def home(lang):
    h, t = HOME[lang], T[lang]
    meta = "".join(f"<span><strong>{a}</strong> {b}</span>" if a else f"<span><strong>{b}</strong></span>" for a, b in h["meta"])
    what = "".join(
        f'<div class="card">{f"<span class=\"card__badge\">{b}</span>" if b else ""}<h3>{a}</h3><p>{c}</p></div>' for a, c, b in h["what"])
    shots = "".join(f'<figure>{shot(lang, k, a, "")}<figcaption>{c}</figcaption></figure>' for k, a, c in h["shots"])
    who = "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in h["who"])
    nums = "".join(f'<div class="specs__item"><div class="label">{b}</div><div class="value" style="font-size:1.6rem">{a}</div></div>' for a, b in h["nums"])
    plans = "".join(
        f'<div class="plan{" plan--full" if full else ""}"><h3>{n}</h3><div class="price">{p}</div><ul>{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
        for n, p, items, full in h["plans"])
    news = "".join(f"<li>{x}</li>" for x in h["new"])
    body = f"""<section class="hero">
  <div class="container hero__grid">
    <div>
      <p class="eyebrow">{h['eyebrow']}</p>
      <h1>{h['h1']}</h1>
      <p class="lead">{h['lead']}</p>
      <div class="hero__actions">{store_button(lang)}<a href="{FILES['features'][lang]}" class="btn btn--outline">{t['more']}</a></div>
      <div class="hero__meta">{meta}</div>
    </div>
    <div class="hero__visual"><img src="../assets/img/hero-{lang}.svg" alt="{esc(h['hero_alt'])}" width="400" height="500"></div>
  </div>
</section>

<div class="wave"></div>

<section class="section--tight">
  <div class="container">
    <div class="card card--new">
      <span class="badge-new">{h['new_badge']}</span>
      <h2 style="margin-top:16px">{h['new_h']}</h2>
      <p class="lead" style="margin-bottom:0">{h['new_lead']}</p>
      <ul class="changelog-list">{news}</ul>
      <p class="news-status">{h['new_status']}</p>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="container"><div class="callout">{h['callout']}</div></div>
</section>

<section class="section--alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">{h['what_eyebrow']}</p><h2>{h['what_h']}</h2></div>
    <div class="grid-3">{what}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head"><p class="eyebrow">{h['shots_eyebrow']}</p><h2>{h['shots_h']}</h2></div>
    <div class="shots">{shots}</div>
  </div>
</section>

<section class="section--alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">{h['who_eyebrow']}</p><h2>{h['who_h']}</h2></div>
    <div class="grid-3">{who}</div>
  </div>
</section>

<section class="section--tight">
  <div class="container"><div class="specs">{nums}</div></div>
</section>

<section class="section--alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">{h['price_eyebrow']}</p><h2>{h['price_h']}</h2></div>
    <div class="plans">{plans}</div>
    <p style="margin-top:22px;font-size:.92rem">{h['price_note']}</p>
  </div>
</section>

{cta_band(lang, h['cta_h'], h['cta_p'])}"""
    return page(lang, "home", h["title"], h["desc"], body, jsonld=jsonld(lang))


def features(lang):
    f = FEATURES[lang]
    measure = "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in f["measure"])
    spots = ""
    for key, title, lead, bullets in f["spots"]:
        li = "".join(f"<li>{b}</li>" for b in bullets)
        spots += f'<div class="feature"><div class="feature__text"><h2>{title}</h2><p class="lead">{lead}</p><ul>{li}</ul></div><div class="feature__img">{shot(lang, key, title)}</div></div>\n'
    c0, c1, c2 = f["cmp_cols"]
    rows = "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in f["cmp"])
    body = f"""<section class="section--tight page-head">
  <div class="container"><p class="eyebrow">{f['eyebrow']}</p><h1>{f['h1']}</h1><p class="lead">{f['lead']}</p></div>
</section>

<div class="wave"></div>

<section>
  <div class="container">
    <div class="section-head"><p class="eyebrow">{f['m_eyebrow']}</p><h2>{f['m_h']}</h2></div>
    <div class="grid-3">{measure}</div>
  </div>
</section>

<section class="section--alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">{f['s_eyebrow']}</p><h2>{f['s_h']}</h2></div>
    {spots}
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head"><h2>{f['cmp_h']}</h2></div>
    <table class="compare"><thead><tr><th>{c0}</th><th>{c1}</th><th>{c2}</th></tr></thead><tbody>{rows}</tbody></table>
    <p class="compare-note">{f['cmp_note']}</p>
  </div>
</section>

{cta_band(lang, HOME[lang]['cta_h'], HOME[lang]['cta_p'])}"""
    return page(lang, "features", f["title"], f["desc"], body)


def download(lang):
    d = DOWNLOAD[lang]
    specs = "".join(f'<div class="specs__item"><div class="label">{a}</div><div class="value">{b}</div></div>' for a, b in d["specs"])
    sheet = "".join(f'<li><span class="num">—</span><div><strong>{a}</strong><p>{b}</p></div></li>' for a, b in d["sheet"])
    faq = "".join(f'<div class="card"><h3>{q}</h3><p>{a}</p></div>' for q, a in d["faq"])
    body = f"""<section class="section--tight page-head">
  <div class="container">
    <p class="eyebrow">{d['eyebrow']}</p><h1>{d['h1']}</h1><p class="lead">{d['lead']}</p>
    {store_button(lang)}
  </div>
</section>

<div class="wave"></div>

<section>
  <div class="container">
    <div class="grid-2">
      <div>
        <div class="section-head"><p class="eyebrow">{d['req_eyebrow']}</p><h2>{d['req_h']}</h2></div>
        <div class="specs" style="grid-template-columns:repeat(2,1fr)">{specs}</div>
        <p style="margin-top:20px;font-size:.92rem">{d['req_note']}</p>
      </div>
      <div class="card">
        <p class="eyebrow">{d['sheet_eyebrow']}</p>
        <h3>{d['sheet_h']}</h3>
        <ul class="advantage-list" style="grid-template-columns:1fr;margin-top:18px">{sheet}</ul>
      </div>
    </div>
  </div>
</section>

<section class="section--alt">
  <div class="container">
    <div class="section-head"><p class="eyebrow">{d['faq_eyebrow']}</p><h2>{d['faq_h']}</h2></div>
    <div class="grid-2">{faq}</div>
  </div>
</section>

{cta_band(lang, d['cta_h'], d['cta_p'])}"""
    return page(lang, "download", d["title"], d["desc"], body)


def contact(lang, depth=1):
    c = CONTACT[lang]
    up = "" if depth else f"{lang}/"
    blocks = "".join(f'<div class="contact-block"><h3>{a}</h3><p>{b}</p><p class="value">{v.replace("href=\"telechargement.html\"", "href=\"" + up + "telechargement.html\"").replace("href=\"download.html\"", "href=\"" + up + "download.html\"")}</p></div>' for a, b, v in c["blocks"])
    faq = "".join(f"<h2>{q}</h2><p>{a.replace('href=\"confidentialite.html\"', 'href=\"' + up + 'confidentialite.html\"').replace('href=\"privacy.html\"', 'href=\"' + up + 'privacy.html\"')}</p>" for q, a in c["faq"])
    body = f"""<section class="section--tight page-head">
  <div class="container"><p class="eyebrow">{c['eyebrow']}</p><h1>{c['h1']}</h1><p class="lead">{c['lead']}</p></div>
</section>

<div class="wave"></div>

<section>
  <div class="container"><div class="contact-grid">{blocks}</div></div>
</section>

<section class="section--alt">
  <div class="container">
    <div class="section-head"><h2>{c['faq_h']}</h2></div>
    <article class="doc">{faq}</article>
  </div>
</section>

{cta_band(lang, c['cta_h'], c['cta_p'], f'<a href="mailto:{EMAIL}" class="btn btn--primary">{EMAIL}</a>')}"""
    return page(lang, "contact", c["title"], c["desc"], body, depth=depth)


def privacy(lang, depth=1):
    p = PRIVACY[lang]
    sections = "".join(f"<h2>{t}</h2>{c}" for t, c in p["sections"])
    body = f"""<section class="section--tight page-head">
  <div class="container"><p class="eyebrow">{p['eyebrow']}</p><h1>{p['h1']}</h1><p class="lead">{p['updated']}</p></div>
</section>

<div class="wave"></div>

<section>
  <div class="container">
    <div class="callout" style="margin-bottom:36px">{p['note']}</div>
    <article class="doc">{sections}</article>
  </div>
</section>"""
    return page(lang, "privacy", p["title"], p["desc"], body, depth=depth)


def redirect(dest, lang="fr", auto=True):
    script = """<script>
  (function () {
    var lang = (navigator.language || "fr").toLowerCase();
    var map = {fr: "fr", es: "es", de: "de", pt: "pt", it: "it", ja: "ja"};
    window.location.replace((map[lang.slice(0, 2)] || "en") + "/index.html");
  })();
</script>
""" if auto else ""
    names = {"fr": "Français", "en": "English", "es": "Español", "de": "Deutsch", "pt": "Português", "it": "Italiano", "ja": "日本語"}
    links = " — ".join(f'<a href="{l}/index.html" style="color:#39FF14">{names[l]}</a>' for l in LANGS)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url={dest}">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Acoustic Detector</title>
<link rel="canonical" href="{SITE}/{dest}">
{script}</head>
<body style="background:#1E0C36;color:#fff;font-family:sans-serif"><p>{links}</p></body>
</html>
"""


def not_found():
    return """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>404 — Acoustic Detector</title>
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
<main><section><div class="container" style="text-align:center;padding:80px 0">
<p class="eyebrow">404</p>
<h1>Page introuvable / Page not found</h1>
<p class="lead" style="margin:0 auto 28px"><a href="/fr/index.html">Retour à l'accueil</a> · <a href="/en/index.html">Back to home</a></p>
</div></section></main>
</body>
</html>
"""


def sitemap():
    urls = []
    for key in NAV_ORDER + ["privacy"]:
        for lang in LANGS:
            path = lambda l: f"{SITE}/{l}/{'' if key == 'home' else FILES[key][l]}"
            prio = "1.0" if key == "home" else ("0.8" if key in ("features", "download") else "0.5")
            freq = "weekly" if key == "home" else "monthly"
            alts = "".join(f'    <xhtml:link rel="alternate" hreflang="{HREFLANGS[l]}" href="{path(l)}"/>\n' for l in LANGS)
            urls.append(f"""  <url>
    <loc>{path(lang)}</loc>
{alts}    <xhtml:link rel="alternate" hreflang="x-default" href="{path('fr')}"/>
    <lastmod>{TODAY}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n\n' + "\n\n".join(urls) + "\n</urlset>\n")


def build():
    for lang in LANGS:
        d = ROOT / lang
        d.mkdir(exist_ok=True)
        (d / FILES["home"][lang]).write_text(home(lang), encoding="utf-8")
        (d / FILES["features"][lang]).write_text(features(lang), encoding="utf-8")
        (d / FILES["download"][lang]).write_text(download(lang), encoding="utf-8")
        (d / FILES["contact"][lang]).write_text(contact(lang), encoding="utf-8")
        (d / FILES["privacy"][lang]).write_text(privacy(lang), encoding="utf-8")
        (ROOT / "assets" / "img" / f"hero-{lang}.svg").write_text(hero_svg(lang), encoding="utf-8")
    for name, lang, key in LEGACY:
        html = contact(lang, depth=0) if key == "contact" else privacy(lang, depth=0)
        (ROOT / name).write_text(html, encoding="utf-8")
    (ROOT / "index.html").write_text(redirect("fr/index.html"), encoding="utf-8")
    (ROOT / "en.html").write_text(redirect("en/index.html", lang="en", auto=False), encoding="utf-8")
    (ROOT / "404.html").write_text(not_found(), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print("Site généré dans", ROOT)


if __name__ == "__main__":
    build()
