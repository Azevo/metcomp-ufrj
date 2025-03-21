"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um programa (divisores.py) que, dado um número inteiro positivo, liste os divisores desse número na tela e também o número de divisores.
Exemplo: Para n = 20, a saída deverá ser Divisores: 1, 2, 4, 5, 10, 20 (total = 6).
"""

def divisores(numero):
    """Função que dado um numero devolve uma lista de todos os seu divisores"""
    lista = [] #lista que recebera os divisores
    for divisor in range(1,numero+1): # de 1 a n, se não houver resto de divisão então é um divisor e o numero é coletado
        if numero%divisor==0:
            lista.append(divisor)
    return lista

numero = int(input('Número: ')) # recebe numero
if numero <= 0: # para numeros fora de escopo
    print('Número precisa ser positivo')
else:
    lista_divisores = divisores(numero)
    print(f'Divisores: {str(lista_divisores)[1:-1]} (total = {len(lista_divisores)})')




