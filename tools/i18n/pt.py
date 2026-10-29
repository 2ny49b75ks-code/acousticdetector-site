EMAIL = "j_david@live.ca"
LANG = "pt"
LABEL = "PT"
LOCALE = "pt_BR"
HREFLANG = "pt-BR"
STORE_L = "pt"

T = {
    "nav": {"home": "Início", "features": "Recursos", "download": "Download", "contact": "Contato", "privacy": "Privacidade"},
    "cta": "Baixar", "store": "Baixar na App Store", "menu": "Menu",
    "footer": "© 2026 JDG inc. — Quebec, Canadá. Acoustic Detector é uma marca da JDG inc.",
    "more": "Ver todos os recursos",
}

JDG = '<div class="jdg-apps" style="margin-top:18px;padding-top:14px;border-top:1px solid rgba(127,127,127,.3);font-size:.88em;line-height:1.8;text-align:center"><strong>Outros apps da JDG inc., Quebec:</strong> <a href="https://camordtu.netlify.app/">CaMordTu</a> <span style="opacity:.75">(guia de pesca em Quebec)</span> · <a href="https://sitedim.netlify.app/fr/index.html">SITE DIM</a> <span style="opacity:.75">(levantamento de obra em realidade aumentada)</span> · <a href="https://appmycreation.com/">MY CREATION</a> <span style="opacity:.75">(suas obras em relevo 3D e realidade aumentada)</span> · <a href="https://tricolab.netlify.app/fr/index.html">Tricolab</a> <span style="opacity:.75">(tricô, crochê e scrapbook)</span> · <a href="https://fortchateau.netlify.app/en/index.html">Fort et Château</a> <span style="opacity:.75">(fortes e castelos do mundo)</span></div>'

HERO = dict(title="RT60 POR BANDA DE OITAVA", target="META 0,50 s", axis="FREQUÊNCIA (Hz)", calc="RT60 CALCULADO", result="0,77 s", note="Estimativa indicativa · modelo de Sabine", dec=",")
OG = ("APP PARA IPHONE — GRÁTIS", "Ouça. Analise. Corrija.", "Decibelímetro · RT60 · Mapa de ruído · LiDAR · Afinador")

