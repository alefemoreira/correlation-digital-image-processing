from time import time
import numpy as np
from PIL import Image
from filters.sobel import sobel
from filters.median import median_filter
from reader.reader import read
from filters.box import box_11x11, box_1x11_11x1
from filters.negative_rgb import negative_rgb
from utils.rgb2yiq import rgb2yiq
from utils.correlation import icorrelation, correlation

dancingInWater = Image.open(('images/DancingInWater.jpg')).convert('RGB')
image = np.array(dancingInWater, 'uint8')

start = time()
output = correlation(image , [1/25] * 25, (5, 5), (1, 1))
print(f'end seq: {time() - start}')
start = time()
output1 = icorrelation(image , [1/25] * 25, (5, 5), (1, 1))
print(f'end con: {time() - start}')

i_output = Image.fromarray(output)
i_output.show()

i_output1 = Image.fromarray(output1)
i_output1.show()
# i_output.save('images/output.jpeg')

# data = read('files/example2.txt')
