from math import ceil

def rgb2yiq(rgb: tuple) -> tuple:
    r, g, b = rgb
    
    y = ceil(0.299 * r + 0.587 * g + 0.114 * b)
    i = ceil(0.596 * r - 0.274 * g - 0.322 * b)
    q = ceil(0.211 * r - 0.523 * g + 0.312 * b)

    return (y, i, q)
