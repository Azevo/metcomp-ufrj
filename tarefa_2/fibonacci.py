"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
DESAFIO A série de Fibonacci é uma sequencia de números inteiros, onde cada um é a soma dos dois anteriores, começando com 1 e 1. Portanto os primeiros números são: 
1, 1, 2, 3, 5, 8, 13, 21...
(Curiosidade: Essa serie aparece codificada em muitos fenómenos da natureza. Seus termos estabelecem entre si a chamada proporção áurea, muito usada nas artes e arquitetura por ser considerada agradavel aos olhos. Seu valor é φ = 1,618)
Escreva um programa (fibonacci.py) que imprima os primeiros 100 números da serie de Fibonacci
"""

print("Programa que imprime os 100 primeiros valores da Série de fibonacci")
retrasado = 0 #valores iniciais 
anterior = 1 #valores iniciais
prox = anterior + retrasado #valores iniciais    retrasado = anterior # "i" o ultimo valor, recebe o valor do "penultimo" numero da série salvo
anterior = prox # "j" o penultimo valor salvo, recebe o valor "presente" de fibonacci
    
for n in range(0,100,prox): # 'for' salta casas equivalente a soma dos ultimos valores da série
    print('%03d : %1d' %(n+1,prox)) # imprime o valor "presente" da série de fibonacci, igual a "k"
    prox = anterior + retrasado # é a soma dos ultimos valores salvos da série 
    retrasado = anterior # "i" o ultimo valor, recebe o valor do "penultimo" numero da série salvo
    anterior = prox # "j" o penultimo valor salvo, recebe o valor "presente" de fibonacci
    