HOME = dict(
    title="Acoustic Detector — Decibelímetro, RT60 e acústica de ambientes",
    desc="App gratuito para iPhone: decibelímetro, analisador, afinador, RT60 por banda de oitava, mapa de ruído, parede dupla e escaneamento LiDAR do ambiente. Offline, em 7 idiomas.",
    eyebrow="Medição sonora e tratamento acústico",
    h1="Ouça. Analise. Corrija.",
    lead="O Acoustic Detector transforma seu iPhone em uma ferramenta de acústica. Meça o ruído, analise o espectro, escaneie um ambiente com LiDAR e descubra onde ele ressoa e quanta espuma acústica adicionar. Grátis, 100 % offline, em 7 idiomas.",
    meta=[("iOS 17+", "necessário"), ("", "iPhone"), ("7 idiomas", "PT · FR · EN · ES · DE · IT · JA"), ("Grátis", "compra única opcional")],
    hero_alt="Reverberação de um ambiente por banda de oitava, comparada à meta de 0,50 segundo",
    new_badge="Novidades", new_h="Versão 1.4.1: um afinador gratuito, mais estável e preciso",
    new_lead="O Acoustic Detector traz um afinador gratuito para violão, ukulele, violino e mais, e agora fala português, francês, inglês, espanhol, alemão, italiano e japonês.",
    new=["Afinador gratuito: violão/guitarra (5 afinações), ukulele (com sol grave e barítono), violino, viola, violoncelo, bandolim, banjo e modo cromático para a voz",
         "Versão 1.4.1: leitura mais estável que ignora medições erráticas, agulha mais precisa, indicador de nível do sinal",
         "Notas em Dó Ré Mi ou em C D E conforme o idioma, e uma vibração quando está afinado",
         "7 idiomas, à escolha no menu principal",
         "RT60 por banda de oitava, de 125 Hz a 4 kHz, em relação à sua meta",
         "Mapa de ruído: meça em vários pontos e obtenha um mapa de calor",
         "Parede dupla: frequência de ressonância e isolamento por frequência",
         "O app é gratuito: decibelímetro, analisador, afinador, tabela de medições e exportação em PDF incluídos; Tratamento e Calculadoras com uma compra única"],
    new_status="Versão 1.4.1 disponível na App Store.",
    callout="<p><strong>Uma ferramenta indicativa, apresentada com honestidade.</strong> O microfone do iPhone não é um instrumento certificado: os valores exibidos são estimativas, claramente identificadas como tais, com calibração manual opcional para refinar a precisão. O Acoustic Detector não substitui um instrumento calibrado para conformidade regulatória oficial.</p>",
    what_eyebrow="O que o Acoustic Detector faz", what_h="Um único aparelho para medir e corrigir",
    what=[("Decibelímetro ao vivo", "Nível em dB em tempo real, com mínimo, média e máximo, calibração do microfone e histórico em cores.", ""),
          ("Analisador de espectro", "Análise de frequências ao vivo, com detecção de tom puro: frequência, período e comprimento de onda.", ""),
          ("Tratamento de um ambiente", "O tempo de reverberação (RT60) em relação à meta do seu uso, e a quantidade de espuma acústica a adicionar.", ""),
          ("Escaneamento LiDAR", "No iPhone Pro, varra o ambiente: as dimensões e a área de cada parede são preenchidas sozinhas.", ""),
          ("Mapa de ruído", "Meça o nível em vários pontos e veja as zonas calmas e barulhentas em um mapa de calor.", ""),
          ("Afinador", "Violão, ukulele, violino, viola, violoncelo, bandolim, banjo, ou qualquer nota e sua voz: agulha e cents ao vivo.", "Novo"),
          ("Calculadoras", "Soma de fontes sonoras, pressão sonora, frequência e comprimento de onda, e cálculo de parede dupla.", "")],
    shots_eyebrow="Prévia", shots_h="Sóbrio, preciso, pronto para o campo",
    shots=[("menu", "Menu principal", "Menu"), ("tuner", "Afinador de violão com agulha e cents", "Afinador"), ("sono", "Decibelímetro e calibração do microfone", "Decibelímetro"),
           ("freq", "Reverberação por frequência e absorção dos materiais", "RT60 por frequência"),
           ("noise", "Mapa de calor do ruído de um ambiente", "Mapa de ruído"), ("wall", "Cálculo de parede dupla", "Parede dupla"),
           ("lidar", "Escaneamento do ambiente com LiDAR", "Escaneamento LiDAR"), ("table", "Tabela de medições", "Tabela")],
    who_eyebrow="Para quem", who_h="Da obra ao estúdio",
    who=[("Empreiteiros e técnicos", "Meça o ruído de um local, verifique uma divisória, estime o tratamento de um ambiente antes de orçar."),
         ("Estúdios, músicos, áudio", "Calcule a reverberação de uma sala, encontre os graves problemáticos, estime a espuma a adicionar e afine seus instrumentos."),
         ("Casa e escritório", "Home theater, home office, sala de reuniões: descubra onde ressoa e o que fazer a respeito.")],
    nums=[("5", "Modos de medição"), ("6", "Bandas de oitava"), ("10", "Materiais acústicos"), ("100 %", "Offline")],
    price_eyebrow="Preço", price_h="Grátis, com uma compra única opcional",
    plans=[("Grátis", "$ 0", ["Decibelímetro ao vivo e calibração", "Analisador de espectro", "Afinador (violão, violino, voz e mais)", "Tabela de medições", "Exportação em PDF com gráficos"], False),
           ("Completo", "CA$ 4,99, compra única", ["Tudo do gratuito", "Tratamento: RT60, absorção, escaneamento LiDAR, mapa de ruído", "Calculadoras: fontes, pressão, ondas, parede dupla", "Sem assinatura"], True)],
    price_note="O preço é exibido pela App Store conforme o seu país. Se você comprou o app antes de ele se tornar gratuito, tudo continua desbloqueado automaticamente.",
    cta_h="Pronto para ouvir o seu ambiente?", cta_p="O Acoustic Detector está disponível na App Store, para iPhone. Grátis, com uma compra única opcional.",
)

