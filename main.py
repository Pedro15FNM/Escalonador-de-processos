from escalonadores import FCFS, RR, SJF
from utilitarios import Media


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

    resultado_rr = RR(entrada_tratada, quantum=2)

    media_rr = Media(resultado_rr)

    media_fcfs = Media(resultado_fcfs)

    print(media_rr)
    print(media_fcfs)


if __name__ == "__main__":
    main()
