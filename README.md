Implementação de algoritmos de Escalonamento de processos. Trabalho da disciplina de Sistemas Operacionas.

O projeto implementa:
 - FCFS: First-Come, First-Served
 - SJF: Shortest Job First
 - RR: Round Robin (com quantum = 2)

O programa suporta três formas de leitura do arquivo de processos, na seguinte ordem de prioridade:

1. Argumento via linha de comando:passando o caminho do arquivo diretamente na execução.
   python3 main.py caminho/para/arquivo.txt

2. Redirecionamento da entrada padrão (stdin): enviando o conteúdo do arquivo pelo fluxo padrão do terminal.
   python3 main.py < caminho/para/arquivo.txt

3. Arquivo padrão no diretório: executando o script sem argumentos, caso exista um arquivo chamado *entrada.txt* na mesma pasta do main.py.
   python3 main.py

Cada linha do arquivo deve conter dois números inteiros separados por espaço, indicando respectivamente o tempo de chegada e a duração (pico) de cada processo. Linhas em branco são ignoradas.

0 20
0 10
4 6
4 8