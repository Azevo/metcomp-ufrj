lista = [3,2,1]

for numero in range(0,len(lista)-1):
    """A função passa de um em um mudando o valor do atual se o prox for maior, caso contrario o prox vira o valor"""
    if lista[numero] > lista[numero+1] : lista[numero+1] = lista[numero] # se o prox numero for menor, recebe o valor do anterior
    # não é preciso um else

print(f'O maior número é: {lista[-1]}')
