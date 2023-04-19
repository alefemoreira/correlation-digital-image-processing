import numpy as np
from utils.stats import median
from utils.correlation import neighborsRGB

def median_filter(image, dim, pivot, use_zero=True):
    m, n = dim
    output = np.array(image, 'uint8')

    if m % 2 == 0 or n % 2 == 0 or m <= 0 or n <= 0:
        return None
    
    for i in range(len(image)):
        for j in range(len(image[0])):
            neighbors = neighborsRGB(image, (i, j), dim, pivot, use_zero)
            if neighbors == None:
                output[i][j] = (0, 0, 0)
                return

            r, g, b = neighbors
            output[i][j][0] = median(r)
            output[i][j][1] = median(g)
            output[i][j][2] = median(b)

    return output
