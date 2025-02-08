
"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 1
"""

"""
2. Escreva um programa em Python (polar.py) que, dado um par de coordenadas cartesianas em duas dimensões, x e y, calcule e imprima o par de coordenadas polares r e θ
correspondente. Imprima θ tanto em radianos como em graus.
"""

from math import atan2,pi #Importa as funções usadas da biliboteca math

def cardiais(x,y):
    """Função que dada uma coordenada x e y, calcula sua forma polar (raio + argumento)"""
    r = ((x**2)+(y**2))**(1/2)
    o = atan2(y,x) #Calcula o arcotangente de y/x entre -pi/2 e pi/2 levando em conta os sinais de ambos 
    if o < 0: o = o + (2 * pi) #Caso o angulo se encontro entre o terceiro e quarto quadrando, soma 2pi ao angulo
    print("Raio: {:.2f} Radianos: {:.2f} Graus: {:.2f}".format(r,o,o*180/pi)) #Imprime a resposta e transforma radianos em graus 



x = float(input("Coordenada X: ")) #Recebe a coordenada x
y = float(input("Coordenada Y: ")) #Recebe a coordenada y

cardiais(x,y) #Aplica as coordenadas na função