from numpy import loadtxt, mean # importa apenas as funções usadas
notas = loadtxt("notas.txt") # carrega as notas do arquivo como um array
N = 0 # Número de alunos
media = 0 # Média dos alunos
aprovados = 0 # Quantidade de alunos aprovados
reprovados = 0 # Quantidade de alunos reprovados
desvio = 0 # Desvio padrão
soma = 0 # somatorio das notas
soma_quad = 0 # somatorio quadratico das notas
for n in notas: # separa aprovados de reprovados e calcula o total de alunos
    if n >= 7:
        aprovados += 1
    elif n < 3:
        reprovados += 1
    N += 1
    soma += n
    soma_quad += n**2
media = soma/N # calcula a média
desvio = ((soma_quad/(N-1))-(N*media**2)/(N-1))**(1/2) # Desvio padrão de acordo com a fórmula dada
print('-'*29)
print('Programa que Imprime úteis\nInformações de um notas.txt')
print(f' Número de alunos: {N} \n  aprovados: {aprovados:3d} \n  reprovados: {reprovados:2d}')
print(f' Média dos alunos: {media:.2f} \n Média pelo numpy: {mean(notas):.2f} \n desvio padrão: {desvio:.2f}')
print('-'*29)

'''
Resultado:
-----------------------------
Programa que Imprime úteis
Informações de um notas.txt
 Número de alunos: 78 
  aprovados:  14 
  reprovados: 13
 Média dos alunos: 5.15 
  desvio padrão: 2.06
-----------------------------
'''
