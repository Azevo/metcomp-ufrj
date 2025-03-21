'''
Daniele ＾▽＾

b) O código Cria a função taylor_log(x, N) que retorna a aproximação de log⁡(1+x) com N termos da série de Taylor. ✓

c) Para um valor de x, ele imprime:
O valor de log⁡(1+x) usando a biblioteca math. ✓
O valor obtido pela série de Taylor até N. ✓
A diferença entre a série de Taylor e math.log(1+x). ✓
O valor do termo N+1 da série. ✓
O código roda o programa para x=−0.5 e x=1.5 com N=1,2,4,6. ✓

d)O código plota o gráfico comparando log⁡(1+x) com as aproximações da série de Taylor para N=1,2,4,6 cobrindo o intervalo −0.5<x<1.5. ✓

'''

import numpy as np
import matplotlib.pyplot as plt
#import math
import sys


"""FUNÇÔES"""
def taylor_log(x,N):
    '''
    Calcula a serie de taylor para a função ln(1+x) até o expoente N
    '''
    log = 0
    for n in range(1,(N+1)):
        log += ((-1)**(n+1))*((x**n)/n) #Formula da serie de taylor
    return log


def erro_relativo(x,n):
    """
    Calcula e retorna o valor absoluto do erro revalivo da serie de taylor, sendo o erro do enesimo termo é ele mesmo (n) menos o termo seguinte (n+1)
    """
    return abs((taylor_log(x,n))-(taylor_log(x,n+1))) #Calculo do valor absoluto do erro de acordo com a tarefa 6


def tabela_log(x):
    '''
    Função que para um dado x e n, imprime uma tabela com o valor da função ln(1+x), série de taylor para n = 1 2 4 e 6 e o erro relativo
    '''
    print(f'Para x = {x} | Bilbioteca math: {np.log(1+x):.4f}') #Por conta do valor mostado ser pequeno, sao usadas 4 casas decimais
    for n in [1,2,4,6]:
        print(f'Série para n= {n}: {taylor_log(x,n):.4f} | Erro: +-{erro_relativo(x,n):.4f}') #Por conta do valor mostado ser pequeno, sao usadas 4 casas decimais




"""INTRUÇÔES"""
print("Programa Série de Taylor - ln(1+x)")


print('MANUAL\n *Escreva o valor de x para receber uma tabela comparando a função ln(1+x) e sua série de Taylor no valor x')


print(" *O programa gera automaticamente o gráfico da função e das séries de Taylor\n *Para SAIR do programa: Digite 'q' ou 'quit' no valor de x")






"""ALGORITMO"""
while True:
    x = input("Valor de x ( ou 'q' para sair ): ")
    if x == 'q' or x == 'quit': #Permite sair do laço infinito
        break
    if float(x)<-1: # Impede o erro de ln() de um valor negativo
        sys.exit('Erro de Dominio, X deve ser maior que -1')
    tabela_log(float(x)) #função da tabela
    print(43*'-') # barra separadora
    plt.title("Serie de Taylor - ln(1+x)")
    x = np.arange(-0.5,1.5,0.01)
    math_y = [np.log(1+x) for x in x] # para cada valor do array x, calcula a função ln(1+x)
    plt.plot(x,math_y,'g-',label="ln(1+x)") 
    plt.plot(x,taylor_log(x,1),'r-',label="N = 1")
    plt.plot(x,taylor_log(x,2),'b-',label="N = 2")
    plt.plot(x,taylor_log(x,4),'c-',label="N = 4")
    plt.plot(x,taylor_log(x,6),'y-',label="N = 6")
    plt.ylabel('ln(1+x)')
    plt.xlabel('x')
    plt.grid() # coloca as grades no fundo para facilitar a leitura do grafico
    plt.legend(loc="upper left") # coloca a legenda no canto superior esquerdo, onde não a nenhuma linha do grafico
    plt.savefig('log.png') # salva o grafico como um png
    plt.show()
"""
Para x = -0.5 | Bilbioteca math: -0.6931
Série para n= 1: -0.5000 | Erro: +-0.0681
Série para n= 2: -0.6250 | Erro: +-0.0265
Série para n= 4: -0.6823 | Erro: +-0.0046
Série para n= 6: -0.6911 | Erro: +-0.0009


Para x = 1.5 | Bilbioteca math: 0.9163
Série para n= 1: 1.5000 | Erro: +-0.5413
Série para n= 2: 0.3750 | Erro: +-0.5837
Série para n= 4: 0.2344 | Erro: +-0.8368
Série para n= 6: -0.1453 | Erro: +-1.3792

"""
"""
JHL:
- Usando-se as funções do numpy para arrays, pode-se evitar laços e ser mais eficiente: Ex.: math_y = np.log(1 + x)
- Fala em erro relativo, mas usa o erro absoluto
-  O erro seria entre o valor da biblioteca math e taylor_log(x,n). Este erro deveria ser comparado com o termo de ordem N+1. Quando não sabemos o valor exato, usamos o termo de ordem N+1 como estimativa do erro.
Nota: 5,0/6,0
"""

