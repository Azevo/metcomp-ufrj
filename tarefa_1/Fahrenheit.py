
"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 1
"""

"""
Escreva um programa em Python (Fahrenheit.py), que para uma temperatura dada em ◦Celsius, calcule e imprima na tela seu valor em Fahrenheit
"""

temp = float(input('Temperatura em Celsius: ')) #Recebe um valor real referente a temperatura

print("Temperatura em Fahrenheit:" + '{:.2f}'.format(((temp* 1.8)+32))) #Imprime o valor em Fahrenheit com duas casas decimais 