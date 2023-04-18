import numpy as np
from numpy import ndarray


def calc_expansion(r, r_min, r_max, l):
    return np.round(((r - r_min) / (r_max - r_min)) * (l - 1))

def histogram_expansion(image: ndarray, l):
    # pegar o maximo de cada banda
    # pegar o minimo de cada banda
    # percorrer a imagem aplixando o calc_expansion nas 3 bandas de cada pixel
    pass


def get_r_min_max(image: ndarray):
    pass
