def negative_rgb(image: np.Array):
    output = copy(image)

    for i in range(len(image)):
        for j in range(len(image[0])):
            output[i][j] = rgb2yiq(image[i][j])

