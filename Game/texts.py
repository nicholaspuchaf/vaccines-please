storyFrames = [
    {
        "background": "static/Mexicolandia.png",
        "characters": [],
        "text": "Essa é a Mexicolândia, um país assolado por miséria e doença. Eles ficaram nessa condição pois seu presidente não acreditou nas vacinas."
    }
    # ,
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


playingFrames = [
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "",
        "flag":"",
        "opcoes":["Teste","Vitao","Victor","Salvador"]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Ei, você! Você não é daqui, não é?",
        "flag": "",
        "opcoes":["Teste","Vitao","Victor","Salvador"]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Como se chama?",
        "flag":"escolheNome",
        "opcoes":["Teste","Vitao","Victor","Salvador"]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Você tem algum documento que comprove sua vacinação?",
        "flag":"",
        "opcoes":["Teste","Vitao","Victor","Salvador"]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Vamos ver o que você tem aqui...",
        "flag":"",
        "opcoes":[]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Hmm, isso parece suspeito.",
        "flag":"",
        "opcoes":[]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Você vai ter que me convencer de que tomou todas as vacinas.",
        "flag":"",
        "opcoes":[]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Vamos começar o interrogatório...",
        "flag":"startGame",
        "opcoes":[]
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Me mostre o seu cartão de vacina da Covid19",
        "flag":"",
        "opcoes":["Não tenho", "Errr", "Não tomo isso ai", "Lascou"],
        "vacinaCorreta":"covid19"
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Me mostre o seu cartão de vacina da Gripe Aviária",
        "flag":"",
        "opcoes":["Não tenho", "Errr", "Não tomo isso ai", "Perdi"]
    }    
]