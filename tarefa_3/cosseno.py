"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 3
"""

"""
Escreva um algoritmo que use um loop do tipo for para calcular a série cos(x).
Implemente esse algoritmo em Python (cosseno.py).
Use a função factorial da biblioteca math.
Teste com x = π/6 e com x = π/3, com a série indo até o termo (x^4)/4! inclusive.
Compare com o valor de cos(x) do módulo math. Copie o resultado do programa para o arquivo (cosseno.py), como comentário no final.
"""

import math # Importa a biblioteca math

x1 = math.pi/6 # valor de teste pi/6
x2 = math.pi/3 # valor de teste pi/3

def cos(x):
    """Função que dado um valor x retorna o seu cosseno, calculado a partir da sua série até n=2"""
    c = 0
    for n in range(0,3): # como range() calcula a diferença, precisamos adicionar +1 para calcular n = 0,1,2 
        c += ((-1)**n *x**(2*n))/(math.factorial(2*n))
    return c

cosx1 = cos(x1) # calculamos e guardamos em uma variavel para futuro uso, é uma boa prática de programação que evita calculos repetidos
cosx2 = cos(x2) # valor série de x2
func_cosx1 = math.cos(x1) # valor da função da bilbioteca math
func_cosx2 = math.cos(x2) # valor da função da bilbioteca math
diferenca1 = cosx1-func_cosx1 # a diferença das duas 1
diferenca2 = cosx2-func_cosx2 # a diferença das duas 2

print(f'x: pi/6, Série: {cosx1}, Função: {func_cosx1}, Diferença: {diferenca1}')
print(f'x: pi/3, Série: {cosx2}, Função: {func_cosx2}, Diferença: {diferenca2}')

#x: pi/6, Série: 0.8660538834157472, Função: 0.8660254037844387, Diferença: -2.847963130847564e-05
#x: pi/3, Série: 0.501796201500181, Função: 0.5000000000000001, Diferença: -0.001796201500180894