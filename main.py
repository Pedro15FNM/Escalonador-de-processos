#GRUPO: PEDRO FRANÇA NUNES MOREIRA E LEONARDO SOUZA LEITE
import os
import sys
from escalonadores import FCFS, RR, SJF
from utilitarios import Media


def main():

#==LEITURA DA ENTRADA==#
    #Lê o arquivo e retorna uma lista de linhas do arquivo
    def ler_entrada() -> list[str]:
        # Argumento via terminal: python3 main.py arquivo.txt
        if len(sys.argv) > 1:
            with open(sys.argv[1], "r", encoding="utf-8") as arquivo:
                return arquivo.read().splitlines()

        # Redirecionamento via stdin: python3 main.py < arquivo.txt
        if not sys.stdin.isatty():
            conteudo = sys.stdin.read()
            if conteudo.strip():
                return conteudo.splitlines()

        # Fallback para arquivo local padrão: python3 main.py
        if os.path.exists("entrada.txt"):
            with open("entrada.txt", "r", encoding="utf-8") as arquivo:
                return arquivo.read().splitlines()

        raise FileNotFoundError("Nenhum arquivo de entrada foi informado ou encontrado.")

#==TRATAMENTO DA ENTRADA==#
    entrada_tratada = []
    contador = 0

    entrada = ler_entrada()

    for linha in entrada:
        if linha.strip(): #se a lista não estiver vazia aciona o contador e inicializa a linha convertida
            contador += 1
            linha_convertida = []
            
            #adiciona os valores na linha convertida
            for valor in linha.split():
                linha_convertida.append(int(valor))

            linha_convertida.append(contador)#adiciona o id
            entrada_tratada.append(linha_convertida)#adiciona a linha em uma lista maior

    # o resoltado final é uma lista de listas de inteiros
    # esas listas de inteiros representam os processos e tem 3 indicies: 
    # 0 é o momento de chegada, 1 é a duração, e 2 é o id

#==CHAMADA DAS FUNÇÕES DE ESCALONAMENTO E EXIBIÇÃO NA TELA DO RESULTADO==#
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
