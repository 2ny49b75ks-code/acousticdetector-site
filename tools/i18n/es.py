EMAIL = "j_david@live.ca"
LANG = "es"
LABEL = "ES"
LOCALE = "es_ES"
HREFLANG = "es"
STORE_L = "es"

T = {
    "nav": {"home": "Inicio", "features": "Funciones", "download": "Descarga", "contact": "Contacto", "privacy": "Privacidad"},
    "cta": "Descargar", "store": "Descargar en el App Store", "menu": "Menú",
    "footer": "© 2026 JDG inc. — Quebec, Canadá. Acoustic Detector es una marca de JDG inc.",
    "more": "Ver todas las funciones",
}

JDG = '<div class="jdg-apps" style="margin-top:18px;padding-top:14px;border-top:1px solid rgba(127,127,127,.3);font-size:.88em;line-height:1.8;text-align:center"><strong>Más apps de JDG inc., Quebec:</strong> <a href="https://camordtu.netlify.app/">CaMordTu</a> <span style="opacity:.75">(guía de pesca en Quebec)</span> · <a href="https://sitedim.netlify.app/fr/index.html">SITE DIM</a> <span style="opacity:.75">(mediciones de obra en realidad aumentada)</span> · <a href="https://appmycreation.com/">MY CREATION</a> <span style="opacity:.75">(tus obras en relieve 3D y realidad aumentada)</span> · <a href="https://tricolab.netlify.app/fr/index.html">Tricolab</a> <span style="opacity:.75">(punto, ganchillo y scrapbooking)</span> · <a href="https://apps.apple.com/ca/app/id6811432420?l=fr-CA">Fort et Château</a> <span style="opacity:.75">(fuertes y castillos del mundo)</span></div>'

HERO = dict(title="RT60 POR BANDA DE OCTAVA", target="OBJETIVO 0,50 s", axis="FRECUENCIA (Hz)", calc="RT60 CALCULADO", result="0,77 s", note="Estimación orientativa · modelo de Sabine", dec=",")
OG = ("APP PARA IPHONE — GRATIS", "Escucha. Analiza. Corrige.", "Sonómetro · RT60 · Mapa de ruido · LiDAR · Afinador")

