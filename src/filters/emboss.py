from utils.correlation import correlation

def emboss(image, offset=0, use_zero=True):
    return correlation(image, [-1, 0, 0, 1], (2, 2), (0, 0), offset, use_zero)
