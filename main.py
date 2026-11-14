from escalonadores import FCFS, RR, SJF
from utilitarios import Media


def main():

#==LEITURA E TRATAMENTO DA ENTRADA==#
    entrada_tratada = []
    contador = 0
    
    #abre o arquivo da entrada
    with open("entrada.txt", "r", encoding="utf-8") as arquivo:
        
        #divide o arquivo em uma lista de linhas
        entrada = arquivo.read().splitlines()

    for linha in entrada:
        if linha.strip(): #se a lista não estiver vazia aciona o contador e inicializa a linha convertida
            contador += 1
            linha_convertida = []# vai representar um processo indices: 0 é o momento de chegada, 1 é a duração, e 2 é o id
            
            #converte a linha em uma lista de seus valores(separados por espaços)
            for valor in linha.split():
                linha_convertida.append(float(valor))#adiciona o valor(a chegada e a duração)

            linha_convertida.append(contador)#adiciona o id
            entrada_tratada.append(linha_convertida)#adiciona a linha em uma lista maior

    # o resoltado final é uma lista de listas de flotas
    # esas listas de floats representam os processos e tem 3 indicies: 0 é o momento de chegada, 1 é a duração, e 2 é o id

    entrada_tratada.sort(key=lambda p: (p[0], p[2]))

#==CHAMADA DAS FUNÇÕES DE ESCALONAMENTO E EXIBIÇÃO NA TELA DO RESULTADO==#
    # Chama o algoritmo e guarda o resultado
    resultado_sjf = SJF(entrada_tratada)
    resultado_fcfs = FCFS(entrada_tratada)
    resultado_rr = RR(entrada_tratada, quantum=2)

    media_rr = Media(resultado_rr)
    media_sjf = Media(resultado_sjf)
    media_fcfs = Media(resultado_fcfs)

    print(f"FCFS {media_fcfs[0]:.1f} {media_fcfs[1]:.1f} {media_fcfs[2]:.1f}".replace(".", ","))
    print(f"SJF {media_sjf[0]:.1f} {media_sjf[1]:.1f} {media_sjf[2]:.1f}".replace(".", ","))
    print(f"RR {media_rr[0]:.1f} {media_rr[1]:.1f} {media_rr[2]:.1f}".replace(".", ","))

if __name__ == "__main__":
    main()
