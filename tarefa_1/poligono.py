
"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 1
"""

"""
A área de um polígono regular de N lados de comprimento L é a soma das áreas dos N
triângulos isósceles em que pode ser dividido. Pode se mostrar que esta área do polígono
vale

A = (N . L²)/(4 tan(pi/N))

Escreva um programa em Python chamado poligono.py que calcule esta área para
dados valores de L e N .
"""

from math import tan, pi #Importa as funções usadas da biliboteca math

print("Programa que calcula a área de um polígono de N lados de comprimento L")

print('-'*41) # apenas um divisor visual
N = int(input('Valor de N: ')) # recebe uma variavel interia "N". inteira pois não a poligonos de 1.5 faces
L = float(input('Valor de L: ')) # recebe uma variavel real "L"
if N < 3 or L <= 0: # Não existe Polinomio regular com menos que 3 lados ou area zero/negativa
    print('Área Impossivel ou Inexistente')
else:
    A = (N*L**2)/(4*tan(pi/N)) # formula dada no enunciado
    print('Área do polinomio: %.2f' %A) # imprime a resposta com duas casas decimais 