FEATURES = dict(
    title="Recursos — Acoustic Detector",
    desc="Decibelímetro, analisador, afinador, RT60 por banda de oitava, absorção, mapa de ruído, escaneamento LiDAR, parede dupla e relatórios em PDF: tudo o que o Acoustic Detector faz.",
    eyebrow="Recursos", h1="Tudo o que você precisa para medir e corrigir um ambiente",
    lead="O microfone e a câmera do iPhone, usados para medir, calcular e documentar a acústica de um local — sem sair do app, sem conexão.",
    m_eyebrow="Medir", m_h="Grátis: o necessário para medir no dia a dia",
    measure=[("Decibelímetro ao vivo", "Nível em dB em tempo real, com mínimo, média e máximo, e dois estilos de gráfico (Festival, Estúdio)."),
             ("Calibração do microfone", "Compare com um decibelímetro de referência e ajuste: cada medição indica se está calibrada ou estimada."),
             ("Analisador de espectro", "Análise de frequências ao vivo (FFT) e classificação do som: puro, complexo ou ruído."),
             ("Tom puro", "Para um tom puro, a frequência, o período e o comprimento de onda são calculados para você."),
             ("Histórico em cores", "Cada sessão é salva com sua curva: verde, amarelo ou vermelho conforme o nível."),
             ("Tabela de medições", "O registro de todas as suas medições, com filtro, ordenação e exportação em relatório PDF com gráficos.")],
    s_eyebrow="Em detalhe", s_h="Cada ferramenta, de perto",
    spots=[
        ("tuner", "Afinador", "Afine de ouvido, ou deixe a agulha fazer isso.",
         ["Violão/guitarra (5 afinações), ukulele (incluindo sol grave e barítono), violino, viola, violoncelo, bandolim e banjo", "Modo cromático para a voz e qualquer nota", "Agulha com cents ao vivo e uma escala de ajuste fino de ±10 cents, com vibração quando está afinado", "Leitura estabilizada que ignora medições erráticas, com indicador do nível do sinal", "Frequência de referência ajustável de 430 a 450 Hz, e gratuito"]),
        ("sono", "Decibelímetro, calibração e histórico", "O decibelímetro mais simples de abrir no campo.",
         ["Nível ao vivo, mínimo, média e máximo", "Calibração do microfone com um instrumento de referência, com o estado da calibração anotado em cada medição", "Histórico de sessões com sua curva em cores", "Compartilhe a imagem ou adicione à tabela de medições"]),
        ("freq", "Reverberação por frequência", "Saber onde o ambiente tem problema, não só se tem.",
         ["RT60 por banda de oitava, de 125 Hz a 4 kHz, em relação à meta do seu uso (escritório, estúdio, sala de reuniões, home theater)", "As bandas acima da meta são sinalizadas, com uma dica para os graves", "Curvas de absorção de cada material do ambiente, entre 10 materiais", "Modelo de Sabine e coeficientes típicos: uma estimativa indicativa"]),
        ("lidar", "Do escaneamento à espuma a adicionar", "Escaneie o ambiente e deixe o app fazer as contas.",
         ["No iPhone Pro (LiDAR), uma varredura preenche as dimensões e a área de cada parede", "Sem LiDAR, digite as dimensões à mão: todo o resto funciona", "Esquema 3D isométrico do ambiente, incluído na tabela e no relatório PDF", "A quantidade de espuma acústica a adicionar para atingir a meta", "Medição do RT60 ao vivo com uma breve rajada de ruído"]),
        ("noise", "Mapa de ruído", "Ver onde há barulho em um ambiente num piscar de olhos.",
         ["Toque na planta do ambiente e meça cinco segundos em cada ponto", "Mapa de calor das zonas calmas e barulhentas", "Nível mais calmo, média (Leq) e nível mais barulhento", "Salvo na tabela de medições e no relatório PDF"]),
        ("calc", "Calculadoras acústicas", "As fórmulas do ofício, sem papel nem calculadora.",
         ["Soma de fontes sonoras: quantos dB juntas", "Nível de pressão sonora a partir da pressão em pascals", "Frequência, período e comprimento de onda", "Cada resultado é adicionado à tabela com um toque"]),
        ("wall", "Parede dupla", "Estimar o isolamento de uma parede antes de construí-la.",
         ["Cálculo massa-mola-massa a partir da massa de cada folha e da profundidade da cavidade", "Frequência de ressonância e isolamento por banda de oitava", "Com ou sem lã mineral, e folhas desacopladas como opção", "Estimativa indicativa, não um índice Rw/STC certificado"]),
        ("table", "Tabela de medições e relatórios PDF", "Tudo o que você mede fica organizado e compartilhável.",
         ["Cada medição é adicionada a uma tabela central, filtrável por tipo", "Relatório PDF com gráficos e esquema 3D do ambiente", "Salve um gráfico em Fotos ou compartilhe com as ferramentas do iOS", "Tudo fica no seu aparelho: sem conta, sem servidor"]),
    ],
    cmp_h="Grátis ou Acoustic Detector Completo", cmp_cols=("", "Grátis", "Completo"),
    cmp=[("Decibelímetro ao vivo e calibração", "✓", "✓"), ("Analisador de espectro", "✓", "✓"), ("Afinador", "✓", "✓"), ("Tabela de medições e exportação em PDF", "✓", "✓"),
         ("RT60 do ambiente e espuma a adicionar", "—", "✓"), ("RT60 por banda de oitava e absorção", "—", "✓"), ("Escaneamento LiDAR do ambiente", "—", "✓"),
         ("Mapa de ruído", "—", "✓"), ("Calculadoras e parede dupla", "—", "✓")],
    cmp_note="“Acoustic Detector Completo” é uma compra única de CA$ 4,99, sem assinatura.",
)

