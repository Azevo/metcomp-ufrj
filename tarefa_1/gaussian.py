
"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 1
"""

"""
5. Uma das funções mais usadas em ciência e tecnologia é a função Gaussiana

f(x) = 1 /( s.((2.pi)^(1/2)) ) . e^(-1/2 . ((x-m)/s)²)

Escreva um programa em Python (gaussian.py), que calcule o valor desta função
para m = 0, s = 5 e x = 3

"""

from math import pi,e #Importa as funções usadas da biliboteca math

def gauss(m,s,x):
    """Função que calcula e impimi o resultado da função gaussiana com m s e x, o calculo está no '.format()'"""
    print('{:.2f}'.format((1/(s*((2*(pi))**(1/2))))*((e)**((-1/2)*(((x-m)/s)**2)))))
    """
    (1/(s*((2*(math.pi))**(1/2))))*((math.e)**((-1/2)*(((x-m)/s)**2))) é a formula geral gaussiana 
    para quaiquer m, s e x dadas a função
    """



gauss(0,5,3) # executa a função com os valores pedidos no enunciado