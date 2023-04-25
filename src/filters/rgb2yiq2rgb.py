import numpy as np
from utils.rgb2yiq import rgb2yiq
from utils.yiq2rgb import yiq2rgb

def rgb2yiq2rgb(image):
    """Recebe uma imagem em formato em ndarray em rgb, depois passa para yiq e volta para rgb

    Args:
        image (ndarray): Imagem em formato ndarray

    Returns:
        ndarray: Imagem em formato ndarray
    """
    output = np.array(image)
    r, c = len(image), len(image[0])
    for i in range(r):
        for j in range(c):
            output[i][j] = yiq2rgb(rgb2yiq(image[i][j]))
    return image