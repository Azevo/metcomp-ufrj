print("Programa que imprime uma tabela com temperatuas em Celcius e Fahrenheit")
c = -20 # temperatura inicial do enunciado, caso mudada a tabela pode ou não ficar desorgaizada

print('-'*26) # apenas para remeter uma tabela
while c  <= 40: #loop até a temperatura final desejana, caso mudada a tabela pode ou não ficar desorgaizada
    print(f"| {c:6.2f} Cº  : {float(c) * 1.8 + 32:6.2f} Fº |") # format considerando um float grande para a tabelar ficar organizada
    c = c + 5 # taxa de quanto a temperatura vai aumentar, essa pode ser alterada conforme desejar
print('-'*26) # apenas para remeter uma tabela