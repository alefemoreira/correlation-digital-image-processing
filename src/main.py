import numpy as np
from PIL import Image
from filters.median import median_filter
from src.reader.reader import read
from src.filters.box import box_11x11, box_1x11_11x1
from utils.rgb2yiq import rgb2yiq

# dancingInWater = Image.open(('../images/DancingInWater.jpg')).convert('RGB')
# image = np.array(dancingInWater, 'uint8')

# output = median_filter(image, dim=(9, 9), pivot=(4, 4), use_zero=True)


data = read('../files/example2.txt')
output = box_1x11_11x1(data['image_nd'])


i_output = Image.fromarray(output)
i_output.show()