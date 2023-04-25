import time
from numpy import ndarray
from utils.correlation import correlation

"""
A função box(image, dim, use_zero) aplica um filtro de média de ordem dim em uma imagem image, considerando 
a vizinhança definida por dim. A função retorna a imagem resultante.A função box(image, dim, use_zero) aplica 
um filtro de média de ordem dim em uma imagem image, considerando a vizinhança definida por dim. A função retorna 
a imagem resultante.
"""
def box(image, dim, use_zero):
    m, n = dim
    o = correlation(image, [1/m] * m, (m, 1), (m // 2, 0), 0, use_zero)
    output = correlation(o, [1/n] * n, (1, n), (0, n // 2), 0, use_zero)

    return output


"""
A função box_11x11(image: ndarray, offset=0, use_zero=True) aplica um filtro de média de ordem 11 em uma 
imagem image, utilizando a função correlation() para realizar a operação de filtragem. A função retorna a 
imagem resultante, e mede o tempo de execução da operação.
"""
def box_11x11(image: ndarray, offset=0, use_zero=True):
    """
    Recebe uma imagem em formato ndarray e aplica o filtro box 11x11

    :param image: Um ndarray que representa a imagem a ser tratada
    :param offset: offset a ser somado
    :param use_zero: se True a extensão por zero será usada
    :return: Um ndarray que representa uma imagem com o filtro box 11x11 aplicado
    """
    start = time.time()

    # [1/121]*121 vai repetir o 1/121 121 vezes no array da mascara
    out_image = correlation(
        image, [1 / 121] * 121, (11, 11), (5, 5), offset, use_zero)

    end = time.time()
    print("Tempo de execução do filtro Box 11x11: ", end - start, ' segundos')

    return out_image


def box_1x11_11x1(image: ndarray, offset=0, use_zero=True):
    """
    Recebe uma imagem em formato ndarray e aplica o filtro box 11x11 de forma separada em 2 filtros
    um box 11x1 e um box 1x11

    :param image: Um ndarray que representa a imagem a ser tratada
    :param offset: offset a ser somado
    :param use_zero: se True a extensão por zero será usada
    :return: Um ndarray que representa uma imagem com o filtro box 11x11 aplicado
    """

    start = time.time()

    # Box 11x_1
    out_image = correlation(
        image, [1 / 11] * 11, (1, 11), (0, 5), offset, use_zero)

    # Box 0x_11
    out_image = correlation(
        out_image, [1 / 11] * 11, (11, 1), (5, 1), offset, use_zero)

    end = time.time()
    print("Tempo de execução do filtro Box11x1(Box1x11(Image)): ",
          end - start, ' segundos')

    return out_image
