"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 3
"""

"""
Em 1888 Johannes Rydberg publicou a fórmula que fornece os comprimentos de onda λ das linhas de emissão do átomo de hidrogênio:
    1/λ = R(1/m² - 1/n²)
onde R é a constante de Rydberg R = 1.097 x 10^-2 nm^-1 e m e n são inteiros positivos.
Para um dado valor de m, teremos uma série de linhas para todos os valores de n > m.
As 3 primeiras séries, m = 1, 2, 3 são conhecidas como séries de Lyman, Balmer e Paschen.
Os valores de λ das 5 primeiras linhas de cada série são:
 ____________________________________________________________
    Serie para m = 1    Serie para m =2    Serie para m =3
 ____________________________________________________________
        121.54 nm           656.34 nm        1875.24 nm
        102.55 nm           486.17 nm        1281.91 nm
        97.23 nm            434.08 nm        1093.89 nm
        94.96 nm            410.21 nm        1005.01 nm
        93.76 nm            397.04 nm        954.67 nm
 ____________________________________________________________

Escreva um algoritmo para o cáculo de λ e implemente-o em Python no programa Ryd-
berg.py. Seu programa deve ter como saída a tabela acima, ou seja, calcular os valores
de λ das cinco primeiras linhas para m = 1, 2 e 3.
"""
R = 1.097e-2 # Constante de Rydberg em nm^-1
series = {} # dicionario que recebera a posição e valores das séries na tabela
M=3 # Número de colunas
N=5 # Número de Linhas
t = [] # lista que vai servir como a "matriz" do topo da tabela
info = [] # lista que recebera as informações das séries para imprimir 
print('-'*(M*18)) # divisor visual para organização

for m in range(1,1+M): # gera o calculo para M valores, começando em 1
    for n in range(1+m,1+m+N): #para cada m terá N valores maiores que ele 
        f = 1/((R)*((1/(m**2))-(1/(n**2)))) #formula dada no enunciado
        series[(m,n-m)]=f #cria uma "matriz" com M colunas e N linhas, feito assim para se adequar a diferentes Ns e Ms
    t.append(f' Série m={str(m):10s}')

print(''.join(t)) # imprime a legenda no topo da tabela (serie m=1 , ..., serie m=M)
print('-'*(M*18)) # divisor visual para organização

for j in range (1,N+1): # transporta as colunas em linhas para gerar a imagem da tabela
    for i in range(1,M+1):
        serie = f'{series[i,j]:-7.2f}'
        info.append(f'{serie} mn {' '*8}')
    info.append('\n')
    if j==(N):
        info.pop() #Quando é o ultimo valor, remove o '\n' e não pula a linha
print(''.join(info))
print('-'*(M*18))