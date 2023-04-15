import numpy as np
from PIL import Image
from filters.median import median_filter
from utils.rgb2yiq import rgb2yiq

dancingInWater = Image.open(('../images/DancingInWater.jpg')).convert('RGB')
image = np.array(dancingInWater, 'uint8')

output = median_filter(image, size=(9, 9), center=(4, 4), use_zero=True)

i_output = Image.fromarray(output)
i_output.show()

print(rgb2yiq((255, 255, 0)))
