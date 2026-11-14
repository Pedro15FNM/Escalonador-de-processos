#GRUPO: PEDRO FRANÇA NUNES MOREIRA E LEONARDO SOUZA LEITE
def Media(lista_prontos: list[list[int]]) -> list[float]:
    retorno_soma = 0
    resposta_soma = 0
    espera_soma = 0

    if not lista_prontos:
        return [0.0, 0.0, 0.0]

    for i in lista_prontos:
        retorno_soma += i[0]
        resposta_soma += i[1]
        espera_soma += i[2]

    retorno_medio = retorno_soma / len(lista_prontos)
    resposta_medio = resposta_soma / len(lista_prontos)
    espera_medio = espera_soma / len(lista_prontos)

    lista_medias = [retorno_medio, resposta_medio, espera_medio]

    return lista_medias
