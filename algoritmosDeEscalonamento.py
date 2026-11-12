def main():

    entrada_tratada = []
    contador = 0

    with open("entrada.txt", "r", encoding="utf-8") as arquivo:
        entrada = arquivo.read().splitlines()

    print(entrada)

    for linha in entrada:
        if linha.strip():
            contador += 1
            linha_convertida = []

            for valor in linha.split():
                linha_convertida.append(float(valor))

            linha_convertida.append(contador)
            entrada_tratada.append(linha_convertida)

    # 0 é o momento de chegada, 1 é a duração, e 2 é o id

    print("Entrada Tratada:", entrada_tratada)

    # Chama o algoritmo e guarda o resultado
    resultado_sjf = SJF(entrada_tratada)

    print("")
    # Imprime a simulação instante por instante
    print("Simulação SJF:", resultado_sjf)

    resultado_fcfs = FCFS(entrada_tratada)

    print()


def FCFS(entrada_tratada: list[list[float]]):

    lista_pronta = []

    def extrair_informacoes(entrada_tratada):
        """
        Minha estratégia foi simples, ao invés de contabilizar cada iteração decide fazer de forma mais elegante pelo algoritmo ser simples.
        Minha estratégia e separar as informações mais relevantes primeiro. Como: tempo de chegada, tempo de duração ou pico, tempo de conclusão, e tempo da primeira execução.
        Separei todas essas informações em um dicionário simples, já que as mesmas são as mais fundamentais para calcular o tempo de retorno, resposta e espera.

        Já para calcular os valores usando o FCFS, utilizei a seguinte ideia:
        Como a lista entrege será uma lista com listas contendo três valores flutuantes (tempo de chegada, tempo de duração ou de pico e o id de processo), já posso elminar o id do processo sua chegada e duração.
        Já para a conclusão, criei uma variável responsável por medir todo o tempo percorrido até o momento, ela começa com o valor zero e antes de ser atribuida a chave "conclusão" do dicionário, é somado ao tempo de execução atual do processo. A lógica é que, se o processo está sendo executado agora, ele só irá ser concluido quando seu tempo de pico terminar. Entretanto, se o processo tiver seu tempo de chegada depois do tempo percorrido atual, quer dizer que teremos algum tempo ocioso onde nenhum processo será executado, logicamente, somar a duração com o tempo percorrido atual não funciona nesse caso. Para contornar isso usamos um if para verificar se o tempo de chegada do processo é menor que o tempo percorrido até o momento. Se for menor, executamos o algorimto já descrito, se não, então somamos normalmente o seu tempo de execução mais a diferença entre o tempo percorrido até o tempo de chegada do processo atual.
        Para o tempo de primeira execução, percebi que se utilizar o tempo percorrido antes de soma-lo com o tempo de pico, vou obter o tempo exato em que o processo começa executando logo depois dos processos passados. Mas, isso somente se o tempo de chegada do processo for menor ou igual ao tempo percorrido até o momento, se não, logo o tempo de chegada está a frente do tempo percorrido, o que faz com que o seu tempo de primeira execução seja igual ao seu tempo de chegada.
        """
        dicionario_processos = {}  # Dicionário onde os valores mais importantes de cada processo serão salvos da seguinte forma:
        """
        {Processo 1: { 
                chegada: t_che, 
                duração: t_dur, 
                conlusão: t_con, 
                1 execução: t_exe
            },
            Processo 2: { 
                chegada: t_che, 
                duração: t_dur, 
                conlusão: t_con, 
                1 execução: t_exe
            }
        }
        """
        tempo_percorrido = 0
        for i in entrada_tratada:
            if i[0] <= tempo_percorrido:
                primeira_execucao = tempo_percorrido  # Se o tempo de chegada do processo for menor que o tempo percorrido até o momento, logo quando o processo anterior termina, o processo atual começa logo em seguida, tornando essa sua primeira execução.
            else:
                primeira_execucao = i[
                    0
                ]  # Se o tempo de chegada do processo for maior que o tempo percorrido até o momento, logo o processo atual só começa a ser executado no instante de sua chegada, tornando essa sua primeira execução.
            if (
                tempo_percorrido < i[0]
            ):  # Se o tempo percorrido for menor que o tempo de chegada do processo atual, significa que houve um intervalo de tempo em que não havia nenhum processo para executar, logo o tempo percorrido é atualizado com o tempo de chegada do processo atual mais seu tempo de pico.
                tempo_percorrido += (
                    i[1] + (i[0] - tempo_percorrido)
                )  # O calculo do tempo percorrido é dado pela soma da duração de pico do processo mais a diferença de tempo da chegada do processo até o tempo percorrido antes do processo surgir.
            else:
                tempo_percorrido += i[
                    1
                ]  # Tempo percorrido se atualiza com o tempo de pico do processo atual
            dicionario_processos.update(
                {
                    f"Processo {i[2]}": {
                        "chegada": i[0],
                        "duração": i[1],
                        "conclusao": tempo_percorrido,
                        "1 execução": primeira_execucao,
                    }
                }
            )
        return dicionario_processos

    dicionario_processos = extrair_informacoes(entrada_tratada)

    # Calcular lista do "tempo de retorno"
    lista_retorno = []
    for _, i in dicionario_processos.items():
        lista_retorno.append(i["conclusao"] - i["chegada"])
    # Calcular lista do "tempo de resposta"
    lista_resposta = []
    for _, i in dicionario_processos.items():
        lista_resposta.append(i["1 execução"] - i["chegada"])
    # Calcular lista do "tempo de espera"
    lista_espera = []
    cont = 0
    for _, i in dicionario_processos.items():
        lista_espera.append(lista_retorno[cont] - i["duração"])
        cont += 1

    # Calcular médias
    retorno_medio = sum(lista_retorno) / len(lista_retorno)
    resposta_medio = sum(lista_resposta) / len(lista_resposta)
    espera_medio = sum(lista_espera) / len(lista_espera)

    # Finalmente atribuir a lista pronta.
    lista_pronta.extend([retorno_medio, resposta_medio, espera_medio])

    return lista_pronta