HOME = dict(
    title="Acoustic Detector — Sonómetro, RT60 y acústica de salas",
    desc="App gratuita para iPhone: sonómetro, analizador, afinador, RT60 por banda de octava, mapa de ruido, doble tabique y escáner LiDAR de la sala. Sin conexión, en 7 idiomas.",
    eyebrow="Medición sonora y tratamiento acústico",
    h1="Escucha. Analiza. Corrige.",
    lead="Acoustic Detector convierte tu iPhone en una herramienta de acústica. Mide el ruido, analiza el espectro, escanea una sala con LiDAR y descubre dónde resuena y cuánta espuma acústica añadir. Gratis, 100 % sin conexión, en 7 idiomas.",
    meta=[("iOS 17+", "requerido"), ("", "iPhone"), ("7 idiomas", "ES · FR · EN · DE · PT · IT · JA"), ("Gratis", "compra única opcional")],
    hero_alt="Reverberación de una sala por banda de octava, comparada con el objetivo de 0,50 segundos",
    new_badge="Novedades", new_h="Versión 1.4.1: un afinador gratuito, más estable y preciso",
    new_lead="Acoustic Detector incluye un afinador gratuito para guitarra, ukelele, violín y más, y habla español, francés, inglés, alemán, portugués, italiano y japonés.",
    new=["Afinador gratuito: guitarra (5 afinaciones), ukelele (con sol grave y barítono), violín, viola, violonchelo, mandolina, banjo y modo cromático para la voz",
         "Versión 1.4.1: lectura más estable que ignora las medidas erráticas, aguja más precisa, indicador de nivel de la señal",
         "Notas en Do Re Mi o en C D E según el idioma, y una vibración cuando está afinado",
         "7 idiomas, a elegir desde el menú principal",
         "RT60 por banda de octava, de 125 Hz a 4 kHz, frente a tu objetivo",
         "Mapa de ruido: mide en varios puntos y obtén un mapa de calor",
         "Doble tabique: frecuencia de resonancia y aislamiento por frecuencia",
         "La app es gratuita: sonómetro, analizador, afinador, tabla de mediciones y exportación a PDF incluidos; Tratamiento y Calculadoras con una compra única"],
    new_status="Versión 1.4.1 disponible en el App Store.",
    callout="<p><strong>Una herramienta orientativa, presentada con honestidad.</strong> El micrófono del iPhone no es un instrumento certificado: los valores mostrados son estimaciones, identificadas claramente como tales, con una calibración manual opcional para afinar la precisión. Acoustic Detector no sustituye a un instrumento calibrado para el cumplimiento normativo oficial.</p>",
    what_eyebrow="Qué hace Acoustic Detector", what_h="Un solo dispositivo para medir y corregir",
    what=[("Sonómetro en directo", "Nivel en dB en tiempo real, con mínimo, media y máximo, calibración del micrófono e historial en colores.", ""),
          ("Analizador de espectro", "Análisis de frecuencias en directo, con detección de tono puro: frecuencia, periodo y longitud de onda.", ""),
          ("Tratamiento de una sala", "El tiempo de reverberación (RT60) frente al objetivo de tu uso, y la cantidad de espuma acústica que añadir.", ""),
          ("Escáner LiDAR", "En un iPhone Pro, barre la sala: las dimensiones y la superficie de cada pared se rellenan solas.", ""),
          ("Mapa de ruido", "Mide el nivel en varios puntos y localiza las zonas tranquilas y ruidosas en un mapa de calor.", ""),
          ("Afinador", "Guitarra, ukelele, violín, viola, violonchelo, mandolina, banjo, o cualquier nota y tu voz: aguja y cents en directo.", "Novedad"),
          ("Calculadoras", "Suma de fuentes sonoras, presión acústica, frecuencia y longitud de onda, y cálculo de doble tabique.", "")],
    shots_eyebrow="Vista previa", shots_h="Sobrio, preciso, listo para el trabajo de campo",
    shots=[("menu", "Menú principal", "Menú"), ("tuner", "Afinador de guitarra con aguja y cents", "Afinador"), ("sono", "Sonómetro y calibración del micrófono", "Sonómetro"),
           ("freq", "Reverberación por frecuencia y absorción de materiales", "RT60 por frecuencia"),
           ("noise", "Mapa de calor del ruido de una sala", "Mapa de ruido"), ("wall", "Cálculo de doble tabique", "Doble tabique"),
           ("lidar", "Escaneo de sala con LiDAR", "Escáner LiDAR"), ("table", "Tabla de mediciones", "Tabla")],
    who_eyebrow="Para quién", who_h="De la obra al estudio",
    who=[("Contratistas y técnicos", "Mide el ruido de un lugar, comprueba un tabique, estima el tratamiento de una sala antes de presupuestar."),
         ("Estudios, músicos, audio", "Calcula la reverberación de una sala, localiza los graves problemáticos, estima la espuma que añadir y afina tus instrumentos."),
         ("Casa y oficina", "Cine en casa, oficina en casa, sala de reuniones: descubre dónde resuena y qué hacer al respecto.")],
    nums=[("5", "Modos de medición"), ("6", "Bandas de octava"), ("10", "Materiales acústicos"), ("100 %", "Sin conexión")],
    price_eyebrow="Precio", price_h="Gratis, con una compra única opcional",
    plans=[("Gratis", "0 $", ["Sonómetro en directo y calibración", "Analizador de espectro", "Afinador (guitarra, violín, voz y más)", "Tabla de mediciones", "Exportación a PDF con gráficos"], False),
           ("Completo", "4,99 $ CA, compra única", ["Todo lo gratuito", "Tratamiento: RT60, absorción, escáner LiDAR, mapa de ruido", "Calculadoras: fuentes, presión, ondas, doble tabique", "Sin suscripción"], True)],
    price_note="El precio lo muestra el App Store según tu país. Si compraste la app antes de que fuera gratuita, todo sigue desbloqueado automáticamente.",
    cta_h="¿Listo para escuchar tu sala?", cta_p="Acoustic Detector está disponible en el App Store, para iPhone. Gratis, con una compra única opcional.",
)

