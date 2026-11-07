explicação de como o código está funcionando:

Passos:

1. leitura do arquivo, transforma a entrada em uma lista de processos, especificamente uma lista de listas, onde cada lista interna é uma linha da entrada(um processo), armazenando momento de chegada, tempo de duração, e id do processo
    
2. chamamos os algoritmos de escalonamento(recebe a entrada tratada, explicada no passo 1): a ideia é que o algoritmo simule o escalonamento passo a passo(instante a instante), retornando uma lista com todos os instantes do "processamento" e qual processo(id do processo) fica em execução para cada instante, funcionando como uma linha do tempo que indica qual processo o processador se ocupa em cada instante. A escolha dele ser instante a instante foi por didática, é mais facil de visualizar assim, e quando eu estava programando foi essa ideia que eu tive primeiro
    
3. chamamos as calculadoras: a calculadora recebe a linha do tempo indicada no passo 2. Com isso e com a entrada tratada do passo 1, ela consegue todas as variáveis para calcular os tempos de retorno, espera e resposta médios. Não fizemos a calculadora integrada com os algoritmos de escalonamento pq o código do calculo dos tempos médios seria igual para os 3, assim o código fica mais modularizado, também deixar o retorno dos algoritmos de escalonamento ser a linha do tempo ao invés dos tempos médios direto é algo mais didático e pode ser interessante para uma possível apresentação