def SJF(entrada_tratada: list[list[float]]) -> list[list[float]]:

    lista_prontos = []  # processos prontos para executar
    retorno = []
    instante = 0
    cont = 0

    lista_novos = (
        entrada_tratada.copy()
    )  # processos esperando para estarem prontos de inicio são todos

    # simula cada instante do processamento(talvez não seja a ideia mais eficiente mas foi a que eu tive)
    while cont > 0 or len(lista_novos) > 0 or len(lista_prontos) > 0:
        cont -= 1

        # pula a troca de processo se já tiver um processo em andamento
        if cont <= 0:
            # adiciona prontos e remove prontos dos novos
            for w in lista_novos.copy():
                if w[0] <= instante:
                    lista_prontos.append(w)
                    lista_novos.remove(w)

            # se não tem ninguem pronto pula a iteração
            if not lista_prontos:
                instante += 1
                continue

            shortest = [
                0,
                -1,
                -1,
            ]  # como vamos ter que escolher o shortest job temos que resetar essa variavel logo antes(colocar em outros trechos do código gera problemas, é importante que ela resete logo antes de procurar um novo)

            # escolhe quem é o shortest job
            for j in lista_prontos:
                if j[1] < shortest[1] or shortest[1] == -1:
                    shortest = j

            # adiciona o job escolhido no retorno junto com o instante no qual ele foi escolhido
            retorno.append([instante, shortest[2]])
            lista_prontos.remove(
                shortest
            )  # retira ele da lista de prontos para não ser chamado novamente
            cont = shortest[1]

        else:
            retorno.append([instante, shortest[2]])

        instante += 1

    return retorno


def RR() -> float:

    return 0


def retornoMedio() -> float:
    return 0


def respostaMedio() -> float:
    return 0


def esperaMedio() -> float:
    return 0


if __name__ == "__main__":
    main()
