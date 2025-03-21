"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um programa (circulo1.py) em Python que lê as coordenadas x, y (sendo
ambos > 0) de um ponto e diga se este ponto pertence à região H da figura, ou seja,
x² + y² ≤ 1
"""

import sys # Biblioteca opcional para garantir que apenas numeros serão lidos do teclado

x,y = input('X: '), input('Y: ')
try:
    x = float(x) # tenta converter o valor lido em um float, caso de erro o programa para
    y = float(y)
except:
    sys.exit("Não são numeros") # mendagem de erro
if x < 0 or y < 0: # Ambos precisam ser inteiros
    print(x,y)
    print("Não são números validos")
elif (x**2+y**2)**(1/2) <= 1: # Verifica se as coordenada fazem parte do semicirculo
    print('Ponto pertence a area H')
else:
    print('Ponto não pertence a area H')