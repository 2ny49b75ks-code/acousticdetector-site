EMAIL = "j_david@live.ca"
LANG = "it"
LABEL = "IT"
LOCALE = "it_IT"
HREFLANG = "it"
STORE_L = "it"

T = {
    "nav": {"home": "Home", "features": "Funzioni", "download": "Download", "contact": "Contatti", "privacy": "Privacy"},
    "cta": "Scarica", "store": "Scarica dall'App Store", "menu": "Menu",
    "footer": "© 2026 JDG inc. — Québec, Canada. Acoustic Detector è un marchio di JDG inc.",
    "more": "Vedi tutte le funzioni",
}

JDG = '<div class="jdg-apps" style="margin-top:18px;padding-top:14px;border-top:1px solid rgba(127,127,127,.3);font-size:.88em;line-height:1.8;text-align:center"><strong>Altre app di JDG inc., Québec:</strong> <a href="https://camordtu.netlify.app/">CaMordTu</a> <span style="opacity:.75">(guida alla pesca nel Québec)</span> · <a href="https://sitedim.netlify.app/fr/index.html">SITE DIM</a> <span style="opacity:.75">(rilievo di cantiere in realtà aumentata)</span> · <a href="https://appmycreation.com/">MY CREATION</a> <span style="opacity:.75">(le tue opere in rilievo 3D e realtà aumentata)</span> · <a href="https://tricolab.netlify.app/fr/index.html">Tricolab</a> <span style="opacity:.75">(maglia, uncinetto e scrapbooking)</span> · <a href="https://apps.apple.com/ca/app/id6811432420?l=fr-CA">Fort et Château</a> <span style="opacity:.75">(forti e castelli del mondo)</span></div>'

HERO = dict(title="RT60 PER BANDA D'OTTAVA", target="OBIETTIVO 0,50 s", axis="FREQUENZA (Hz)", calc="RT60 CALCOLATO", result="0,77 s", note="Stima indicativa · modello di Sabine", dec=",")
OG = ("APP PER IPHONE — GRATIS", "Ascolta. Analizza. Correggi.", "Fonometro · RT60 · Mappa del rumore · LiDAR · Accordatore")

