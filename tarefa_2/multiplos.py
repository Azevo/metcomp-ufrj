"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um algoritmo que, dados n e dois números inteiros positivos i e j diferentes de 0, imprime em ordem crescente os n primeiros naturais que são múltiplos de i ou de j ou de ambos.
Implemente este algoritmo em Python. Os valores de i, j e n devem ser lidos do teclado. 
O programa deve estar no arquivo multiplos.py. Exemplo: Para n = 5, i = 2 e j = 3, a saída deverá ser: 0,2,3,4,6
"""

"""PS: Exercicio mais estupido dessa lista"""

n = int(input('n: ')) # recebe n
i = int(input('i: ')) # recebe i
j = int(input('j: ')) # recebe j
lista=[]

if n<=0 or i<=0 or j<=0:
    print('Todos os valores devem ser positivos')
else:
    k=0 # numero natural que vai aumentando 
    while len(lista)<n: # aumenta o numero natural até encontar n valores multiplos de i ou j
        if k%i==0 or k%j==0:
            lista.append(k)
        k += 1
print(str(lista)[1:-1]) # imprime apenas os valores 

