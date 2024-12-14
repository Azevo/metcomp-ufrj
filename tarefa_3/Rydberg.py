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

for j in range (1,N+1):
    for i in range(1,M+1):
        serie = f'{series[i,j]:-7.2f}'
        info.append(f'  {serie:17s}')
    info.append('\n')
    if j==(N):
        info.pop() #Quando é o ultimo valor, remove o '\n' e não pula a linha
print(''.join(info))
print('-'*(M*18))