import numpy as np
from numpy import ndarray


def calc_expansion(r, r_min, r_max, l):
    return np.round(((r - r_min) / (r_max - r_min)) * (l - 1))

def histogram_expansion(image: ndarray, l):
    pass
