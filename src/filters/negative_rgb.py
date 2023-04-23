import numpy as np

from utils.rgb_inversion import rgb_inversion

def negative_rgb(image):
    """
    Recebe uma imagem e aplica o negativo nas 3 bandas de cores

    :param image: Um ndarray que representa a imagem a ser tratada
    :return: Um ndarray com o negativo nas 3 bandas
    """
    output = np.array(image)

    for i in range(len(image)):
        for j in range(len(image[0])):
            output[i][j] =  rgb_inversion(image[i][j])

    return output
