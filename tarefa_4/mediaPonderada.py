print("Programa para Média Ponderada")

print("\nAtenção! \n * Coloque os valores na respectiva ordem e separados por um espaço \n * O valor da nota deve ser informada \n * Caso não informado o valor do peso será 1 \n")

def mediaPonderada(n1,n2,peso1=1,peso2=1):
    """Recebe duas notas e dois pesos respectivos e retorna sua média ponderada, caso não informado o peso será 1"""
    return ((n1 * peso1) + (n2 * peso2)) / (peso1 + peso2)

n1p1 = list(map(float,input("Nota 1 e Peso 1 (Default = 1): ").split())) #cria uma lista de floats 
n2p2 = list(map(float,input("Nota 2 e Peso 2 (Default = 1): ").split())) #cria uma lista de floats

# Algoritmo para englobar todas as possibilidades de nota default ou não
if len(n1p1) + len(n2p2) > 3:
    media = mediaPonderada(n1p1[0],n2p2[0],n1p1[1],n2p2[1])
elif len(n1p1) == 2:
    media = mediaPonderada(n1p1[0],n2p2[0],n1p1[1])
elif len(n2p2) == 2:
    media = mediaPonderada(n1p1[0],n2p2[0],peso2=n2p2[1])
else:
    media = mediaPonderada(n1p1[0],n2p2[0])
print(f'Média: {media:.2f}\n')


'''
RESPOSTAS

Nota 1 e Peso 1 (Default = 1): 10
Nota 2 e Peso 2 (Default = 1): 10
Média: 10.00

Nota 1 e Peso 1 (Default = 1): 5 2
Nota 2 e Peso 2 (Default = 1): 5
Média: 5.00

Nota 1 e Peso 1 (Default = 1): 5  
Nota 2 e Peso 2 (Default = 1): 5 2
Média: 5.00

Nota 1 e Peso 1 (Default = 1): 7.5 2
Nota 2 e Peso 2 (Default = 1): 8.3
Média: 7.77
'''