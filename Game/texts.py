storyFrames = [
    {
        "background": "static/Mexicolandia.png",
        "characters": [],
        "text": "Essa é a União das Repúblicas Sem Saúde (URSS), um país assolado por miséria e doença. Eles ficaram nessa condição pois seu presidente não acreditou nas vacinas."
    },
    {
        "background": "static/Mexicolandia.png",
        "characters": [],
        "text": "Na contramão deste país..."
    },
    {
        "background": "static/EstadosVacinados1.png",
        "characters": [],
        "text": "Temos os Estados Vacinados da América, um país que se tornou um exemplo mundial de vacinação e saúde pública."
    },
    {
        "background": "static/EstadosVacinados1.png",
        "characters": [],
        "text": "Após longos anos de luta, eles conseguiram erradicar doenças como sarampo, poliomielite e outras que assolavam a população."
    },
    {
        "background": "static/EstadosVacinados1.png",
        "characters": [],
        "text": "Dessa forma, abriram mão da vacinação, pois não havia mais doenças para combater."
    },
    {
        "background": "static/EstadosVacinados1.png",
        "characters": [],
        "text": "Por isso, eles eram extremamente rigorosos com a imigração de pessoas de outros países, especialmente aqueles que não acreditavam na vacinação."
    },
    {
        "background": "static/Mexicolandia.png",
        "characters": [],
        "text": "Você é um jovem que cresceu em União das Repúblicas Sem Saúde (URSS) e sonha em viver nos Estados Vacinados da América."
    },
    {
        "background": "static/Mexicolandia.png",
        "characters": [],
        "text": "Você decidiu que era hora de deixar União das Repúblicas Sem Saúde (URSS) e tentar a sorte nos Estados Vacinados, porém não havia como entrar sem ser vacinado."
    },
    {
        "background": "static/Mexicolandia.png",
        "characters": [],
        "text": "Portanto, você falsificou alguns certificados de vacinação e conseguiu embarcar no trem que te levaria para os Estados Vacinados."
    },
    {
        "background": "static/EstadosVacinados1.png",
        "characters": [],
        "text": "Ao chegar lá, você foi abordado por um agente de imigração que iria verificar seus documentos e encaminhado para um interrogatório(...)"
    }
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
            "Vim da União das Repúblicas Sem Saúde (URSS)!.",
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
        "text": "Mostre o cartão de vacina da Peste Bubonica. Agora.",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://bubonica",
        "outras":["https://bubonica_f1","https://bubonica_f2","https://bubonica_f3"],
        "vacina":"Peste Bubonica"
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "E o cartão da vacina contra Covid-19? Cadê?",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://covid",
        "outras":["https://covid_f1","https://covid_f2","https://covid_f3"],
        "vacina":"Covid-19"
    },{
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Mostre o cartão de vacina da Febre Amarela. Agora.",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://febre",
        "outras":["https://febre_f1","https://febre_f2","https://febre_f3"],
        "vacina":"Febre Amarela"
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "E o cartão da vacina contra HIV? Cadê?",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://hiv",
        "outras":["https://hiv_f1","https://hiv_f2","https://hiv_f3"],
        "vacina":"Virus da Imunodeficiencia Humana"
    },{
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Mostre o cartão de vacina da Poliomelite. Agora.",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://poliomelite",
        "outras":["https://poliomelite_f1","https://poliomelite_f2","https://poliomelite_f3"],
        "vacina":"Poliomelite"
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "E o cartão da vacina contra Rubéola? Cadê?",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://rubeola",
        "outras":["https://rubeola_f1","https://rubeola_f2","https://rubeola_f3"],
        "vacina":"Rubéola"
    },{
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Mostre o cartão de vacina da Tetano. Agora.",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://tetano",
        "outras":["https://tetano_f1","https://tetano_f2","https://tetano_f3"],
        "vacina":"Tétano"
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "E o cartão da vacina contra Tuberculose? Cadê?",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://tuberculose",
        "outras":["https://tuberculose_f1","https://tuberculose_f2","https://tuberculose_f3"],
        "vacina":"Tuberculose"
    },{
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Mostre o cartão de vacina da Variola. Agora.",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://variola",
        "outras":["https://variola_f1","https://variola_f2","https://variola_f3"],
        "vacina":"Varíola"
    },
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "E o cartão da vacina contra Zika? Cadê?",
        "flag": "",
        "opcoes": [
            "Não tomei, e agora ?",
            "Não tenho isso comigo agora.",
            "Tomei, mas perdi o cartão.",
            ""
        ],
        "vacinaCorreta": "https://zika",
        "outras":["https://zika_f1","https://zika_f2","https://zika_f3"],
        "vacina":"Zika"
    }
]

vacinacao_frame = [
    {
        "background": "static/mainRoom1.jpeg",
        "characters": ["static/officer_no_bg.png"],
        "text": "Vem aqui que vou te dar essa vacina que você não tomou, seu lazarento!",
        "flag": "",
        "opcoes": [
            "Pronto tomei",
            "Doi pra caramba, porra",
            "",
            ""
        ],
    }
]

ending_frames = [
    {
        "background": "static/EstadosVacinados1.png",
        "characters": [""],
        "text": "Parabéns, bem vindo aos Estados Vacinados da América, fico feliz que tenha tomado todas as vacinas.",
        "flag": "goodEnding",
    },
    {
        "background": "static/badEnding.jpeg",
        "characters": [""],
        "text": "Seu maldito, entrou no Estados Vacinas da América sem vacina. Agora trouxe a doença para todos. O país foi devastado por sua causa",
        "flag": "badEnding",
    },
    {
        "background": "static/EstadosVacinados1.png",
        "characters": [""],
        "text": "Parabéns, bem vindo aos Estados Vacinados da América, fico feliz que tenha tomado todas as vacinas.",
        "flag": "sadEnding",
    }
]