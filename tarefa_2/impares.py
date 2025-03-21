"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um programa (impares.py) que, dado um número inteiro positivo n, imprima os n primeiros naturais ímpares e sua soma.
Exemplo: Para n = 3 a saída deverá ser 1,3,5 e soma = 9
"""

contador = 0  # contador zerado
lista = [] # lista dos números impares
numero = int(input('Número interiro positivo: '))
while len(lista) < numero:
    contador += 1 # contador aumenta
    if contador%2 != 0 : # se tiver resto da divisao é impar 
        lista.append(contador) # lista adiciona o numero impar
print(f'Primeiros naturais ímpares: {str(lista)[1:-1]}') # transforma a lista em uma string e imprime do segundo ao penultimo caractere (tudo menos '[' e ']')
print(f'Somatório é igual a: {sum(lista)}')