"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 3
"""

"""
Notas: Média, aprovados e reprovados
    (a) Copie o arquivo (notas.txt), que contém as notas dos alunos de uma turma.
    (b) Escreva um algoritmo e implemente o programa em Python (notas.py) que leia esses números para um array e imprima:
        * o número de alunos da turma. Esse número deve ser obtido através de um contador.
        * a média da turma µ, com uma casa decimal. Essa média deve ser calculada no programa através da soma explícita das notas.
        * o desvio padrão σ (com uma casa decimal) , dado por σ² = [Calculo que eu não vou botar aqui]
        * o número de alunos que passaram direto: nota ≥ 7, indicando o percentual entre parêntesis.
        * o número de alunos reprovados direto: nota < 3, indicando o percentual entre parêntesis.
    (c) O módulo numpy oferece as funções min, max, sum, len para array. Compare seus resultados com o dos métodos numpy.mean(array) e numpy.std(array,ddof=1).
        Copie o resultado do programa para o arquivo (notas.py), como comentário no final.
"""

from numpy import loadtxt, mean, std # loadtxt carrega o arquivo, mean calcula a média e std é para o desvio padrão

notas = loadtxt("tarefa_3/notas.txt") # carrega as notas do arquivo como um array

N = 0 # Número de alunos
media = 0 # Média dos alunos
aprovados = 0 # Quantidade de alunos aprovados
reprovados = 0 # Quantidade de alunos reprovados
desvio = 0 # Desvio padrão
soma = 0 # somatorio das notas
soma_quad = 0 # somatorio quadratico das notas

for nota in notas: # separa aprovados de reprovados e calcula o total de alunos
    if nota >= 7:
        aprovados += 1
    elif nota < 3:
        reprovados += 1
    N += 1
    soma += nota
    soma_quad += nota**2
media = soma/N # calcula a média
desvio = ((soma_quad/(N-1))-(N*media**2)/(N-1))**(1/2) # Desvio padrão de acordo com a fórmula dada

print('-'*29)
print(f' Número de alunos: {N} \n  aprovados: {aprovados:3d} ({aprovados*100/N:.0f}%) \n  reprovados: {reprovados:2d} ({reprovados*100/N:.0f}%)')
print(f' Média dos alunos: {media:.2f} \n Média pelo numpy: {mean(notas):.2f} \n Desvio padrão: {desvio:.2f} \n Desvio padrão numpy: {std(notas,ddof=1):.2f}')
print('-'*29)

'''
Resultado:
-----------------------------
 Número de alunos: 78 
  aprovados:  14 (18%) 
  reprovados: 13 (17%)
 Média dos alunos: 5.15 
 Média pelo numpy: 5.15 
 Desvio padrão: 2.06 
 Desvio padrão numpy: 2.05
-----------------------------
'''
