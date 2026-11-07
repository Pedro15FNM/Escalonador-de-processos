def main():

    entrada_tratada = []

    with open("entrada.txt", "r", encoding="utf-8") as arquivo:
        entrada = arquivo.read().splitlines()

    #print(entrada)    

    for linha in entrada:

        if linha.strip():
            linha_convertida = []

            for valor in linha.split():
                linha_convertida.append(float(valor))
        
            entrada_tratada.append(linha_convertida)

    #print(entrada_tratada)

def FCFS()-> float:

def SJF() -> float:

def RR() -> float:
    

if __name__ == "__main__":
    main()
