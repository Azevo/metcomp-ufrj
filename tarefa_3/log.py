"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 3
"""

"""
Escreva um algoritmo que use um loop do tipo for para calcular a série log(x).
Implemente esse algoritmo em Python (log.py). Teste com x = 1.2 e com a série indo até o termo correspondente a n = 3, inclusive. 
Compare com o valor de ln(1.2) do módulo math.
Copie o resultado do programa para o arquivo (log.py), como comentário no final.
"""

import math # importa a bilbioteca math

x = 1.2 # valor do x a ser calculado nas funções

def log(x):
    """Função que dado um valor x retorna o seu log calculado a partir da sua série até n=3"""
    c = 0
    for n in range(1,4): # somatorio até n = 3, mas o range() é apenas a diferença ou seja 4 - 1 = 3, poderia ser um while
        a = 2*n-1
        c += (1/a)*((x-1)/(x+1))**a
    return 2*c


# calculamos e guardamos em uma variavel para futuro uso, é uma boa prática de programação que evita calculos repetidos

logx = log(x) # valor da série de taylor do x
func_logx = math.log(x) # valor da função da bilbioteca math
diferenca = logx-func_logx # a diferença das duas 

print(f'X: {x}, Série: {logx}, Função: {func_logx}, Diferença: {logx-func_logx}')

#X: 0.5, Série: -0.6930041152263374, Função: -0.6931471805599453, Diferença: 0.00014306533360786133
#X: 1.2, Série: 0.18232154203740839, Função: 0.1823215567939546, Diferença: -1.4756546207195242e-08
#X: 3, Série: 1.0958333333333332, Função: 1.0986122886681098, Diferença: -0.002778955334776567