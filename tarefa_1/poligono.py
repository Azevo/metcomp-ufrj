from math import tan, pi #Funções utilizadas da biblioteca math

print("Programa que calcula a área de um polígono de N lados de comprimento L")

print('-'*41) # apenas um divisor visual
N = int(input('Valor de N: '))
L = float(input('Valor de L: '))
if N < 3 or L <= 0: # Não existe Polinomio regular com menos que 3 lados ou area zero/negativa
    print('Área Impossivel ou Inexistente')
else:
    A = (N*L**2)/(4*tan(pi/N))
    print('Área do polinomio: %.2f' %A)