FEATURES = dict(
    title="Funciones — Acoustic Detector",
    desc="Sonómetro, analizador, afinador, RT60 por banda de octava, absorción, mapa de ruido, escáner LiDAR, doble tabique e informes PDF: todo lo que hace Acoustic Detector.",
    eyebrow="Funciones", h1="Todo lo que necesitas para medir y corregir una sala",
    lead="El micrófono y la cámara del iPhone, usados para medir, calcular y documentar la acústica de un lugar — sin salir de la app, sin conexión.",
    m_eyebrow="Medir", m_h="Gratis: lo necesario para medir a diario",
    measure=[("Sonómetro en directo", "Nivel en dB en tiempo real, con mínimo, media y máximo, y dos estilos de gráfico (Festival, Estudio)."),
             ("Calibración del micrófono", "Compara con un sonómetro de referencia y ajusta: cada medición indica si está calibrada o estimada."),
             ("Analizador de espectro", "Análisis de frecuencias en directo (FFT) y clasificación del sonido: puro, complejo o ruido."),
             ("Tono puro", "Para un tono puro, la frecuencia, el periodo y la longitud de onda se calculan por ti."),
             ("Historial en colores", "Cada sesión se guarda con su curva: verde, amarillo o rojo según el nivel."),
             ("Tabla de mediciones", "El registro de todas tus mediciones, con filtro, orden y exportación a informe PDF con gráficos.")],
    s_eyebrow="En detalle", s_h="Cada herramienta, de cerca",
    spots=[
        ("tuner", "Afinador", "Afina de oído, o deja que la aguja lo haga.",
         ["Guitarra (5 afinaciones), ukelele (incluido sol grave y barítono), violín, viola, violonchelo, mandolina y banjo", "Modo cromático para la voz y cualquier nota", "Aguja con cents en directo y una escala de ajuste fino de ±10 cents, con vibración cuando está afinado", "Lectura estabilizada que ignora las medidas erráticas, con indicador del nivel de la señal", "Frecuencia de referencia ajustable de 430 a 450 Hz, y gratis"]),
        ("sono", "Sonómetro, calibración e historial", "El sonómetro más sencillo de abrir sobre el terreno.",
         ["Nivel en directo, mínimo, media y máximo", "Calibración del micrófono con un instrumento de referencia, con el estado de calibración anotado en cada medición", "Historial de sesiones con su curva en colores", "Comparte la imagen o añádela a la tabla de mediciones"]),
        ("freq", "Reverberación por frecuencia", "Saber dónde tiene problemas la sala, no solo si los tiene.",
         ["RT60 por banda de octava, de 125 Hz a 4 kHz, frente al objetivo de tu uso (oficina, estudio, sala de reuniones, cine en casa)", "Las bandas por encima del objetivo se señalan, con un consejo para los graves", "Curvas de absorción de cada material de la sala, entre 10 materiales", "Modelo de Sabine y coeficientes típicos: una estimación orientativa"]),
        ("lidar", "Del escaneo a la espuma que añadir", "Escanea la sala y deja que la app haga los cálculos.",
         ["En un iPhone Pro (LiDAR), un barrido rellena las dimensiones y la superficie de cada pared", "Sin LiDAR, introduce las dimensiones a mano: todo lo demás funciona", "Esquema 3D isométrico de la sala, incluido en la tabla y el informe PDF", "La cantidad de espuma acústica que añadir para alcanzar el objetivo", "Medición del RT60 en directo con una breve ráfaga de ruido"]),
        ("noise", "Mapa de ruido", "Ver dónde hay ruido en una sala de un vistazo.",
         ["Toca el plano de la sala y mide cinco segundos en cada punto", "Mapa de calor de las zonas tranquilas y ruidosas", "Nivel más tranquilo, media (Leq) y nivel más ruidoso", "Guardado en la tabla de mediciones y en el informe PDF"]),
        ("calc", "Calculadoras acústicas", "Las fórmulas del oficio, sin papel ni calculadora.",
         ["Suma de fuentes sonoras: cuántos dB en conjunto", "Nivel de presión acústica a partir de la presión en pascales", "Frecuencia, periodo y longitud de onda", "Cada resultado se añade a la tabla con un toque"]),
        ("wall", "Doble tabique", "Estimar el aislamiento de un tabique antes de construirlo.",
         ["Cálculo masa-resorte-masa a partir de la masa de cada hoja y la profundidad de la cámara", "Frecuencia de resonancia y aislamiento por banda de octava", "Con o sin lana mineral, y hojas desolidarizadas como opción", "Estimación orientativa, no un índice Rw/STC certificado"]),
        ("table", "Tabla de mediciones e informes PDF", "Todo lo que mides queda ordenado y se puede compartir.",
         ["Cada medición se añade a una tabla central, filtrable por tipo", "Informe PDF con gráficos y esquema 3D de la sala", "Guarda un gráfico en Fotos o compártelo con las herramientas de iOS", "Todo se queda en tu dispositivo: sin cuenta, sin servidor"]),
    ],
    cmp_h="Gratis o Acoustic Detector Completo", cmp_cols=("", "Gratis", "Completo"),
    cmp=[("Sonómetro en directo y calibración", "✓", "✓"), ("Analizador de espectro", "✓", "✓"), ("Afinador", "✓", "✓"), ("Tabla de mediciones y exportación a PDF", "✓", "✓"),
         ("RT60 de la sala y espuma que añadir", "—", "✓"), ("RT60 por banda de octava y absorción", "—", "✓"), ("Escáner LiDAR de la sala", "—", "✓"),
         ("Mapa de ruido", "—", "✓"), ("Calculadoras y doble tabique", "—", "✓")],
    cmp_note="«Acoustic Detector Completo» es una compra única de 4,99 $ CA, sin suscripción.",
)

