
"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 1
"""

"""
Escreva um programa (notas.py) que receba um numero inteiro n correspondente á
um valor em reais. Calcule a quantidade mínima de notas que um banco deve fornecer
para atingir o valor, sabendo que as notas disponíveis sao de 100, 50, 20, 10 e 5 reais.
"""

notas = [100,50,20,10,5] #Define quais notas poderão ser usadas

def calc(valor):
    """Uma função que calcula o troco de um valor a partir das notas disponiveis em uma lista com n notas chamada 'notas' """
    for nota in notas: # para cada nota calcula o maior divisor e diminui do valor inputado
        md = valor//nota # encontra o maior divisor inteiro
        print(f'{nota:3d} | {md:3d}') #Imprime uma linha com a relação nota | quantidade, que no final resulta em uma tabela
        valor = valor-(nota*md) # diminui do valor inputado
    if valor!=0: #Em caso de resto, uma mensagem é impressa no prompt
        print("Não foi possível atingir o valor com as notas disponiveis, restando %1d reais"%(valor))

entrada = int(input("Valor em reais: "))

print('Troco:') 

calc(entrada) #Calcula e imprime a tabela