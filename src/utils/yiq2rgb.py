from stats import fit0_255

def yiq2rgb(yiq):
    y, i, q = yiq

    r = fit0_255(y + 0.956 * i + 0.621 * q)
    g = fit0_255(y - 0.272 * i - 0.647 * q)
    b = fit0_255(y - 1.106 * i + 1.703 * q)

    return (r, g, b)
