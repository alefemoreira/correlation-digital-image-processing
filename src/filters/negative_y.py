import numpy as np 

from utils.rgb2yiq import  rgb2yiq
from utils.yiq2rgb import  yiq2rgb
from utils.y_inversion import  y_inversion
from utils.stats import normaliza

def negY(image: np.ndarray):
  """Recebe uma imagem em formato ndarray e retorna esse mesmo ndarray com a conversão aplicada

  Args:
      image (np.ndarray): Imagem em formato em ndarray

  Returns:
      ndarray: Imagem em formato ndarray com negativo em Y aplicado
  """
  
  output = np.array(image, 'uint8')

  # Percorrendo a imagem
  for i in range(len(image)):
    for j in range(len(image[0])):
      r,g,b = image[i][j] 

      Y,I,Q = rgb2yiq((r,g,b))
      
      
      # Operação para aplicar o negativo na banda Y seguido da conversão para RGB
      r,g,b = yiq2rgb(y_inversion((Y,I,Q)))
      
      # Normalização dos limites
      r,g,b = normaliza(r,g,b)
      
      # Novo pixel com Y invertido
      output[i][j] = [r,g,b]

  return output