HOME = dict(
    title="Acoustic Detector — Fonometro, RT60 e acustica degli ambienti",
    desc="App gratuita per iPhone: fonometro, analizzatore, accordatore, RT60 per banda d'ottava, mappa del rumore, doppia parete e scansione LiDAR della stanza. Offline, in 7 lingue.",
    eyebrow="Misura del suono e trattamento acustico",
    h1="Ascolta. Analizza. Correggi.",
    lead="Acoustic Detector trasforma il tuo iPhone in uno strumento di acustica. Misura il rumore, analizza lo spettro, scansiona una stanza con il LiDAR e scopri dove risuona e quanta schiuma acustica aggiungere. Gratis, 100 % offline, in 7 lingue.",
    meta=[("iOS 17+", "richiesto"), ("", "iPhone"), ("7 lingue", "IT · FR · EN · ES · DE · PT · JA"), ("Gratis", "acquisto singolo facoltativo")],
    hero_alt="Riverbero di una stanza per banda d'ottava, confrontato con l'obiettivo di 0,50 secondi",
    new_badge="Novità", new_h="Versione 1.4.1: un accordatore gratuito, più stabile e preciso",
    new_lead="Acoustic Detector include un accordatore gratuito per chitarra, ukulele, violino e altro, e ora parla italiano, francese, inglese, spagnolo, tedesco, portoghese e giapponese.",
    new=["Accordatore gratuito: chitarra (5 accordature), ukulele (anche Sol grave e baritono), violino, viola, violoncello, mandolino, banjo e modalità cromatica per la voce",
         "Versione 1.4.1: lettura più stabile che ignora le misure anomale, ago più preciso, indicatore del livello del segnale",
         "Note in Do Re Mi o in C D E secondo la lingua, e una vibrazione quando è intonato",
         "7 lingue, selezionabili dal menu principale",
         "RT60 per banda d'ottava, da 125 Hz a 4 kHz, rispetto al tuo obiettivo",
         "Mappa del rumore: misura in più punti e ottieni una mappa di calore",
         "Doppia parete: frequenza di risonanza e isolamento per frequenza",
         "L'app è gratuita: fonometro, analizzatore, accordatore, tabella delle misure ed esportazione PDF inclusi; Trattamento e Calcolatori con un acquisto singolo"],
    new_status="Versione 1.4.1 disponibile sull'App Store.",
    callout="<p><strong>Uno strumento indicativo, presentato con onestà.</strong> Il microfono dell'iPhone non è uno strumento certificato: i valori mostrati sono stime, chiaramente indicate come tali, con una calibrazione manuale facoltativa per affinare la precisione. Acoustic Detector non sostituisce uno strumento calibrato per la conformità normativa ufficiale.</p>",
    what_eyebrow="Cosa fa Acoustic Detector", what_h="Un solo dispositivo per misurare e correggere",
    what=[("Fonometro in tempo reale", "Livello in dB in tempo reale, con minimo, media e massimo, calibrazione del microfono e storico a colori.", ""),
          ("Analizzatore di spettro", "Analisi delle frequenze in tempo reale, con rilevamento del tono puro: frequenza, periodo e lunghezza d'onda.", ""),
          ("Trattamento di una stanza", "Il tempo di riverbero (RT60) rispetto all'obiettivo del tuo uso, e la quantità di schiuma acustica da aggiungere.", ""),
          ("Scansione LiDAR", "Su iPhone Pro, passa lo sguardo sulla stanza: dimensioni e superficie di ogni parete si compilano da sole.", ""),
          ("Mappa del rumore", "Misura il livello in più punti e individua le zone calme e rumorose su una mappa di calore.", ""),
          ("Accordatore", "Chitarra, ukulele, violino, viola, violoncello, mandolino, banjo, o qualsiasi nota e la tua voce: ago e cent in tempo reale.", "Novità"),
          ("Calcolatori", "Somma di sorgenti sonore, pressione sonora, frequenza e lunghezza d'onda, e calcolo della doppia parete.", "")],
    shots_eyebrow="Anteprima", shots_h="Sobrio, preciso, pronto per il lavoro sul campo",
    shots=[("menu", "Menu principale", "Menu"), ("tuner", "Accordatore per chitarra con ago e cent", "Accordatore"), ("sono", "Fonometro e calibrazione del microfono", "Fonometro"),
           ("freq", "Riverbero per frequenza e assorbimento dei materiali", "RT60 per frequenza"),
           ("noise", "Mappa di calore del rumore di una stanza", "Mappa del rumore"), ("wall", "Calcolo della doppia parete", "Doppia parete"),
           ("lidar", "Scansione della stanza con LiDAR", "Scansione LiDAR"), ("table", "Tabella delle misure", "Tabella")],
    who_eyebrow="Per chi", who_h="Dal cantiere allo studio",
    who=[("Imprese e tecnici", "Misura il rumore di un luogo, verifica una parete divisoria, stima il trattamento di una stanza prima di fare un preventivo."),
         ("Studi, musicisti, audio", "Calcola il riverbero di una sala, individua i bassi problematici, stima la schiuma da aggiungere e accorda i tuoi strumenti."),
         ("Casa e ufficio", "Home cinema, ufficio in casa, sala riunioni: scopri dove risuona e cosa fare.")],
    nums=[("5", "Modalità di misura"), ("6", "Bande d'ottava"), ("10", "Materiali acustici"), ("100 %", "Offline")],
    price_eyebrow="Prezzo", price_h="Gratis, con un acquisto singolo facoltativo",
    plans=[("Gratis", "0 $", ["Fonometro in tempo reale e calibrazione", "Analizzatore di spettro", "Accordatore (chitarra, violino, voce e altro)", "Tabella delle misure", "Esportazione PDF con grafici"], False),
           ("Completo", "4,99 CA$, acquisto singolo", ["Tutto il gratuito", "Trattamento: RT60, assorbimento, scansione LiDAR, mappa del rumore", "Calcolatori: sorgenti, pressione, onde, doppia parete", "Nessun abbonamento"], True)],
    price_note="Il prezzo è mostrato dall'App Store in base al tuo paese. Se hai acquistato l'app prima che diventasse gratuita, tutto resta sbloccato automaticamente.",
    cta_h="Pronto ad ascoltare la tua stanza?", cta_p="Acoustic Detector è disponibile sull'App Store, per iPhone. Gratis, con un acquisto singolo facoltativo.",
)

