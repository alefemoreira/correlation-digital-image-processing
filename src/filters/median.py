import numpy as np
from utils.stats import median
from utils.correlation import neighborsRGB

def median_filter(image, dim, pivot, use_zero=True):
    m, n = dim
    output = np.array(image, 'uint8')

    # mxn impar
    if m % 2 == 0 or n % 2 == 0 or m <= 0 or n <= 0:
        return None
    
    for i in range(len(image)):
        for j in range(len(image[0])):
            # Buscando a vizinhaça
            neighbors = neighborsRGB(image, (i, j), dim, pivot, use_zero)

            # Caso haja alguma vizinhaça fora da imagem o pixel não é calculado
            if neighbors == None:
                output[i][j] = (0, 0, 0)
                continue

            # Fazendo a mediana para as 3 bandas
            r, g, b = neighbors
            output[i][j][0] = np.median(r)
            output[i][j][1] = np.median(g)
            output[i][j][2] = np.median(b)

    return output
