from time import time
import numpy as np
from PIL import Image
from filters.sobel import sobel
from filters.median import median_filter
from reader.reader import read
from filters.box import box_11x11, box_1x11_11x1
from filters.negative_rgb import negative_rgb
from utils.hist_expansion import histogram_expansion
from utils.rgb2yiq import rgb2yiq
from utils.correlation import icorrelation, correlation
from sys import argv

if (len(argv < 1)):
    print('insira o caminho da imagem')
    exit(code=1)

data = read(argv[0])

data['']