FEATURES = dict(
    title="Funzioni — Acoustic Detector",
    desc="Fonometro, analizzatore, accordatore, RT60 per banda d'ottava, assorbimento, mappa del rumore, scansione LiDAR, doppia parete e report PDF: tutto ciò che fa Acoustic Detector.",
    eyebrow="Funzioni", h1="Tutto ciò che serve per misurare e correggere una stanza",
    lead="Il microfono e la fotocamera dell'iPhone, usati per misurare, calcolare e documentare l'acustica di un luogo — senza uscire dall'app, senza connessione.",
    m_eyebrow="Misurare", m_h="Gratis: quello che serve per misurare ogni giorno",
    measure=[("Fonometro in tempo reale", "Livello in dB in tempo reale, con minimo, media e massimo, e due stili di grafico (Festival, Studio)."),
             ("Calibrazione del microfono", "Confronta con un fonometro di riferimento e regola: ogni misura indica se è calibrata o stimata."),
             ("Analizzatore di spettro", "Analisi delle frequenze in tempo reale (FFT) e classificazione del suono: puro, complesso o rumore."),
             ("Tono puro", "Per un tono puro, frequenza, periodo e lunghezza d'onda sono calcolati per te."),
             ("Storico a colori", "Ogni sessione viene salvata con la sua curva: verde, giallo o rosso secondo il livello."),
             ("Tabella delle misure", "Il registro di tutte le tue misure, con filtro, ordinamento ed esportazione in report PDF con grafici.")],
    s_eyebrow="In dettaglio", s_h="Ogni strumento, da vicino",
    spots=[
        ("tuner", "Accordatore", "Accorda a orecchio, o lascia fare all'ago.",
         ["Chitarra (5 accordature), ukulele (anche Sol grave e baritono), violino, viola, violoncello, mandolino e banjo", "Modalità cromatica per la voce e qualsiasi nota", "Ago con cent in tempo reale e una scala di accordatura fine di ±10 cent, con vibrazione quando è intonato", "Lettura stabilizzata che ignora le misure anomale, con indicatore del livello del segnale", "Frequenza di riferimento regolabile da 430 a 450 Hz, e gratuito"]),
        ("sono", "Fonometro, calibrazione e storico", "Il fonometro più semplice da aprire sul campo.",
         ["Livello in tempo reale, minimo, media e massimo", "Calibrazione del microfono con uno strumento di riferimento, con lo stato di calibrazione annotato su ogni misura", "Storico delle sessioni con la loro curva a colori", "Condividi l'immagine o aggiungila alla tabella delle misure"]),
        ("freq", "Riverbero per frequenza", "Sapere dove la stanza ha un problema, non solo se ce l'ha.",
         ["RT60 per banda d'ottava, da 125 Hz a 4 kHz, rispetto all'obiettivo del tuo uso (ufficio, studio, sala riunioni, home cinema)", "Le bande sopra l'obiettivo sono segnalate, con un consiglio per i bassi", "Curve di assorbimento di ogni materiale della stanza, tra 10 materiali", "Modello di Sabine e coefficienti tipici: una stima indicativa"]),
        ("lidar", "Dalla scansione alla schiuma da aggiungere", "Scansiona la stanza e lascia fare i conti all'app.",
         ["Su iPhone Pro (LiDAR), una passata compila le dimensioni e la superficie di ogni parete", "Senza LiDAR, inserisci le dimensioni a mano: tutto il resto funziona", "Schema 3D isometrico della stanza, riportato nella tabella e nel report PDF", "La quantità di schiuma acustica da aggiungere per raggiungere l'obiettivo", "Misura dell'RT60 in tempo reale con un breve burst di rumore"]),
        ("noise", "Mappa del rumore", "Vedere a colpo d'occhio dove una stanza è rumorosa.",
         ["Tocca la pianta della stanza e misura cinque secondi in ogni punto", "Mappa di calore delle zone calme e rumorose", "Livello più calmo, media (Leq) e livello più rumoroso", "Salvata nella tabella delle misure e nel report PDF"]),
        ("calc", "Calcolatori acustici", "Le formule del mestiere, senza carta né calcolatrice.",
         ["Somma di sorgenti sonore: quanti dB insieme", "Livello di pressione sonora a partire dalla pressione in pascal", "Frequenza, periodo e lunghezza d'onda", "Ogni risultato si aggiunge alla tabella con un tocco"]),
        ("wall", "Doppia parete", "Stimare l'isolamento di una parete prima di costruirla.",
         ["Calcolo massa-molla-massa a partire dalla massa di ogni lastra e dalla profondità dell'intercapedine", "Frequenza di risonanza e isolamento per banda d'ottava", "Con o senza lana minerale, e lastre disaccoppiate come opzione", "Stima indicativa, non un indice Rw/STC certificato"]),
        ("table", "Tabella delle misure e report PDF", "Tutto ciò che misuri resta in ordine e condivisibile.",
         ["Ogni misura viene aggiunta a una tabella centrale, filtrabile per tipo", "Report PDF con grafici e schema 3D della stanza", "Salva un grafico in Foto o condividilo con gli strumenti di iOS", "Tutto resta sul tuo dispositivo: nessun account, nessun server"]),
    ],
    cmp_h="Gratis o Acoustic Detector Completo", cmp_cols=("", "Gratis", "Completo"),
    cmp=[("Fonometro in tempo reale e calibrazione", "✓", "✓"), ("Analizzatore di spettro", "✓", "✓"), ("Accordatore", "✓", "✓"), ("Tabella delle misure ed esportazione PDF", "✓", "✓"),
         ("RT60 della stanza e schiuma da aggiungere", "—", "✓"), ("RT60 per banda d'ottava e assorbimento", "—", "✓"), ("Scansione LiDAR della stanza", "—", "✓"),
         ("Mappa del rumore", "—", "✓"), ("Calcolatori e doppia parete", "—", "✓")],
    cmp_note="«Acoustic Detector Completo» è un acquisto singolo di 4,99 CA$, senza abbonamento.",
)

