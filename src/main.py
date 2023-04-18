from time import time
import numpy as np
from PIL import Image
from filters.sobel import sobel
from filters.median import median_filter
from reader.reader import reader
from utils.rgb2yiq import rgb2yiq
from utils.correlation import correlation

dancingInWater = Image.open(('images/testpat.1k.color2.tif')).convert('RGB')
image = np.array(dancingInWater, 'uint8')

start = time()
output = correlation(image , [1/11] * 11, (11, 1), (5, 0))
output = correlation(output, [1/11] * 11, (1, 11), (0, 5))
print(f'end: {time() - start}')
start = time()
output1 = correlation(output, [1/121] * 121, (11, 11), (5, 5))
print(f'end1: {time() - start}')

i_output = Image.fromarray(output)
i_output1 = Image.fromarray(output1)
i_output.show()
i_output1.show()
i_output.save('images/output.jpeg')

data = reader('files/example2.txt')