DOWNLOAD = dict(
    title="Descarga — Acoustic Detector",
    desc="Descarga Acoustic Detector en el App Store para iPhone. Gratis, con una compra única opcional.",
    eyebrow="Descarga", h1="Acoustic Detector en el App Store",
    lead="Una app nativa de iOS, pensada para usarse directamente sobre el terreno: en la obra, en el estudio o en casa.",
    req_eyebrow="Requisitos", req_h="Comprueba la compatibilidad de tu dispositivo",
    specs=[("Sistema", "iOS 17+"), ("Dispositivo", "iPhone"), ("Precio", "Gratis"), ("Compra única", "4,99 $ CA")],
    req_note="Acoustic Detector funciona en cualquier iPhone con iOS 17 o posterior. El escaneo de sala con LiDAR requiere un iPhone Pro con sensor LiDAR (iPhone 12 Pro y posteriores); en los demás iPhone, las dimensiones de la sala se introducen a mano.",
    sheet_eyebrow="Ficha técnica", sheet_h="Información de la app",
    sheet=[("Editor", "JDG inc., Quebec, Canadá"), ("Identificador", "JDG-inc.AcousticDetector"), ("Idiomas", "Español, francés, inglés, alemán, portugués (Brasil), italiano y japonés"), ("Exportaciones", "Informe PDF con gráficos, compartir imágenes")],
    faq_eyebrow="Preguntas frecuentes", faq_h="Antes de descargar",
    faq=[("¿Es compatible mi dispositivo?", "Si tu iPhone tiene iOS 17 o posterior, es compatible. El LiDAR no es necesario: solo añade el escaneo automático de la sala."),
         ("¿Cuánto cuesta?", "La app es gratuita. La compra única opcional «Acoustic Detector Completo» (4,99 $ CA) desbloquea Tratamiento y Calculadoras, sin suscripción."),
         ("¿Funciona sin conexión?", "Sí. Las mediciones y los cálculos se hacen en el dispositivo, sin cuenta ni servidor. Solo la compra y la restauración pasan por el App Store."),
         ("¿Son precisas las mediciones?", "El micrófono del iPhone da una estimación, no una medición certificada. Una calibración manual opcional permite afinar el resultado."),
         ("¿En qué idiomas está?", "En español, francés, inglés, alemán, portugués (Brasil), italiano y japonés, a elegir desde el menú principal."),
         ("¿Cómo obtengo ayuda?", f'Escríbenos a <a href="mailto:{EMAIL}">{EMAIL}</a> o visita la página de <a href="contact.html">Contacto</a>.')],
    cta_h="¿Listo para empezar?", cta_p="Acoustic Detector está disponible en el App Store.",
)

