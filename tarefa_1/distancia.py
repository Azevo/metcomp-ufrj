
"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 1
"""

"""
13. A distância entre dois pontos da superfície da Terra é dada por

d = Rm x arccos(sin(t1) x sin(t2) + cos(t1) x cos(t2) x cos(g1 - g2)) 

onde (t1, g1) e (t2, g2) são a latitude e longitude de dois pontos da Terra, em graus, e Rm = 6371.01 km é o raio médio da Terra.
Faça um programa em Python chamado distancia.py que calcule essa distância dados os dois pontos em graus.
Lembre que os argumentos das funções trigonométricas devem ser em radianos, portanto seu programa deve fazer essa transformação.
Para testar seu programa, pesquise quais são a latitude, longitude e a distância entre duas cidades da sua escolha.
Verifique se seu programa dá o mesmo resultado.
Seu programa deve imprimir também os valores que vocês pesquisaram, com os nomes das cidades.
Na sua pesquisa, você provavelmente vai encontrar algo do tipo: 75◦59´32′′.
Para transformar para graus decimal faça 75 + (59/60) + (32.483/3600) que dá 75.99◦ (Sugestão: faça primeiro o item 11.)
"""

from math import acos,sin,cos,radians #Importa as funções usadas da biliboteca math

R = 6371.01 # raio médio da terra 

#Distancias 'Rio de janeiro': (-22.9035,-43.2096), 'Juiz de Fora' : (-21.7578, -43.3485), 'Maturín':(9.7339, -63.1891)

def distancia(t1,g1,t2,g2):
    """Função que dada a latitude e longitude de dois pontos na terra, calcula e retorna sua distancia"""
    t1,g1 = radians(t1),radians(g1) #transformando de graus para radianos
    t2,g2 = radians(t2),radians(g2) #transformando de graus para radianos
    d = R * acos((sin(t1)*sin(t2)) + (cos(t1)*cos(t2)*cos(g1-g2))) #formula para calcular a distância 
    return d # retorna a distancia calculada

print('-'*57)
print("Programa que calcula a distância de dois pontos da terra")
print('Distância entre Rio de janeiro e Juiz de Fora: %.2f km' %(distancia(-22.9035,-43.2096,-21.7578, -43.3485)))
print('Distância de acordo com o Google maps: 128.32 km')
print('Distância entre Rio de janeiro e Maturín: %.2f km' %(distancia(-22.9035,-43.2096,9.7339, -63.1891)))
print('Distância de acordo com o Google maps: 4234.34 km')
print('-'*57)