"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um algoritmo para encontrar o valor de x para a equação ax2 + bx + c = 0 para
quaisquer valores de a, b e c reais. Implemente este algoritmo escrevendo um programa
segundoGrau.py. Ele deve atender as seguintes especificações:

    a)solicitar a digitação dos coeficientes da equação pelo teclado e parar o programa caso a=0, escrevendo na tela uma mensagem que deixe claro o motivo;

    b)escrever na tela o número e o tipo (real ou complexa) de raízes existentes;

    c)as raízes devem ser claramente indicadas, inclusive as partes reais e imaginarias das soluções complexas. Ex:

    d)Teste seu programa usando valores para os coeficientes que cubram todas as possibilidades, inclusive se a = 0. Coloque os testes realizados como comentário ao final do programa.
"""

import sys # Importe da biblioteca sys para levantar erros em caso de operação fora do escopo
import math # Importa a biblioteca math para usar funções matematicas

print("Algoritmo para encrontrar o valor de x para a equacao ax² + bx + c = 0")
a,b,c = int(input('a: ')),int(input('b: ')),int(input('c: '))

if a==0:
    sys.exit('Não é uma equação de segundo Grau')
delta = ((b**2)-4*a*c)
print('a equação %5.2f x**2 + %5.2f x + %5.2f possui:' %(a,b,c))
if delta < 0:
    re = -b/(2*a)
    img = (math.sqrt(4*a*c-(b**2)))/(2*a)
    print('duas raizes complexas: %5.2f +- %5.2f i' %(re,img))
else:
    r1 = (-b + math.sqrt(delta))/(2*a)
    r2 = (-b - math.sqrt(delta))/(2*a)
    if r1==r2:
        print('uma raiz real: %5.2f' %(r1))
    else:
        print('duas raizes reais: %5.2f e %5.2f' %(r1,r2))