DOWNLOAD = dict(
    title="Download — Acoustic Detector",
    desc="Baixe o Acoustic Detector na App Store para iPhone. Grátis, com uma compra única opcional.",
    eyebrow="Download", h1="Acoustic Detector na App Store",
    lead="Um app nativo para iOS, feito para ser usado direto no campo: na obra, no estúdio ou em casa.",
    req_eyebrow="Requisitos", req_h="Verifique a compatibilidade do seu aparelho",
    specs=[("Sistema", "iOS 17+"), ("Aparelho", "iPhone"), ("Preço", "Grátis"), ("Compra única", "CA$ 4,99")],
    req_note="O Acoustic Detector funciona em qualquer iPhone com iOS 17 ou mais recente. O escaneamento LiDAR do ambiente exige um iPhone Pro com sensor LiDAR (iPhone 12 Pro e mais recentes); nos outros iPhones, as dimensões do ambiente são digitadas à mão.",
    sheet_eyebrow="Ficha técnica", sheet_h="Informações do app",
    sheet=[("Desenvolvedor", "JDG inc., Quebec, Canadá"), ("Identificador", "JDG-inc.AcousticDetector"), ("Idiomas", "Português (Brasil), francês, inglês, espanhol, alemão, italiano e japonês"), ("Exportações", "Relatório PDF com gráficos, compartilhamento de imagens")],
    faq_eyebrow="Perguntas frequentes", faq_h="Antes de baixar",
    faq=[("Meu aparelho é compatível?", "Se o seu iPhone roda iOS 17 ou mais recente, ele é compatível. O LiDAR não é necessário: ele apenas acrescenta o escaneamento automático do ambiente."),
         ("Quanto custa?", "O app é gratuito. A compra única opcional “Acoustic Detector Completo” (CA$ 4,99) desbloqueia Tratamento e Calculadoras, sem assinatura."),
         ("Funciona offline?", "Sim. As medições e os cálculos são feitos no aparelho, sem conta nem servidor. Só a compra e a restauração passam pela App Store."),
         ("As medições são precisas?", "O microfone do iPhone fornece uma estimativa, não uma medição certificada. Uma calibração manual opcional permite refinar o resultado."),
         ("Em quais idiomas?", "Em português (Brasil), francês, inglês, espanhol, alemão, italiano e japonês, à escolha no menu principal."),
         ("Como obter ajuda?", f'Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a> ou visite a página de <a href="contact.html">Contato</a>.')],
    cta_h="Pronto para começar?", cta_p="O Acoustic Detector está disponível na App Store.",
)

