from utils.correlation import correlation
from utils.hist_expansion import histogram_expansion
from utils.stats import fit0_255

import numpy as np


def sobel(image, offset=0, use_zero=True):
    """Aplica tanto o filtro de sobel vertical quanto o horizontal depois há a soma desses dois resultados 
    e a normalização de valores e a aplicação da expansão de histograma

    Args:
        image (ndarray): Imagem no formato ndarray
        offset (int, optional): offset com valor padrão  0.
        use_zero (bool, optional): Extensão por zero com padrão True.

    Returns:
        ndarray: Imagem no formato nd array com 2 filtros de sobel aplicados e com expansão de histograma
    """
    output = np.array(image, 'uint8')
    v = correlation(
        image, [-1, 0, 1, -2, 0, 2, -1, 0, 1], (3, 3), (1, 1), offset, use_zero)
    h = correlation(
        image, [-1, -2, -1, 0, 0, 0, 1, 2, 1], (3, 3), (1, 1), offset, use_zero)

    for i in range(len(image)):
        for j in range(len(image[0])):
            r1, g1, b1 = h[i][j]
            r2, g2, b2 = v[i][j]
            output[i][j] = (fit0_255(fit0_255(r1) + fit0_255(r2)),
                            fit0_255(fit0_255(g1) + fit0_255(g2)),
                            fit0_255(fit0_255(b1) + fit0_255(b2)))

    return histogram_expansion(output)
