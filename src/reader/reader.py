import numpy as np
from PIL import Image
from filters.median import median_filter
from filters.rgb2yiq2rgb import rgb2yiq2rgb
from filters.sobel import sobel
from filters.emboss import emboss
from filters.box import box
from filters.negative_rgb import negative_rgb
from filters.negative_y import negY
from utils.correlation import correlation


def read(path: str) -> dict:
    data = {}
    with open(path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if 'TYPE' in line:
                data['type'] = line.strip().split(":")[-1]
                pass
            if 'MASK' in line:
                data['mask'] = np.fromstring(
                    line.strip().split(":")[-1], dtype=float, sep=' ')
                pass
            if 'MDIM' in line:
                data['dim'] = np.fromstring(
                    line.strip().split(":")[-1], dtype=int, sep=' ')
                pass
            if 'PIVOT' in line:
                data['pivot'] = np.fromstring(
                    line.strip().split(":")[-1], dtype=int, sep=' ')
                pass
            if 'FILE' in line:
                filepath = line.strip().split(":")[-1]
                image = Image.open(filepath).convert("RGB")
                imagenp = np.array(image, 'uint8')

                data['filepath'] = filepath
                data['image'] = image
                data['imagenp'] = imagenp
                pass
            if 'OFFSET' in line:
                data['offset'] = int(line.strip().split(":")[-1])
                pass
            if 'OUTPUT' in line:
                data['output'] = line.strip().split(":")[-1]
                pass

    return data


def filter_image(data: dict) -> np.ndarray:
    if data['type'] == 'MEDIAN':
        image = data['imagenp']
        pivot = data['pivot']
        dim = data['dim']
        return median_filter(image, dim, pivot, use_zero=True)

    if data['type'] == 'SOBEL':
        image = data['imagenp']
        offset = data['offset']
        return sobel(image, offset)

    if data['type'] == 'EMBOSS':
        image = data['imagenp']
        offset = data['offset']
        return emboss(image, offset)

    if data['type'] == 'SUM':
        image = data['imagenp']
        pivot = data['pivot']
        dim = data['dim']
        m, n = dim
        offset = data['offset']
        return correlation(
            image=image,
            mask=[1] * m * n,
            dim=dim,
            pivot=pivot,
            offset=offset,
            use_zero=True
        )

    if data['type'] == 'BOX':
        image = data['imagenp']
        dim = data['dim']
        return box(image=image, dim=dim, use_zero=True)

    if data['type'] == 'RYR':
        image = data['imagenp']
        return rgb2yiq2rgb(image=image)

    if data['type'] == 'CORR':
        image = data['imagenp']
        pivot = data['pivot']
        dim = data['dim']
        mask = data['mask']
        offset = data['offset']
        return correlation(image, mask=mask, pivot=pivot, dim=dim, offset=offset, use_zero=True)

    if data['type'] == 'NEGY':
        image = data['imagenp']
        return negY(image)

    if data['type'] == 'NEG':
        image = data['imagenp']
        return negative_rgb(image)


if __name__ == "__main__":
    data = read('../../files/example2.txt')
    print(data)
