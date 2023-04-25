from utils.correlation import correlation
from utils.hist_expansion import histogram_expansion
from utils.stats import fit0_255

import numpy as np


def sobel(image, offset=0, use_zero=True):
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
