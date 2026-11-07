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

    print(entrada_tratada)



def FCFS()-> float:

    return 0

def SJF(entrada_tratada: list[float]) -> float:
    lista_novos, lista_prontos, retorno = []
    duracao_total = 0
    shortest = -1

    #calcula tempo total de duração
    for i in entrada_tratada:
        duracao_total += entrada_tratada[i][1]
    
    #simula cada instante do processamento(talvez não seja a ideia mais eficiente mas foi a que eu tive)
    for instante in range (duracao_total) :
        lista_prontos, lista_novos = atualizaProntos(lista_prontos, entrada_tratada, lista_novos)

        for j in lista_prontos:
            if lista_prontos[j][1]>shortest or shortest==-1:
                shortest = lista_prontos[j][1]
            retorno.append([instante][lista_prontos[j][2]])


    return 0

def RR() -> float:
    
    return 0

def retornoMedio()-> float:
    return 0

def respostaMedio()-> float:
    return 0

def esperaMedio()-> float:
    return 0

def atualizaProntos() -> list[list[float]], list[list[float]]
    return [[0]], [[0]]




if __name__ == "__main__":
    main()
