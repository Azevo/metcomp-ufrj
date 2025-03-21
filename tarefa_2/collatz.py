"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Conjectura de Collatz: Se temos um número n natural (inteiro e < 0), e realizarmos a seguinte sequencia:
    • se n for par, divida por 2
    • se n for ímpar, multiplique por 3 e some 1
O ultimo número da sequencia será sempre 1. Ex: 10, 5, 16, 8, 4, 2, 1. 
Escreva um programa (collatz.py) que imprima os elementos da sequencia e o numero de elementos, para qualquer valor de n lido do teclado.
"""

import sys # Biblioteca para levantar erros para valores fora do escopo do script

n = input('valor de n: ') # Recebe o valor n
i = [] # lista da sequencia de collatz
try:
    n = int(n) # filtra o valor lido para apenas inteiros serem aceitos
except:
    sys.exit('Não é um inteiro')
if n < 0:
    sys.exit('Não é natural maior que zero') # filtra o valor lido para apenas positivos serem aceitos
else:
    i.append(n) # adiciona o valor inicial
    while n != 1:  
        if n%2 == 0: # verifica se n é par
            n = n/2
        else:
            n = (n*3)+1
        i.append(int(n))
    print(i,'Números de elementos: %.1d'%(i.index(1)+1))

