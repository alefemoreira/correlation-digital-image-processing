from time import time
from PIL import Image
from reader.reader import read, filter_image
from sys import argv

if (len(argv) < 2):
    print('insira o caminho do arquivo')
    exit(0)

data = read(argv[1]) # Lendo o arquivo com uma função própria
start = time()
image = filter_image(data)
end = time()

print(f'Tempo de execução: {end - start} s')

output = Image.fromarray(image)

if 'output' in data.keys():
    output.save(data['output'])
else:
    output.show()




