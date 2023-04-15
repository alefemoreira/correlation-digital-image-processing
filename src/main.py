import numpy as np
from PIL import Image
from filters.median import median_filter
from src.reader.reader import reader
from utils.rgb2yiq import rgb2yiq

dancingInWater = Image.open(('../images/DancingInWater.jpg')).convert('RGB')
image = np.array(dancingInWater, 'uint8')

output = median_filter(image, dim=(9, 9), pivot=(4, 4), use_zero=True)

i_output = Image.fromarray(output)
i_output.show()

data = reader('../files/example2.txt')
