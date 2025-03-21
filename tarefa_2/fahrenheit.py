"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Escreva um programa (fahrenheit.py) em Python que imprima uma tabela de conversão de ◦C para Fahrenheit, de -20◦C a 40◦C em passos de 5◦C.
As colunas da tabela devem estar alinhadas e os graus em Fahrenheit impressos com duas casas decimais
"""

print("Programa que imprime uma tabela com temperatuas em Celcius e Fahrenheit")
c = -20 # temperatura inicial do enunciado, caso mudada a tabela pode ou não ficar desorgaizada

print('-'*26) # apenas para remeter uma tabela
while c  <= 40: #loop até a temperatura final desejana, caso mudada a tabela pode ou não ficar desorgaizada
    print(f"| {c:6.2f} Cº  : {float(c) * 1.8 + 32:6.2f} Fº |") # format considerando um float grande para a tabelar ficar organizada
    c = c + 5 # taxa de quanto a temperatura vai aumentar, essa pode ser alterada conforme desejar
print('-'*26) # apenas para remeter uma tabela