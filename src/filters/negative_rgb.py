from numpy import ndarray


def negative_rgb(image: ndarray):
    # Nova imagem
    negative_image = []

    for line in image:
        new_line = []
        for pixel in line:
            r, g, b = pixel[0], pixel[1], pixel[2]

            # Novo pixel
            new_line.append([255 - r, 255 - g, 255 - b])

        # Nova linha
        negative_image.append(new_line)

    return negative_image
