from numpy import ndarray
from PIL import Image

from utils.rgb2yiq import  rgb2yiq
from utils.yiq2rgb import  yiq2rgb
from utils import  y_inversion
from utils.stats import fit0_255

def negY(image: ndarray):
  """
    Recebe uma imagem em formato ndarray e retorna esse mesmo ndarray com a conversão aplicada
  """

  negY_image = []

  for line in image:
    new_line = []
    for pixel in line:
      r,g,b = pixel[0], pixel[1], pixel[2] 

      # Conversão para YIQ com Y negativo
      y,i,q = rgb2yiq((r,g,b))
      # Operação para aplicar o negativo na banda Y
      y = y-255
      # Conversão para RGB
      r,g,b = yiq2rgb((y,i,q))
      # Normalização dos limites
      r,g,b = normaliza(r,g,b)
      # Novo pixel
      new_line.append([r,g,b])

    # Nova linha
    negY_image.append(new_line)
  
  return negY_image
