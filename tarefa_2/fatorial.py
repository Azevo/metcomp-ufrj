"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um programa (fatorial.py) que, dado um inteiro não-negativo n, calcula n!
(não é para usar a função pronta) O valor de n deve ser lido do teclado.
"""

numero = int(input("valor de n: ")) # Recebe o numero pelo teclado
fatorial = numero # replica esse valor na variavel fatorial
while fatorial > 1: 
    fatorial -= 1 # subtrai 1 do fatorial
    numero = numero * fatorial
print('seu fatorial é: %d'%(numero))