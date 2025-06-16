storyFrames = [
    {
        "background": "static/Mexicolandia.png",
        "characters": [],
        "text": "Essa é a Mexicolândia, um país assolado por miséria e doença. Eles ficaram nessa condição pois seu presidente não acreditou nas vacinas."
    }
    ,
    # {
    #     "background": "static/Mexicolandia.png",
    #     "characters": [],
    #     "text": "Na contramão deste país..."
    # },
    # {
    #     "background": "static/EstadosVacinados1.png",
    #     "characters": [],
    #     "text": "Temos os Estados Vacinados da América, um país que se tornou um exemplo mundial de vacinação e saúde pública."
    # },
    # {
    #     "background": "static/EstadosVacinados1.png",
    #     "characters": [],
    #     "text": "Após longos anos de luta, eles conseguiram erradicar doenças como sarampo, poliomielite e outras que assolavam a população."
    # },
    # {
    #     "background": "static/EstadosVacinados1.png",
    #     "characters": [],
    #     "text": "Dessa forma, abriram mão da vacinação, pois não havia mais doenças para combater."
    # },
    # {
    #     "background": "static/EstadosVacinados1.png",
    #     "characters": [],
    #     "text": "Por isso, eles eram extremamente rigorosos com a imigração de pessoas de outros países, especialmente aqueles que não acreditavam na vacinação."
    # },
    # {
    #     "background": "static/Mexicolandia.png",
    #     "characters": [],
    #     "text": "Você é um jovem que cresceu em Mexicolândia e sonha em viver nos Estados Vacinados da América."
    # },
    # {
    #     "background": "static/Mexicolandia.png",
    #     "characters": [],
    #     "text": "Você decidiu que era hora de deixar Mexicolândia e tentar a sorte nos Estados Vacinados, porém não havia como entrar sem ser vacinado."
    # },
    # {
    #     "background": "static/Mexicolandia.png",
    #     "characters": [],
    #     "text": "Portanto, você falsificou alguns certificados de vacinação e conseguiu embarcar no trem que te levaria para os Estados Vacinados."
    # },
    # {
    #     "background": "static/EstadosVacinados1.png",
    #     "characters": [],
    #     "text": "Ao chegar lá, você foi abordado por um agente de imigração que iria verificar seus documentos e encaminhado para um interrogatório(...)"
    # }
]


# Definindo os frames de jogo (playingFrames)
playingFrames = [
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Você entra em uma sala mal iluminada. Um oficial te encara com um olhar desconfiado.",
        "flag": "",
        "opcoes": [
            "O que está acontecendo aqui?",
            "Boa noite, senhor.",
            "Por que estou aqui?",
            "... [Ficar em silêncio]"
        ]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Ei, você, imigrante! De onde veio?",
        "flag": "",
        "opcoes": [
            "Vim da Mexicolândia!.",
            "Estou só de passagem, não quero confusão.",
            "E você, quem é?",
            "Prefiro não responder."
        ]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Qual é o seu nome?",
        "flag": "escolheNome",
        "opcoes": [
            "Meu nome é Maria.",
            "Pode me chamar de... João.",
            "Por que quer saber meu nome?",
            "Não tenho nome pra dar."
        ]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Cadê o comprovante da sua vacinação? Mostre agora.",
        "flag": "",
        "opcoes": [
            "Aqui está o meu cartão de vacina.",
            "Eu... perdi o comprovante.",
            "Não tenho isso comigo.",
            "Vacina? Que vacina?"
        ]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Vou dar uma olhada nos seus pertences. Abra a bolsa.",
        "flag": "",
        "opcoes": [
            "Tá bem, pode olhar.",
            "Sem chance, isso é invasão de privacidade!",
            "Calma, deixa eu te explicar primeiro.",
            "Por que precisa revistar minhas coisas?"
        ]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Hmm, isso aqui tá meio suspeito, não acha?",
        "flag": "",
        "opcoes": [
            "Não sei do que tá falando, isso é meu!",
            "Calma, posso explicar tudo direitinho.",
            "Suspeito? Você tá vendo coisa onde não tem.",
            "E o que você acha que é isso, hein?"
        ]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Quero provas de que você tá com todas as vacinas em dia.",
        "flag": "",
        "opcoes": [
            "Tomei todas, juro! Posso contar a história.",
            "Olha, eu sou saudável, isso não basta?",
            "Você não tem coisa melhor pra fazer?",
            "E se eu disser que não acredito em vacinas?"
        ]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Chega de papo. O interrogatório começa agora!",
        "flag": "startGame",
        "opcoes": [
            "Tá bem, vou cooperar.",
            "Não vou falar nada sem um advogado.",
            "Você tá exagerando, isso é só uma conversa, né?",
            "O que mais você quer de mim?"
        ]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Mostre o cartão de vacina da Covid-19. Agora.",
        "flag": "",
        "opcoes": [
            "Aqui, ó, tá tudo certinho.",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            "Covid? Isso ainda é exigido?"
        ],
        "vacinaCorreta": "covid19"
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "E o cartão da vacina contra Gripe Aviária? Cadê?",
        "flag": "",
        "opcoes": [
            "Tá aqui, olha aí.",
            "Gripe Aviária? Nunca ouvi falar.",
            "Acho que perdi esse cartão também.",
            "Vacina de gripe de passarinho? Sério isso?"
        ],
        "vacinaCorreta": "gripeAviaria"
    }
]