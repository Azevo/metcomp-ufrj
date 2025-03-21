"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um programa (primo.py) que, dado um número inteiro positivo n, imprima se n é primo ou se não é primo.
O valor de n deve ser lido do teclado.
"""

def primo(n):
    'Função que dada um numero n, retorna se é primo ou não'
    if n == 1:
        return print('não é primo')
    for i in range (n,1,-1): # testa se é primo para todos os valores entre o numero testado e 2
        print(i,n)
        if i!=n and n%i==0:
            return print('não é primo')
    return print('é primo')
    
n = int(input("Numero: ")) # Recebe o numero n

primo(n)