CONTACT = dict(
    title="Contato e suporte — Acoustic Detector", desc="Ajuda, perguntas frequentes, compra e restauração, imprensa: escreva-nos sobre o app Acoustic Detector. Toda mensagem recebe resposta.",
    eyebrow="Contato", h1="Contato e suporte",
    lead="Uma dúvida, um erro a relatar ou uma sugestão? Toda mensagem é lida e recebe uma resposta pessoal.",
    blocks=[("Suporte e dúvidas", "Se puder, informe o modelo do seu iPhone e a versão do iOS.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector">{EMAIL}</a>'),
            ("Imprensa e mídia", "Um kit de imprensa (apresentação, recursos, ficha técnica) está disponível sob pedido.", f'<a href="mailto:{EMAIL}?subject=Acoustic%20Detector%20-%20Imprensa">{EMAIL}</a>'),
            ("Desenvolvedor", "O Acoustic Detector é concebido e desenvolvido pela JDG inc.", "JDG inc. — Quebec, Canadá"),
            ("App", "Disponível na App Store para iPhone com iOS 17+.", '<a href="download.html">Ver a página de download</a>')],
    faq_h="Perguntas frequentes",
    faq=[("As medições em decibéis são calibradas?", "Não, por padrão. O Acoustic Detector usa o microfone integrado do iPhone para estimar o nível sonoro — é indicativo, não um instrumento certificado. O modo Decibelímetro oferece uma calibração manual opcional com um instrumento de referência para ajustar a precisão."),
         ("O escaneamento LiDAR funciona em todos os iPhones?", "Não, apenas nos modelos Pro com sensor LiDAR (iPhone 12 Pro e mais recentes). Nos outros iPhones, as dimensões do ambiente são digitadas manualmente no modo Tratamento — todas as funções de cálculo continuam disponíveis."),
         ("O cálculo de reverberação (RT60) é exato?", "O modo Tratamento oferece duas estimativas: um cálculo teórico (fórmula de Sabine, com base nas suas dimensões e materiais, por banda de oitava) e uma medição ao vivo com uma rajada de ruído. Ambas são aproximações úteis para orientar um tratamento acústico, não medições de laboratório."),
         ("Minhas medições são enviadas para algum lugar?", 'Não. Nenhum dado sai do seu aparelho. Veja nossa <a href="privacy.html">política de privacidade</a>.'),
         ("O app está disponível em português?", "Sim. O Acoustic Detector está disponível em 7 idiomas (português, francês, inglês, espanhol, alemão, italiano e japonês): um botão de idioma no menu principal troca o idioma da interface, independentemente do idioma do seu iPhone."),
         ("Existe assinatura?", "Não. O Acoustic Detector é gratuito: o decibelímetro, o analisador, o afinador, a tabela de medições e a exportação em PDF estão incluídos. Tratamento e Calculadoras são desbloqueados com uma compra única (CA$ 4,99), sem assinatura. As atualizações estão incluídas. Se você comprou o app antes de ele se tornar gratuito, tudo continua desbloqueado automaticamente."),
         ("Como restaurar minha compra?", "Em um iPhone novo ou após reinstalar, abra Tratamento ou Calculadoras e toque em “Restaurar compras”, com o mesmo ID Apple da compra."),
         ("O app existe para Android?", "Por enquanto não — o Acoustic Detector está disponível para iPhone (iOS 17 ou mais recente).")],
    cta_h="Uma dúvida antes de baixar?", cta_p="Escreva-nos — respondemos diretamente, sem rodeios.",
)

PRIVACY = dict(
    title="Política de privacidade — Acoustic Detector", desc="O Acoustic Detector não coleta, transmite nem compartilha nenhum dado pessoal: sem conta, sem servidor, sem rastreadores.",
    eyebrow="Privacidade", h1="Política de privacidade", updated="Última atualização: 2 de outubro de 2026",
    note="<p><strong>Em resumo:</strong> o Acoustic Detector não coleta, transmite nem compartilha nenhum dado pessoal. O app funciona totalmente offline, sem conta, sem servidor e sem serviços de terceiros.</p>",
    sections=[
        ("Microfone", "<p>O app usa o microfone do seu aparelho para as funções de Decibelímetro, Analisador, Afinador e a medição de reverberação (RT60) do modo Tratamento. O som captado é processado inteiramente no seu aparelho, em tempo real, para calcular um nível sonoro, um espectro de frequências ou uma nota. Nenhuma gravação de áudio é salva, transmitida ou compartilhada — apenas os valores numéricos calculados (dB, Hz, segundos) podem ser salvos localmente se você optar por adicionar uma medição à tabela.</p>"),
        ("Câmera e LiDAR", "<p>Nos iPhones Pro, o modo Tratamento oferece um escaneamento opcional do ambiente por câmera e LiDAR (via RoomPlan e ARKit da Apple) para medir automaticamente as dimensões de um ambiente. Esse escaneamento é processado inteiramente no seu aparelho — nenhuma imagem, vídeo ou dado de escaneamento é enviado a lugar algum. Apenas as dimensões e áreas calculadas são mantidas, localmente, se você optar por usá-las.</p>"),
        ("Dados salvos localmente", "<p>As medições que você opta por salvar (sessões do Decibelímetro, entradas da tabela de medições) ficam armazenadas apenas no espaço privado do app no seu aparelho. Esses dados nunca saem do seu aparelho, a menos que você escolha explicitamente exportá-los (relatório PDF, compartilhamento de imagem) pelos recursos nativos de compartilhamento do iOS — nesse caso, o destino é você quem controla.</p>"),
        ("Fotos", "<p>Se você optar por salvar um gráfico ou relatório na sua biblioteca de fotos, o app solicita uma permissão somente para adicionar, limitada a essa única ação. Ele não consulta nem acessa o restante da sua biblioteca de fotos.</p>"),
        ("Compra no app", "<p>Tratamento e Calculadoras são desbloqueados com uma compra única, processada inteiramente pela Apple (App Store). O desenvolvedor não recebe nem seus dados de pagamento nem sua identidade: o app apenas pergunta à Apple se a compra está ativa no seu ID Apple.</p>"),
        ("Sem rastreamento, sem terceiros", "<ul><li>Nenhuma conta de usuário, nenhuma identificação necessária.</li><li>Nenhum servidor remoto; nenhuma conexão é necessária para usar o app (apenas a compra e a restauração passam pela App Store).</li><li>Nenhuma ferramenta de análise, publicidade ou rastreamento de terceiros está integrada ao app.</li><li>Nenhum dado é vendido, compartilhado ou monetizado de qualquer forma.</li></ul>"),
        ("Contato", f'<p>Para qualquer dúvida sobre esta política de privacidade, escreva-nos em <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>'),
    ])
