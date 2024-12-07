from math import acos,sin,cos,radians # funções usadas da biblioteca math

R = 6371.01 # raio médio da terra 

#Distancias 'Rio de janeiro': (-22.9035,-43.2096), 'Juiz de Fora' : (-21.7578, -43.3485), 'Maturín':(9.7339, -63.1891)

def distancia(t1,g1,t2,g2):
    t1,g1 = radians(t1),radians(g1) #transformando de graus para radianos
    t2,g2 = radians(t2),radians(g2) #transformando de graus para radianos
    d = R * acos((sin(t1)*sin(t2)) + (cos(t1)*cos(t2)*cos(g1-g2))) #formula para calcular a distância 
    return d

print('-'*57)
print("Programa que calcula a distância de dois pontos da terra")
print('Distância entre Rio de janeiro e Juiz de Fora: %.2f km' %(distancia(-22.9035,-43.2096,-21.7578, -43.3485)))
print('Distância de acordo com o Google maps: 128.32 km')
print('Distância entre Rio de janeiro e Maturín: %.2f km' %(distancia(-22.9035,-43.2096,9.7339, -63.1891)))
print('Distância de acordo com o Google maps: 4234.34 km')
print('-'*57)