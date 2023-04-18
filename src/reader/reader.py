import numpy as np
from PIL import Image
import os

def read(path: str) -> dict:

    mask_data = {}

    with open(path, 'r') as file:
        lines = file.readlines()

        # mask type
        mask_data['mask_type'] = lines[0].split(":")[1].replace("\n", "")

        # mask
        mask = lines[1].split(":")[1].replace("\n", "")
        mask_data["mask"] = []
        for element in mask.split(" "):
            mask_data['mask'].append(float(element))

        # mask_size
        mask_size = lines[2].split(":")[1].replace("\n", "")
        mask_data["mask_size"] = []
        for element in mask_size.split(" "):
            mask_data['mask_size'].append(int(element))

        # pivot
        pivot = lines[3].split(":")[1].replace("\n", "")
        mask_data["pivot"] = []
        for element in pivot.split(" "):
            mask_data['pivot'].append(int(element))

        # Caminho da imagem
        mask_data['image_path'] = lines[4].split(":")[1].replace("\n", "")

        # offset
        mask_data['offset'] = int(lines[5].split(":")[1].replace("\n", ""))


        # imagem em formato ndarray
        image = Image.open(mask_data['image_path'])
        mask_data['image_nd'] = np.array(image, 'uint8')

        # dimensão da imagem
        mask_data['dim_image'] = [len(mask_data['image_nd']), len(mask_data['image_nd'][0])]

    return mask_data


if __name__ == "__main__":
    data = read('../../files/example2.txt')
    print(data)