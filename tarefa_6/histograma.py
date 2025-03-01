import numpy as np
import matplotlib.pyplot as plt


dados = np.loadtxt("gravidade.txt") # carrega os dados do arquivo txt
media = np.mean(dados) # usa a função da biblioteca numpy para calcular a média
desvio = np.std(dados,ddof=1) # # usa a função da biblioteca numpy para calcular o desvio padrão
text = f'$\\mu={media:.2f}$\n$\\sigma={desvio:.2f}$' # colocar "\\" para evitar o erro "invalid escape sequence '\m'"

print(text)

def grafico_gravidade(bins):
    """
    Função muito especifica para mostar os gravicos do arquivo gravidade.txt com a quantidade de bins desejada
    """
    plt.hist(dados,bins=bins,color='r')
    plt.title('Histograma de Gravidade')
    plt.xlabel("Valor da Gravidade medido")
    plt.ylabel("Vezes que resultou")
    plt.text(0.05,0.95,text,transform=plt.subplot().transAxes,fontsize=12, verticalalignment='top') # cria a legenda no canto superior
    plt.show()


grafico_gravidade(20) # Versao com 20 bins
grafico_gravidade(60) # versao com 60 bins