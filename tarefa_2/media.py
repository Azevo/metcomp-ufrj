"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 2
"""

"""
Numa certa disciplina o aluno faz duas provas parciais, P1 e P2, e uma prova final PF, com valores entre 0 e 10, esta ultima com peso dois.
Para ser aprovado a média destas notas deve ser maior ou igual a 5.
Escreva um programa (media.py) que leia as notas P1, P2 e PF e imprima a media do aluno, com uma casa decimal, dizendo se ele está aprovado ou reprovado
"""

p1 = float(input('NOTA P1: ')) # entrada da nota 1
p2 = float(input('NOTA P2: ')) # entrada da nota 2
pf = float(input('NOTA Pf: ')) # entrada da nota 3

media = ((p1 + p2) + 2*pf)/4 #formula da média simplificada, o mesmo que ((p1+p2)/2 + 2pf)/2

if media >= 5:
    situacao = 'APROVADO'
else: 
    situacao = 'REPROVADO'

print(f'Média: {media:.1f}, Situação: {situacao}')