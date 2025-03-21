"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um programa (MDC.py), que, dados dois números inteiros M e N, imprima o maximo divisor comum (MDC) entre eles.
(Ex: se M = 10 e N = 14 imprime: “O MDC entre 10 e 14 é 2”)
"""

def MDC(n1,n2):
    lista1 = []
    lista2 = []
    for i in range (n1,1,-1): # vai diminuindo do proprio numero até 2, coletando todos os numeros divisiveis
        if i!=n1 and n1%i==0:
            lista1.append(i)
    for i in range (n2,1,-1):
        if i!=n2 and n2%i==0:
            lista2.append(i)
    for i in lista1:
        for j in lista2:
            if i==j:
                return i

n1 = int(input('NUMERO1: '))
n2 = int(input('NUMERO2: '))

print(f'O MDC entre {n1} e {n2} é {MDC(n1,n2)}')