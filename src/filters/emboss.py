from utils.correlation import correlation

def emboss(image, offset=0, use_zero=True):
    """Aplica uma correleçao comum  com uma mascara predefinida

    Args:
        image (ndarray): Imagem no formato ndarray
        offset (int, optional): offset com valor padrão  0.
        use_zero (bool, optional): Extensão por zero com padrão True.

    Returns:
        ndarray: Imagem em formato ndarray com filtro emboss aplicado
    """
    return correlation(image, [-1, 0, 0, 1], (2, 2), (0, 0), offset, use_zero)
