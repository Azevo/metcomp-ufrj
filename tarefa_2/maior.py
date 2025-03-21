"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um algoritmo para descobrir o maior numero entre um conjunto de números que vai sendo fornecido para o programa atraves do teclado. Suponha que a quantidade de números seja conhecida (pode por exemplo, entrar com essa quantidade pelo teclado).
Escreva um programa em Python que implemente este algoritmo para um conjunto de três números. 
"""

lista = []
for i in range(1,4):
    num = input(f'{i}º Número: ')
    lista.append(num)

for numero in range(0,len(lista)-1):
    """O loop passa de um em um lendo o numero, mudando o valor do numero lido se o prox for maior"""
    if lista[numero] > lista[numero+1] : lista[numero+1] = lista[numero] # se o prox numero for menor, recebe o valor do anterior
    # não é preciso um else

print(f'O maior número é: {lista[-1]}')