DOWNLOAD = dict(
    title="Download — Acoustic Detector",
    desc="Scarica Acoustic Detector dall'App Store per iPhone. Gratis, con un acquisto singolo facoltativo.",
    eyebrow="Download", h1="Acoustic Detector sull'App Store",
    lead="Un'app nativa per iOS, pensata per essere usata direttamente sul campo: in cantiere, in studio o a casa.",
    req_eyebrow="Requisiti", req_h="Verifica la compatibilità del tuo dispositivo",
    specs=[("Sistema", "iOS 17+"), ("Dispositivo", "iPhone"), ("Prezzo", "Gratis"), ("Acquisto singolo", "4,99 CA$")],
    req_note="Acoustic Detector funziona su qualsiasi iPhone con iOS 17 o successivo. La scansione LiDAR della stanza richiede un iPhone Pro con sensore LiDAR (iPhone 12 Pro e successivi); sugli altri iPhone le dimensioni della stanza si inseriscono a mano.",
    sheet_eyebrow="Scheda tecnica", sheet_h="Informazioni sull'app",
    sheet=[("Sviluppatore", "JDG inc., Québec, Canada"), ("Identificativo", "JDG-inc.AcousticDetector"), ("Lingue", "Italiano, francese, inglese, spagnolo, tedesco, portoghese (Brasile) e giapponese"), ("Esportazioni", "Report PDF con grafici, condivisione di immagini")],
    faq_eyebrow="Domande frequenti", faq_h="Prima di scaricare",
    faq=[("Il mio dispositivo è compatibile?", "Se il tuo iPhone ha iOS 17 o successivo, è compatibile. Il LiDAR non è necessario: aggiunge solo la scansione automatica della stanza."),
         ("Quanto costa?", "L'app è gratuita. L'acquisto singolo facoltativo «Acoustic Detector Completo» (4,99 CA$) sblocca Trattamento e Calcolatori, senza abbonamento."),
         ("Funziona offline?", "Sì. Misure e calcoli si fanno sul dispositivo, senza account né server. Solo l'acquisto e il ripristino passano dall'App Store."),
         ("Le misure sono precise?", "Il microfono dell'iPhone fornisce una stima, non una misura certificata. Una calibrazione manuale facoltativa permette di affinare il risultato."),
         ("In quali lingue?", "In italiano, francese, inglese, spagnolo, tedesco, portoghese (Brasile) e giapponese, selezionabili dal menu principale."),
         ("Come ottengo assistenza?", f'Scrivici a <a href="mailto:{EMAIL}">{EMAIL}</a> o visita la pagina <a href="contact.html">Contatti</a>.')],
    cta_h="Pronto a iniziare?", cta_p="Acoustic Detector è disponibile sull'App Store.",
)

