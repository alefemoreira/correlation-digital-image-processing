import time

from numpy import ndarray
from PIL import Image
from src.utils.correlation import correlation


def box_11x11(image: ndarray, offset=0, use_zero=True):
    start = time.time()

    # [1/121]*121 vai repetir o 1/121 121 vezes no array da mascara
    out_image = correlation(
        image, [1 / 121] * 121, (11, 11), (6, 6), offset, use_zero)

    end = time.time()
    print("Tempo de execução do filtro Box 11x11: ", end - start)
    return out_image


def box_1x11_11x1(image: ndarray, offset=0, use_zero=True):
    start = time.time()
    out_image = correlation(
        image, [1 / 11] * 11, (1, 11), (1, 6), offset, use_zero)

    out_image = correlation(
        out_image, [1 / 11] * 11, (11, 1), (6, 1), offset, use_zero)

    end = time.time()
    print("Tempo de execução do filtro Box11x1(Box1x11(Image)): ", end - start)

    output = Image.fromarray(out_image)
    output.show()
