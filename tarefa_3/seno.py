"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 3
"""

"""
Escreva um algoritmo que use um loop do tipo for para calcular a série sin(x).
Implemente esse algoritmo em Python (seno.py).
Use a função factorial da biblioteca math.
Teste com x = 1.2 e com a série indo até o termo (x^5)/5! inclusive.
Compare com o valor de sin(1.2) do módulo math.
"""

import math # importa a bilbioteca math

x = 1.2 # Valor de teste

def sen(x):
    """Função que dado um valor x retorna o seu seno, calculado a partir da sua série até n=2"""
    c = 0
    for n in range(0,3): # como range() calcula a diferença, precisamos adicionar +1 para calcular n = 0,1,2
        c += ((-1)**n * x**(2*n+1))/(math.factorial(2*n+1))
    return c

# calculamos e guardamos em uma variavel para futuro uso, é uma boa prática de programação que evita calculos repetidos

senx = sen(x) # valor da série de taylor do x
func_sinx = math.sin(x) # valor da função da bilbioteca math
diferenca = senx-func_sinx # a diferença das duas 

print(f'X: 1.2, Série: {senx}, Função: {func_sinx}, Diferença: {diferenca}')

#X: 1.2, Série: 0.9327359999999999, Função: 0.9320390859672263, Diferença: 0.0006969140327736101