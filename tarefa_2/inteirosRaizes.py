"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um programa (inteirosRaizes.py) em Python que imprima os 20 primeiros números inteiros e suas raízes quadradas em duas colunas, alinhe tambem os números decimais. 
Use um loop do tipo while.
"""

from math import sqrt # Importa apenas a função raiz quadrada da biblioteca math

numero = 1 # valor inicial

while numero <= 20: # loop até 20
    print('| %2d : %1.2f |' %(numero,sqrt(numero))) # imprime a tabela devidamente formatada
    numero += 1 # incrementa o numero em 1