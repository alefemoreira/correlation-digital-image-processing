import numpy as np 
from PIL import Image


from utils.rgb2yiq import  rgb2yiq
from utils.yiq2rgb import  yiq2rgb
from utils.y_inversion import  y_inversion
from utils.stats import normaliza

def negY(image: np.ndarray):
  """
    Recebe uma imagem em formato ndarray e retorna esse mesmo ndarray com a conversão aplicada
  """
  
  negY_image = np.ndarray.__array__(image, 'uint8')
  #percorro a imagem
  for i in range(len(image)):
    new_line = []
    for j in range(len(image[0])):
      r,g,b = image[i][j] 

      # Conversão para YIQ com Y negativo
      Y,I,Q = rgb2yiq((r,g,b))
      
      #operação para aplicar o negativo na banda Y
      Y2 = 255-Y
      
      # Conversao para RGB
      r,g,b = yiq2rgb((Y2,I,Q))
      
      # Normalização dos limites
      r,g,b = normaliza(r,g,b)
      
      # Novo linha
      new_line.append([r,g,b])
      
      #Add a imagem
      negY_image[i][j] = [r,g,b]

  return negY_image
