import numpy as np
from numpy import ndarray

from utils.stats import fit0_255

def calc_expansion(r, r_min, r_max, l):

    # Força número real para garantir resultados matemáticos corretos
    # Se r_max for um número inteiro, o cálculo pode perder a precisão
    r_max = float(r_max)

    return np.round(((r - r_min) / (r_max - r_min)) * (l - 1))


def histogram_expansion(image: ndarray, l=256):
    # pegar o maximo de cada banda
    # pegar o minimo de cada banda
    # percorrer a imagem aplicando o calc_expansion nas 3 bandas de cada pixel

    output = np.zeros_like(image)

    # Image width and height
    iw = image.shape[1]
    ih = image.shape[0]

    maxR = image[:, :, 0].max()
    minR = image[:, :, 0].min()
    maxG = image[:, :, 1].max()
    minG = image[:, :, 1].min()
    maxB = image[:, :, 2].max()
    minB = image[:, :, 2].min()

    max = [maxR, maxG, maxB]
    min = [minR, minG, minB]

    # Linha
    for r in range(ih):
        # Coluna
        for c in range(iw):

            # Pixel [R, G, B]
            pixel = np.zeros(3)

            for i in range(3):
                # Assuming R = G = B
                # Get the value of one channel (0 = blue)
                pixel[i] = calc_expansion(image[r, c, i], min[i], max[i], l)
                pixel[i] = fit0_255(pixel[i])

            output[r, c, :] = pixel

    return output


def get_r_min_max(image: ndarray):
    pass
