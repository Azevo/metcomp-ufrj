"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 3
"""

"""
Determinação da constante gravitacional g
    (a) Copie o arquivo (gravidade.txt), que contém medidas experimentais da aceleração da gravidade g em cm/s^2 .
    (b) Escreva um algoritmo e implemente o programa em Python (gravidade.py) que leia esses números para um array e imprima:
        * o número de medidas realizadas. Esse número deve ser obtido através de um contador.
        * a média das medidas µ, com uma casa decimal. Essa média deve ser calculada no programa através da soma explícita das notas.
        * o desvio padrão σ (com uma casa decimal) , dado por σ² = [Calculo que eu não vou botar aqui]
        * o número de alunos que passaram direto: nota ≥ 7, indicando o percentual entre parêntesis.
        * o percentual de medidas no intervalo µ ± σ.
    (c) O módulo numpy oferece as funções min, max, sum, len para array. Compare seus resultados com o dos métodos numpy.mean(array) e numpy.std(array,ddof=1).
"""

from numpy import loadtxt, mean, std # loadtxt carrega o arquivo, mean calcula a média e std é para o desvio padrão

medidas = loadtxt("tarefa_3/gravidade.txt") # carrega as notas do arquivo como um array

N = 0 # Número de medidas µ
media = 0 # Média µ das medidas de gravidade
intervalado = 0 # Quantidade de medidas dentro do intervalo µ ± σ
desvio = 0 # Desvio padrão σ
soma = 0 # somatorio das medidas
soma_quad = 0 # somatorio quadratico das medidas

media_numpy = mean(medidas) # media calculada pelo modulo da bilbioteca numpy (mais preciso)
desvio_padro_numpy = std(medidas,ddof=1) # desvio padrao calculado pelo modulo da bilbioteca numpy (mais preciso)

limite_sup = media_numpy + desvio_padro_numpy # valor da µ+σ
limite_inf = media_numpy - desvio_padro_numpy # valor da µ-σ

for medida in medidas: # separa os valores dentro do intervalo e calcula o total de medidas
    if medida >= limite_inf and medida <= limite_sup:
        intervalado += 1
    N += 1
    soma += medida
    soma_quad += medida**2 # soma quadratica
media = soma/N # calcula a média µ
desvio = ((soma_quad/(N-1))-(N*media**2)/(N-1))**(1/2) # Desvio padrão de acordo com a fórmula dada

print('-'*37)
print(f' Número de medidas realizadas: {N} \n Medidas no intervalo µ ± σ: {intervalado:1d} ({intervalado*100/N:.0f}%)')
print(f' Média das medidas: {media:.1f} \n Média pelo numpy: {media_numpy:.1f} \n Desvio padrão: {desvio:.1f} \n Desvio padrão numpy: {std(medidas):.1f}')
print('-'*37)

'''
Resultado:
-------------------------------------
 Número de medidas realizadas: 30 
 Medidas no intervalo µ ± σ: 19 (63%)
 Média das medidas: 985.9 
 Média pelo numpy: 985.9 
 Desvio padrão: 2.4 
 Desvio padrão numpy: 2.3
-------------------------------------
'''
