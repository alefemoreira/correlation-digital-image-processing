import numpy as np
from numpy import ndarray

from math import ceil
from utils.stats import fit0_255

"""
Recebe um valor numérico value e retorna o valor inteiro mais próximo de value, garantindo que 
o valor esteja dentro do intervalo de 0 a 255. Se value for menor que 0, a função retorna 0. 
Se value for maior que 255, a função retorna 255.

def fit0_255(value):
    v = ceil(value)

    if v < 0:
        return 0
    if v > 255:
        return 255

    return v
"""

"""
Recebe quatro argumentos numéricos: r, que é o valor do pixel a ser expandido; r_min e r_max, 
que são o mínimo e o máximo valores dos pixels da imagem original, respectivamente; e l, 
que é o número de níveis de intensidade que a imagem resultante deve ter. A função calcula 
a expansão do pixel r utilizando a fórmula de expansão de histograma, arredonda 
o resultado para o inteiro mais próximo e retorna o valor resultante.
"""
def calc_expansion(r, r_min, r_max, l):    

    # Força número real para garantir resultados matemáticos corretos
    # Se r_max for um número inteiro, o cálculo pode perder a precisão
    r_max = float(r_max)

    return np.round(((r - r_min) / (r_max - r_min)) * (l - 1)) # Formula da expansão de histograma


"""
Recebe uma imagem RGB representada por um array numpy multidimensional de três dimensões, 
onde a primeira dimensão representa a altura da imagem, a segunda dimensão representa a 
largura da imagem e a terceira dimensão representa as três bandas de cores (vermelho, verde e azul) da imagem. 
O argumento opcional l define o número de níveis de intensidade que a imagem resultante deve ter e é por padrão 
definido como 256.
"""
def histogram_expansion(image: ndarray, l=256):
    
    output = np.zeros_like(image)

    # Image largura e altura
    iw = image.shape[1]
    ih = image.shape[0]

    #A função começa obtendo os valores máximo e mínimo de cada banda de cores da imagem original
    maxR = image[:, :, 0].max()
    minR = image[:, :, 0].min()

    maxG = image[:, :, 1].max()
    minG = image[:, :, 1].min()

    maxB = image[:, :, 2].max()
    minB = image[:, :, 2].min()

    max = [maxR, maxG, maxB]
    min = [minR, minG, minB]

    #Percorre a imagem pixel a pixel, aplicando a função calc_expansion para cada banda de cor do pixel.
    # Linha
    for r in range(ih):
        # Coluna
        for c in range(iw):

            # Pixel [R, G, B]
            pixel = np.zeros(3)

            #Por fim, a função utiliza a função fit0_255 para garantir que o valor resultante esteja dentro do 
            #intervalo de 0 a 255 e salva o resultado na imagem de saída.
            for i in range(3):
                pixel[i] = calc_expansion(image[r, c, i], min[i], max[i], l)
                pixel[i] = fit0_255(pixel[i])

            output[r, c, :] = pixel

    #A função retorna a imagem RGB resultante com a expansão de histograma aplicada.
    return output


def get_r_min_max(image: ndarray):
    pass
