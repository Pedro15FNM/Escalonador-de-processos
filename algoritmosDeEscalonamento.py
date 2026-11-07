def main():

    entrada_tratada = []
    contador = 0

    with open("entrada.txt", "r", encoding="utf-8") as arquivo:
        entrada = arquivo.read().splitlines()

    print(entrada)    

    for linha in entrada:

        if linha.strip():
            contador+=1
            linha_convertida = []

            for valor in linha.split():
                linha_convertida.append(float(valor))
        
            linha_convertida.append(contador)
            entrada_tratada.append(linha_convertida)

    #0 é o momento de chegada, 1 é a duração, e 2 é o id

    print("Entrada Tratada:", entrada_tratada)
    
    # Chama o algoritmo e guarda o resultado
    resultado_sjf = SJF(entrada_tratada)
    
    print("")
    # Imprime a simulação instante por instante
    print("Simulação SJF:", resultado_sjf)


def FCFS()-> float:

    return 0

def SJF(entrada_tratada: list[float]) -> list[list[float]]:

    lista_prontos = [] #processos prontos para executar
    retorno = [] 
    instante = 0
    cont = 0

    lista_novos = entrada_tratada.copy() #processos esperando para estarem prontos de inicio são todos

    #simula cada instante do processamento(talvez não seja a ideia mais eficiente mas foi a que eu tive)
    while cont > 0 or len(lista_novos) > 0 or len(lista_prontos) > 0:
        cont -= 1

        #pula a troca de processo se já tiver um processo em andamento
        if cont <= 0:
            
            #adiciona prontos e remove prontos dos novos
            for w in lista_novos.copy():
                if w[0]<=instante:
                    lista_prontos.append(w)
                    lista_novos.remove(w)
            
            #se não tem ninguem pronto pula a iteração
            if not lista_prontos:
                instante+=1
                continue

            shortest = [0, -1, -1] #como vamos ter que escolher o shortest job temos que resetar essa variavel logo antes(colocar em outros trechos do código gera problemas, é importante que ela resete logo antes de procurar um novo)

            #escolhe quem é o shortest job
            for j in lista_prontos:
                if j[1]<shortest[1] or shortest[1]==-1:
                    shortest = j

            #adiciona o job escolhido no retorno junto com o instante no qual ele foi escolhido
            retorno.append([instante, shortest[2]])
            lista_prontos.remove(shortest) #retira ele da lista de prontos para não ser chamado novamente
            cont=shortest[1]
            

        else:
            retorno.append([instante, shortest[2]])
        
        instante+=1

    return retorno

def RR() -> float:
    
    return 0

def retornoMedio()-> float:
    return 0

def respostaMedio()-> float:
    return 0

def esperaMedio()-> float:
    return 0




if __name__ == "__main__":
    main()
