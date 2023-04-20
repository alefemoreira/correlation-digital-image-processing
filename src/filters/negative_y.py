import numpy as np 

from utils.rgb2yiq import  rgb2yiq
from utils.yiq2rgb import  yiq2rgb
from utils.y_inversion import  y_inversion
from utils.stats import normaliza

def negY(image: np.ndarray):
  """
    Recebe uma imagem em formato ndarray e retorna esse mesmo ndarray com a conversão aplicada
  """
  
  output = np.array(image, 'uint8')
  #percorro a imagem
  for i in range(len(image)):
    for j in range(len(image[0])):
      r,g,b = image[i][j] 

      Y,I,Q = rgb2yiq((r,g,b))
      
      #operação para aplicar o negativo na banda Y
      
      # Conversao para RGB
      r,g,b = yiq2rgb(y_inversion((Y,I,Q)))
      
      # Normalização dos limites
      r,g,b = normaliza(r,g,b)
      
      #Add a imagem
      output[i][j] = [r,g,b]

  return output
