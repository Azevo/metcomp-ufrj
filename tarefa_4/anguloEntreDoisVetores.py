import numpy as np
import math
import sys

#APRESENTAÇÂO E INFORMAÇÔES SOBRE O PROGRAMA
titulo = "Programa que calcula o ângulo entre dois vetores do R³"

print(f"{titulo}\n\nAtenção! Coloque as coordenadas X, Y, Z dos vetores\nna respectiva ordem e separadas por um espaço entre elas:")

#FUNÇÕES
def modulo(r): # Função para gerar o módulo de um tuple que representa um vetor
    f = lambda x=float: x**2 #Função anonima para elevar os valores
    r = map(f,r)
    r = (sum(r))**(1/2) # Soma e tira a raiz do vetor
    return r

def escalar(r,s):
   esc = r * s
   esc = sum(esc)
   return esc #Retorna o escalar dos vetores r e s

def angulo(r,s):
    cos0 = escalar(r,s)/(modulo(r)*modulo(s)) # Define o cos do angulo como a formula com escalar e modulos
    if math.isclose(cos0,1) or math.isclose(cos0,-1): # A formula pode resultar em +-1.0000002 e essa função isclose() é fundamental para não dar erro e englobar os vetores dependentes
        return 0 #Vetores Linearmente dependentes, não há ângulo entre eles
    elif math.isclose(cos0,0): # Engloba a possibilidade de vetores perpendiculares, cos do angulo = 0
        return 90 #Vetores Perpendiculares, ângulo de 90°
    return math.degrees(math.acos(cos0))

#ALGORITMO
vetor_lido_1 = [float(n) for n in input("Vetor 1: ").split()]# Separa o texto, transforma em float e coloca em uma tuple
vetor_lido_2 = [float(n) for n in input("Vetor 2: ").split()]# Separa o texto, transforma em float e coloca em uma tuple
vetor_1, vetor_2 = np.array(vetor_lido_1),np.array(vetor_lido_2)
if len(vetor_1) != 3 or len(vetor_2) != 3: # Impede o uso de vetores não pertencentes ao R³
    sys.exit('Vetor deve ter 3 coodenadas')


print(f'Vetor 1 Módulo: {modulo(vetor_1):.2f}') # Mostra o módulo do vetor 1, para fins informativos
print(f'Vetor 2 Módulo: {modulo(vetor_2):.2f}') # Mostra o módulo do vetor 2, para fins informativos
print(f'Escalar dos vetores 1 e 2: {escalar(vetor_1,vetor_2)}') # Mostra o escalar, para fins informativos
print(f'O ângulo entre os vetores: {angulo(vetor_1,vetor_2):3.2f}°') # Calcula e imprime o angulo dos vetores
print('-'*60) # Barra que separa o fim dessa resposta de uma possivel proxima, fins de organização

#RESPOSTAS DE ALGUMAS ENTRADAS
'''
Vetor 1: 1 2 3 
Vetor 2: 4 5 6
Vetor 1 Módulo: 3.74
Vetor 2 Módulo: 8.77
Escalar dos vetores 1 e 2: 32.0
O ângulo entre os vetores: 12.93°

Vetor 1: -1 -2 -3
Vetor 2: -4 -5 -6
Vetor 1 Módulo: 3.74
Vetor 2 Módulo: 8.77
Escalar dos vetores 1 e 2: 32.0
O ângulo entre os vetores: 12.93°

Vetor 1: 1 1 1
Vetor 2: 2 2 2
Vetor 1 Módulo: 1.73
Vetor 2 Módulo: 3.46
Escalar dos vetores 1 e 2: 6.0
O ângulo entre os vetores: 0.00°

Vetor 1: 1 0 1
Vetor 2: 0 1 0
Vetor 1 Módulo: 1.41
Vetor 2 Módulo: 1.00
Escalar dos vetores 1 e 2: 0.0
O ângulo entre os vetores: 90.00°

Vetor 1: 1 4 2
Vetor 2: 6 2 9
Vetor 1 Módulo: 4.58
Vetor 2 Módulo: 11.00
Escalar dos vetores 1 e 2: 32.0
O ângulo entre os vetores: 50.59°
'''
