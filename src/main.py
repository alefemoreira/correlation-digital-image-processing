from time import time
from PIL import Image
from reader.reader import read, filter_image
from sys import argv

if (len(argv) < 2):
    print('insira o caminho do arquivo')
    exit(0)

data = read(argv[1])
image = filter_image(data)
Image.fromarray(image).save(data['output'])

print(data)