CONTACT = dict(
    title="Contacto y asistencia — Acoustic Detector", desc="Ayuda, preguntas frecuentes, compra y restauración, prensa: escríbenos sobre la app Acoustic Detector. Cada mensaje recibe respuesta.",
    eyebrow="Contacto", h1="Contacto y asistencia",
    lead="¿Una pregunta, un error que comunicar o una sugerencia? Cada mensaje se lee y recibe una respuesta personal.",
    blocks=[("Asistencia y preguntas", "Si puedes, indica tu modelo de iPhone y tu versión de iOS.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector">{EMAIL}</a>'),
            ("Prensa y medios", "Hay un dosier de prensa (presentación, funciones, ficha técnica) disponible a petición.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector%20-%20Prensa">{EMAIL}</a>'),
            ("Editor", "Acoustic Detector está diseñada y desarrollada por JDG inc.", "JDG inc. — Quebec, Canadá"),
            ("App", "Disponible en el App Store para iPhone con iOS 17+.", '<a href="download.html">Ver la página de descarga</a>')],
    faq_h="Preguntas frecuentes",
    faq=[("¿Las mediciones en decibelios están calibradas?", "No, por defecto no. Acoustic Detector usa el micrófono integrado del iPhone para estimar el nivel sonoro: es orientativo, no un instrumento certificado. El modo Sonómetro ofrece una calibración manual opcional con un instrumento de referencia para ajustar la precisión."),
         ("¿El escaneo de sala con LiDAR funciona en todos los iPhone?", "No, solo en los modelos Pro con sensor LiDAR (iPhone 12 Pro y posteriores). En los demás iPhone, las dimensiones de la sala se introducen manualmente en el modo Tratamiento: todas las funciones de cálculo siguen disponibles."),
         ("¿Es exacto el cálculo de reverberación (RT60)?", "El modo Tratamiento ofrece dos estimaciones: un cálculo teórico (fórmula de Sabine, basado en tus dimensiones y materiales, por banda de octava) y una medición en directo con una ráfaga de ruido. Ambas son aproximaciones útiles para orientar un tratamiento acústico, no mediciones de laboratorio."),
         ("¿Se envían mis mediciones a algún sitio?", 'No. Ningún dato sale de tu dispositivo. Consulta nuestra <a href="privacy.html">política de privacidad</a>.'),
         ("¿Está la app en español?", "Sí. Acoustic Detector está disponible en 7 idiomas (español, francés, inglés, alemán, portugués, italiano y japonés): un botón de idioma en el menú principal cambia el idioma de la interfaz, independientemente del idioma de tu iPhone."),
         ("¿Hay suscripción?", "No. Acoustic Detector se descarga gratis: el sonómetro, el analizador, el afinador, la tabla de mediciones y la exportación a PDF están incluidos. Tratamiento y Calculadoras se desbloquean con una compra única (4,99 $ CA), sin suscripción. Las actualizaciones están incluidas. Si compraste la app antes de que fuera gratuita, todo sigue desbloqueado automáticamente."),
         ("¿Cómo restauro mi compra?", "En un iPhone nuevo o tras reinstalar, abre Tratamiento o Calculadoras y toca «Restaurar compras», con el mismo ID de Apple que usaste para la compra."),
         ("¿Existe la app para Android?", "Por ahora no: Acoustic Detector está disponible en iPhone (iOS 17 o posterior).")],
    cta_h="¿Una pregunta antes de descargar?", cta_p="Escríbenos: respondemos directamente, sin rodeos.",
)

PRIVACY = dict(
    title="Política de privacidad — Acoustic Detector", desc="Acoustic Detector no recopila, transmite ni comparte ningún dato personal: sin cuenta, sin servidor, sin rastreadores.",
    eyebrow="Privacidad", h1="Política de privacidad", updated="Última actualización: 2 de octubre de 2026",
    note="<p><strong>En resumen:</strong> Acoustic Detector no recopila, transmite ni comparte ningún dato personal. La app funciona totalmente sin conexión, sin cuenta, sin servidor y sin servicios de terceros.</p>",
    sections=[
        ("Micrófono", "<p>La app usa el micrófono de tu dispositivo para las funciones de Sonómetro, Analizador, Afinador y la medición de reverberación (RT60) del modo Tratamiento. El sonido captado se procesa íntegramente en tu dispositivo, en tiempo real, para calcular un nivel sonoro, un espectro de frecuencias o una nota. No se guarda, transmite ni comparte ninguna grabación de audio: solo los valores numéricos calculados (dB, Hz, segundos) pueden guardarse localmente si decides añadir una medición a la tabla.</p>"),
        ("Cámara y LiDAR", "<p>En los iPhone Pro, el modo Tratamiento ofrece un escaneo de sala opcional con cámara y LiDAR (mediante RoomPlan y ARKit de Apple) para medir automáticamente las dimensiones de una sala. Este escaneo se procesa íntegramente en tu dispositivo: ninguna imagen, vídeo ni dato de escaneo se envía a ningún sitio. Solo se conservan, localmente, las dimensiones y superficies calculadas, si decides usarlas.</p>"),
        ("Datos guardados localmente", "<p>Las mediciones que decides guardar (sesiones del Sonómetro, entradas de la tabla de mediciones) se almacenan únicamente en el espacio privado de la app en tu dispositivo. Estos datos nunca salen de tu dispositivo, salvo que decidas exportarlos explícitamente (informe PDF, compartir imagen) mediante las funciones nativas de compartir de iOS: en ese caso, el destino lo controlas tú.</p>"),
        ("Fototeca", "<p>Si decides guardar un gráfico o un informe en tu fototeca, la app solicita un permiso de solo añadir, limitado a esa única acción. No consulta ni accede al resto de tu fototeca.</p>"),
        ("Compra integrada", "<p>Tratamiento y Calculadoras se desbloquean con una compra única, gestionada íntegramente por Apple (App Store). El desarrollador no recibe ni tus datos de pago ni tu identidad: la app solo pregunta a Apple si la compra está activa en tu ID de Apple.</p>"),
        ("Sin seguimiento, sin terceros", "<ul><li>Sin cuenta de usuario, sin identificación obligatoria.</li><li>Sin servidor remoto; no se necesita conexión para usar la app (solo la compra y la restauración pasan por el App Store).</li><li>La app no integra ninguna herramienta de análisis, publicidad ni seguimiento de terceros.</li><li>Ningún dato se vende, comparte ni monetiza de ninguna manera.</li></ul>"),
        ("Contacto", f'<p>Para cualquier pregunta sobre esta política de privacidad, escríbenos a <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
    ])