CONTACT = dict(
    title="Contatti e assistenza — Acoustic Detector", desc="Aiuto, domande frequenti, acquisto e ripristino, stampa: scrivici riguardo all'app Acoustic Detector. Ogni messaggio riceve una risposta.",
    eyebrow="Contatti", h1="Contatti e assistenza",
    lead="Una domanda, un bug da segnalare o un suggerimento? Ogni messaggio viene letto e riceve una risposta personale.",
    blocks=[("Assistenza e domande", "Se possibile, indica il modello del tuo iPhone e la versione di iOS.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector">{EMAIL}</a>'),
            ("Stampa e media", "Un kit stampa (presentazione, funzioni, scheda tecnica) è disponibile su richiesta.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector%20-%20Stampa">{EMAIL}</a>'),
            ("Sviluppatore", "Acoustic Detector è ideata e sviluppata da JDG inc.", "JDG inc. — Québec, Canada"),
            ("App", "Disponibile sull'App Store per iPhone con iOS 17+.", '<a href="download.html">Vai alla pagina di download</a>')],
    faq_h="Domande frequenti",
    faq=[("Le misure in decibel sono calibrate?", "No, non per impostazione predefinita. Acoustic Detector usa il microfono integrato dell'iPhone per stimare il livello sonoro — è indicativo, non uno strumento certificato. La modalità Fonometro offre una calibrazione manuale facoltativa con uno strumento di riferimento per affinare la precisione."),
         ("La scansione LiDAR funziona su tutti gli iPhone?", "No, solo sui modelli Pro con sensore LiDAR (iPhone 12 Pro e successivi). Sugli altri iPhone le dimensioni della stanza si inseriscono manualmente nella modalità Trattamento — tutte le funzioni di calcolo restano disponibili."),
         ("Il calcolo del riverbero (RT60) è esatto?", "La modalità Trattamento offre due stime: un calcolo teorico (formula di Sabine, basato sulle tue dimensioni e sui materiali, per banda d'ottava) e una misura in tempo reale con un burst di rumore. Entrambe sono approssimazioni utili per orientare un trattamento acustico, non misure di laboratorio."),
         ("Le mie misure vengono inviate da qualche parte?", 'No. Nessun dato lascia il tuo dispositivo. Consulta la nostra <a href="privacy.html">informativa sulla privacy</a>.'),
         ("L'app è disponibile in italiano?", "Sì. Acoustic Detector è disponibile in 7 lingue (italiano, francese, inglese, spagnolo, tedesco, portoghese e giapponese): un pulsante della lingua nel menu principale cambia la lingua dell'interfaccia, indipendentemente dalla lingua del tuo iPhone."),
         ("C'è un abbonamento?", "No. Acoustic Detector si scarica gratis: fonometro, analizzatore, accordatore, tabella delle misure ed esportazione PDF sono inclusi. Trattamento e Calcolatori si sbloccano con un acquisto singolo (4,99 CA$), senza abbonamento. Gli aggiornamenti sono inclusi. Se hai acquistato l'app prima che diventasse gratuita, tutto resta sbloccato automaticamente."),
         ("Come ripristino il mio acquisto?", "Su un nuovo iPhone o dopo una reinstallazione, apri Trattamento o Calcolatori e tocca «Ripristina acquisti», con lo stesso ID Apple usato per l'acquisto."),
         ("L'app esiste per Android?", "Per ora no — Acoustic Detector è disponibile su iPhone (iOS 17 o successivo).")],
    cta_h="Una domanda prima di scaricare?", cta_p="Scrivici — rispondiamo direttamente, senza giri di parole.",
)

PRIVACY = dict(
    title="Informativa sulla privacy — Acoustic Detector", desc="Acoustic Detector non raccoglie, trasmette né condivide alcun dato personale: nessun account, nessun server, nessun tracker.",
    eyebrow="Privacy", h1="Informativa sulla privacy", updated="Ultimo aggiornamento: 2 ottobre 2026",
    note="<p><strong>In breve:</strong> Acoustic Detector non raccoglie, trasmette né condivide alcun dato personale. L'app funziona interamente offline, senza account, senza server e senza servizi di terze parti.</p>",
    sections=[
        ("Microfono", "<p>L'app usa il microfono del tuo dispositivo per le funzioni Fonometro, Analizzatore, Accordatore e per la misura del riverbero (RT60) della modalità Trattamento. Il suono captato viene elaborato interamente sul tuo dispositivo, in tempo reale, per calcolare un livello sonoro, uno spettro di frequenze o una nota. Nessuna registrazione audio viene salvata, trasmessa o condivisa — solo i valori numerici calcolati (dB, Hz, secondi) possono essere salvati localmente se scegli di aggiungere una misura alla tabella.</p>"),
        ("Fotocamera e LiDAR", "<p>Sugli iPhone Pro, la modalità Trattamento offre una scansione facoltativa della stanza con fotocamera e LiDAR (tramite RoomPlan e ARKit di Apple) per misurare automaticamente le dimensioni di una stanza. Questa scansione è elaborata interamente sul tuo dispositivo — nessuna immagine, video o dato di scansione viene inviato altrove. Solo le dimensioni e le superfici calcolate vengono conservate, localmente, se scegli di usarle.</p>"),
        ("Dati salvati localmente", "<p>Le misure che scegli di salvare (sessioni del Fonometro, voci della tabella delle misure) sono memorizzate solo nello spazio privato dell'app sul tuo dispositivo. Questi dati non lasciano mai il tuo dispositivo, a meno che tu non scelga esplicitamente di esportarli (report PDF, condivisione di immagini) tramite le funzioni di condivisione native di iOS — in tal caso la destinazione la decidi tu.</p>"),
        ("Libreria foto", "<p>Se scegli di salvare un grafico o un report nella tua libreria foto, l'app richiede un'autorizzazione di sola aggiunta, limitata a quella singola azione. Non consulta né accede al resto della tua libreria foto.</p>"),
        ("Acquisto in-app", "<p>Trattamento e Calcolatori si sbloccano con un acquisto singolo, gestito interamente da Apple (App Store). Lo sviluppatore non riceve né i tuoi dati di pagamento né la tua identità: l'app chiede soltanto ad Apple se l'acquisto è attivo sul tuo ID Apple.</p>"),
        ("Nessun tracciamento, nessuna terza parte", "<ul><li>Nessun account utente, nessuna identificazione richiesta.</li><li>Nessun server remoto; non serve alcuna connessione per usare l'app (solo l'acquisto e il ripristino passano dall'App Store).</li><li>Nessuno strumento di analisi, pubblicità o tracciamento di terze parti è integrato nell'app.</li><li>Nessun dato viene venduto, condiviso o monetizzato in alcun modo.</li></ul>"),
        ("Contatti", f'<p>Per qualsiasi domanda su questa informativa sulla privacy, scrivici a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
    ])
