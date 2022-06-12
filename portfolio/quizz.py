import matplotlib.pyplot as dadosGraficos


def informacao_sobre_utilizadores(arg):
    dados = {}
    for quizz in arg:
        dados[quizz.nome] = Pontuacao(quizz)

    return dados


def desenha_graficodados(arg):
    dados = informacao_sobre_utilizadores(arg)

    dadosOrdenados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=False))

    pessoa = list(dadosOrdenados.keys())
    pontuacao = list(dadosOrdenados.values())

    dadosGraficos.figure(figsize=(9, 7))

    dadosGraficos.barh(pessoa, pontuacao, color='#201120FF')

    dadosGraficos.title("Pontuação do Quizz!")
    dadosGraficos.ylabel("Participantes")
    dadosGraficos.xlabel("Pontuação")

    dadosGraficos.savefig('portfolio/static/portfolio/images/dadosGraficos.png')


def Pontuacao(input):
    pontuacao = 0

    if input.pergunta1 == "1996":
        pontuacao += 5

    if input.pergunta2 == "Js":
        pontuacao += 5

    if input.pergunta3 == "5":
        pontuacao += 5

    if input.pergunta4.lower() == "1995":
        pontuacao += 5

    return pontuacao
