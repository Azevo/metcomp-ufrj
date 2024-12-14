import math
print("Programa para comparar a série de Log com a função")
def log(x):
    c = 0
    for n in range(1,4): # somatorio até n = 3 
        a = 2*n-1
        c += (1/a)*((x-1)/(x+1))**a
    return 2*c

x = 1.2 # valor do x a ser calculado nas funções

logx = log(x) # valor da série de taylor do x
func_logx = math.log(x) # valor da função da bilbioteca math
diferenca = logx-func_logx # a diferença das duas 

print(f'X: {x}, Série: {logx}, Função: {func_logx}, Diferença: {logx-func_logx}')

#X: 0.5, Série: -0.6930041152263374, Função: -0.6931471805599453, Diferença: 0.00014306533360786133
#X: 1.2, Série: 0.18232154203740839, Função: 0.1823215567939546, Diferença: -1.4756546207195242e-08
#X: 3, Série: 1.0958333333333332, Função: 1.0986122886681098, Diferença: -0.002778955334776567