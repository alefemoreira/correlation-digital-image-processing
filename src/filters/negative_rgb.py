from numpy import ndarray


def negative_rgb(image: ndarray):
    """
    Recebe uma imagem e aplica o negativo nas 3 bandas de cores

    :param image: Um ndarray que representa a imagem a ser tratada
    :return: Um ndarray com o negativo nas 3 bandas
    """

    # Nova imagem
    negative_image = image.copy()

    for line in range(len(image)):
        for column in range(len(image[0])):
            r, g, b = image[line][column][0], image[line][column][1], image[line][column][2]

            # Novo pixel
            negative_image[line][column] =  [255 - r, 255 - g, 255 - b]

    return negative_image
