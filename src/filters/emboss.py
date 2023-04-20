from utils.correlation import correlation
from utils.hist_expansion import histogram_expansion
from utils.stats import fit0_255

import numpy as np


def emboss(image, offset=0, use_zero=True):
    return correlation(image, [-1, 0, 0, 1], (2, 2), (0, 0), offset, use_zero)
