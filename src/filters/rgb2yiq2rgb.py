import numpy as np
from utils.rgb2yiq import rgb2yiq
from utils.yiq2rgb import yiq2rgb

def rgb2yiq2rgb(image):
    output = np.array(image)
    r, c = image.shape()
    for i in range(r):
      for j in range(c):
         output[i][j] = yiq2rgb(rgb2yiq(image[i][j]))