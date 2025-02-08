
"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 1
"""

"""
6.Escreva um programa em Python (cilindro.py) que, dados o raio R e a altura H de
um cilindro, e mais as suas respectivas incertezas, σR e σH, calcule e imprima o volume
(V ) desse cilindro com sua incerteza (σV ). (Verifique que o quadrado da incerteza no
volume e dado por σ²V = (2πR h σR)² + (πR²σH)² .)
"""

from math import pi #Importa as funções usadas da biliboteca math
from sys import exit #Importa a função exit da biliboteca sys

print("Programa que Calcula o volume de um retângulo de raio r e altura h, com suas incertezas")

def volume_cilindro(r,h,Ir,Ih):
    """Função que recebe um raio e altura com suas incetezas e retorna o volume de um cilindro com essas medidas"""
    if r <= 0 or h <= 0 or Ir <= 0 or Ih <= 0: #Garante que a area e incerteza serão positivas e diferente de zero
        exit('Todos os valores devem ser positivos e maiores que zero')
    
    v = (pi*(r**2))*(h) #Formula do volume dada no enunciado

    Ov = ((2*pi*r*h*Ir)**2)+((pi*(r**2)*Ih)**2)**(1/2) #Formula da incerteza dada no enunciado

    return v,Ov #Retornamos apenas os valores, para manter o código modular (facilmente alteravel/aplicavel)

r = float(input('Raio "r": ')) #Recebe um valor real referente ao raio
Ir = float(input('Incerteza "Ir" do Raio: ')) #Recebe um valor real referente a Incerteza do Raio
h = float(input('Altura "h" : ')) #Recebe um valor real referente a altura
Ih = float(input('Incerteza "Ih" da Altura: ')) #Recebe um valor real referente a Incerteza da altura

v,Ov = volume_cilindro(r,h,Ir,Ih) #Define V e OV como os valores retornados da função
print('O Volume do cilindro é: %.2e +/- %.2e'%(v,Ov)) #Imprime a resposta