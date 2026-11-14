#GRUPO: PEDRO FRANÇA NUNES MOREIRA E LEONARDO SOUZA LEITE
def FCFS(entrada_tratada: list[list[int]]):

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
                1 execucao: t_exe
            },
            Processo 2: { 
                chegada: t_che, 
                duração: t_dur, 
                conlusão: t_con, 
                1 execucao: t_exe
            }
        }
        """
        tempo_percorrido = 0
       
        entrada_ordenada = sorted(entrada_tratada, key=lambda p: (p[0], p[2])) #ordena a entrada em ordem de chegada
       
        for i in entrada_ordenada:
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
                        "pico": i[1],
                        "conclusao": tempo_percorrido,
                        "1 execucao": primeira_execucao,
                    }
                }
            )
        return dicionario_processos

    # === CALCULAR RETORNO, RESPOSTA E ESPERA === #
    dicionario_processos = extrair_informacoes(entrada_tratada)
    for i in dicionario_processos.values():
        retorno = i["conclusao"] - i["chegada"]
        resposta = i["1 execucao"] - i["chegada"]
        espera = retorno - i["pico"]
        lista_pronta.append([retorno, resposta, espera])

    return lista_pronta


def SJF(entrada_tratada: list[list[int]]):
    lista_prontos = []

    def extrair_informacoes(entrada_tratada):
        """
        A ideia aqui é ter uma lista de processos pendentes e disponíveis.
        a lista de disponíveis é atualizada a cada mudança no tempo percorrido
        1 dos disponíveis é escolhido(seus dados são calculados e mandados para o dicionario de retorno)
        esse 1 é removido dos pendentes
        tempo percorrido é incrementado com a duração do processo escolhido
        loop reseta
        """
        pendentes = entrada_tratada.copy()
        tempo_percorrido = 0
        dicionario_processos = {}

        while pendentes:
            # filtra os processos que estão disponíveis no momento atual
            disponiveis = [p for p in pendentes if p[0] <= tempo_percorrido]

            # se não tiver ninguém disponível saltamos no tempo até a chegada do próximo processo(chegada mais proxima) e recalculamos os disponíveis
            if not disponiveis:
                tempo_percorrido = min(p[0] for p in pendentes)
                disponiveis = [p for p in pendentes if p[0] <= tempo_percorrido]

            # escolhe o processo com menor duração(desempate sendo a chegada e o ID)
            escolhido = min(disponiveis, key=lambda p: (p[1], p[0], p[2]))

            # calcula a primeira execução e a conclusão do processo, também incrementa o tempo percorrido
            primeira_execucao = tempo_percorrido
            conclusao = tempo_percorrido + escolhido[1]
            tempo_percorrido = conclusao

            # adiciona os dados do processo no dicionário
            dicionario_processos.update(
                {
                    f"Processo {escolhido[2]}": {
                        "chegada": escolhido[0],
                        "pico": escolhido[1],
                        "conclusao": conclusao,
                        "1 execucao": primeira_execucao,
                    }
                }
            )

            pendentes.remove(escolhido)

        return dicionario_processos

    # === CALCULAR RETORNO, RESPOSTA E ESPERA === #
    dicionario_processos = extrair_informacoes(entrada_tratada)
    for i in dicionario_processos.values():
        retorno = i["conclusao"] - i["chegada"]
        resposta = i["1 execucao"] - i["chegada"]
        espera = retorno - i["pico"]
        lista_prontos.append([retorno, resposta, espera])

    return lista_prontos


def RR(entrada_tratada, quantum):
    lista_prontos = [] 

    def extrair_informacoes(entrada_tratada, quantum):
        # Copiar as sublistas para não zerar os picos na lista principal
        processos_copia = sorted(
            [p.copy() for p in entrada_tratada], key=lambda p: (p[0], p[2])
        ) #ordena a entrada ordenada em ordem de chegada

        dicionario_processos = {}
        tempo_percorrido = 0
        primeira_exec = 0
        conclusao = 0

        dicionario_chegada_processos = {}  

        # Fila para gerenciar quem chegou primeiro
        fila = []

        tem_processo = True

        while tem_processo:
            # Adiciona novos processos que já chegaram no tempo atual para a fila
            for p in processos_copia:
                if p[0] <= tempo_percorrido and p[1] > 0 and p not in fila:
                    fila.append(p)

            # Tratamento de tempo ocioso (se CPU vazia, avança o tempo)
            if not fila:
                tempo_percorrido = min(
                    proc[0] for proc in processos_copia if proc[1] > 0
                )
                continue

            # === Puxa o processo atual garantindo a ordem FIFO ===
            i = fila.pop(0)

            # === CRITÉRIOS DE AVALIAÇÃO DO PROCESSO === #

            # === SALVAR PICO DO PROCESSO ANTES DE EXECUTA-LO ===
            # Se o processo ainda não passou pelo hardware, então adicione ele a lista de processos passados
            if i[2] not in dicionario_chegada_processos:
                dicionario_chegada_processos.update({i[2]: i[1]})

            # Atribuia a pico valor do pico do processo atual
            pico = dicionario_chegada_processos[i[2]]

            # === APLICAR O QUANTUM AOS PROCESSOS === #
            # Se o processo não estiver no dicionario_processos, então atribua o valor de primeira_exec...
            if f"Processo {i[2]}" not in dicionario_processos:
                primeira_exec = tempo_percorrido
            else:
                # Pega a primeira_exec que já estava salva para não sobrescrever
                primeira_exec = dicionario_processos[f"Processo {i[2]}"]["1 execucao"]

            # Evita lacuna ociosa pegando o que for menor: o quantum ou o restinho de pico do processo
            tempo_execucao = min(quantum, i[1])

            # Subtrair do tempo de pico...
            i[1] -= tempo_execucao

            # E aumentar o valor do tempo percorrido a mais um quantum (ou o que sobrou).
            tempo_percorrido += tempo_execucao

            # Conclusão sempre será igual a o tempo percorrido...
            conclusao = tempo_percorrido

            # REGRA DO RR: Processos que chegaram ENQUANTO este executava entram na fila AGORA
            for p in processos_copia:
                if p[0] <= tempo_percorrido and p[1] > 0 and p not in fila and p != i:
                    fila.append(p)

            # Se o processo atual ainda não terminou, ele volta para o final da fila
            if i[1] > 0:
                fila.append(i)

            # === ATUALIZAR O DICIONÁRIO DE PROCESSOS === #
            dicionario_processos.update(
                {
                    f"Processo {i[2]}": {
                        "chegada": i[0],
                        "1 execucao": primeira_exec,
                        "pico": pico,
                        "conclusao": conclusao,  # Valor de conslusão sempre será atualizado...
                    }
                }
            )

            """
            Para veriricar se todos os processos tem o seu tempo de pico igual a zero?
            Utilizo a função "all" em uma lista de booleanos...
            """
            tem_processo = not all(processo[1] == 0 for processo in processos_copia)

        return dicionario_processos

    # === CALCULAR RETORNO, RESPOSTA E ESPERA === #
    dicionario_processos = extrair_informacoes(entrada_tratada, quantum)
    for i in dicionario_processos.values():
        retorno = i["conclusao"] - i["chegada"]
        resposta = i["1 execucao"] - i["chegada"]
        espera = retorno - i["pico"]
        lista_prontos.append([retorno, resposta, espera])

    return lista_prontos
