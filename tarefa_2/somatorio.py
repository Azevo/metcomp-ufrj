N = int(input("Valor de N: "))
s = 0 #somatório zerado
for n in range(1,N+1):#N+1 porque começa no 1 e range é a diferença entre os valores
    s += 1/(n**2)
print(s) # enésimo somatorio

#N=100: 1.6349839001848923
#N=1000: 1.6439345666815615
#N=10000: 1.6448340718480652