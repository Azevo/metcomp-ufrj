print("Programa que soma os primeiros 'n' impares \n")

print('-'*40)
c = 0  # contador zerado
r = [] # lista dos números impares
n = int(input('Número interiro positivo: '))
while len(r) < n:
    c += 1 # contador aumenta
    if c%2 != 0 : # se tiver resto da divisao é impar 
        r.append(c) # lista adiciona o numero impar
print(f'Primeiros naturais ímpares: {r}')
print(f'Somatório é igual a: {sum(r)}')