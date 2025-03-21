"""
Universidade Federal do Rio de Janeiro // Instituto de Física // Métodos Computacionais em Física I // Tarefa 6
"""

'''
Analise de medidas da constante gravitacional g - Histograma da matplotlib.pyplot.
O arquivo gravidade.txt, contem medidas experimentais da aceleração da gravidade g em cm/s2, feita por alunos na FisExpI.
Vamos fazer um histograma destes dados.
O módulo matplotlib.pyplot nos fornece o método plt.hist(valores, bins=20) que plota o histograma dos valores contidos no numpy.array valores.
Faça um programa histograma.py que:

    a) Leia os dados do arquivo gravidade.txt

    b) Faça o histograma desses valores (Rode o programa com 20 e 60 bins)

    c) Obtenha a media (µ) dos valores e o desvio padrão σ usando as funções numpy.mean(array) e numpy.std(array,ddof=1) e apresente esses valores em uma caixa no seu grafico.
'''

import numpy as np # Importa a biblioteca numpy como np
import matplotlib.pyplot as plt # Importa o modulo pyplot da biblioteca matplotlib como plt


dados = np.loadtxt("tarefa_6/gravidade.txt") # carrega os dados do arquivo txt
media = np.mean(dados) # usa a função da biblioteca numpy para calcular a média
desvio = np.std(dados,ddof=1) # usa a função da biblioteca numpy para calcular o desvio padrão
text = f'$\\mu={media:.2f}$\n$\\sigma={desvio:.2f}$' # colocar "\\" para evitar o erro "invalid escape sequence '\m'"

def grafico_gravidade(bins):
    """
    Função muito especifica para mostar os graficos do arquivo gravidade.txt com a quantidade de bins desejada
    """
    plt.hist(dados,bins=bins,color='r') # cria um grafico, color='r' controla a cor dos elementos, no caso será vermelho
    plt.title('Histograma de Gravidade') # Titulo do Grafico
    plt.xlabel("Valor da Gravidade medido") # Legenda horizontal
    plt.ylabel("Vezes que resultou") # Legenda Vertical
    plt.text(0.05,0.95,text,transform=plt.subplot().transAxes,fontsize=12, verticalalignment='top') # cria a legenda no canto superior
    plt.show() #imprime o grafico na tela

grafico_gravidade(20) # Versao com 20 bins
grafico_gravidade(60) # versao com 60 bins