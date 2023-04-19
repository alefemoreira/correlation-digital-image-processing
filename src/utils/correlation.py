import numpy as np
# from numba import jit, prange
from utils.stats import fit0_255
from concurrent.futures import ThreadPoolExecutor, as_completed


from utils.stats import fit0_255


def neighborsRGB(v, pos, dim, pivot, use_zero=True):
    m, n = dim
    i, j = pos
    i_0, j_0 = pivot

    neighborsR = [None] * m * n
    neighborsG = [None] * m * n
    neighborsB = [None] * m * n

    neighborsR[i_0 * n + j_0] = v[i][j][0]
    neighborsG[i_0 * n + j_0] = v[i][j][1]
    neighborsB[i_0 * n + j_0] = v[i][j][2]

    for _i in range(0, m):
        deltaM = _i - i_0
        for _j in range(0, n):
            deltaN = _j - j_0
            iOutOfBound = i + deltaM < 0 or i + deltaM >= len(v)
            jOutOfBound = j + deltaN < 0 or j + deltaN >= len(v[0])
            hasIndexOutOfBound = iOutOfBound or jOutOfBound

            if hasIndexOutOfBound and not use_zero:
                return None

            if hasIndexOutOfBound and use_zero:
                neighborsR[_i * n + _j] = 0
                neighborsG[_i * n + _j] = 0
                neighborsB[_i * n + _j] = 0
                continue

            neighborsR[_i * n + _j] = v[i + deltaM][j + deltaN][0]
            neighborsG[_i * n + _j] = v[i + deltaM][j + deltaN][1]
            neighborsB[_i * n + _j] = v[i + deltaM][j + deltaN][2]

    return (neighborsR, neighborsG, neighborsB)


def correlation(image, mask, dim, pivot, offset=0, use_zero=True):
    output = np.array(image, 'uint8')

    for i in range(len(image)):
        for j in range(len(image[0])):
            neighbors = neighborsRGB(image, (i, j), dim, pivot, use_zero)
            if neighbors == None:
                output[i][j] = (0, 0, 0)
                continue

            nr, ng, nb = neighbors  # nr, ng, nb -> neighborhood r, g, b

            output[i][j][0] = fit0_255(abs(np.inner(nr, mask)) + offset)
            output[i][j][1] = fit0_255(abs(np.inner(ng, mask)) + offset)
            output[i][j][2] = fit0_255(abs(np.inner(nb, mask)) + offset)

    return output


def correlation_quadrant(image, start_pixel, end_pixel, mask, dim, pivot, offset, use_zero, output):
    for i in range(start_pixel[0], end_pixel[0]):
        for j in range(start_pixel[1], end_pixel[1]):
            neighbors = neighborsRGB(image, (i, j), dim, pivot, use_zero)
            # print(i,j)
            if neighbors == None:
                output[i][j] = (0, 0, 0)
                continue
            nr, ng, nb = neighbors  # nr, ng, nb -> neighborhood r, g, b

            output[i][j][0] = fit0_255(abs(np.inner(nr, mask)) + offset)
            output[i][j][1] = fit0_255(abs(np.inner(ng, mask)) + offset)
            output[i][j][2] = fit0_255(abs(np.inner(nb, mask)) + offset)


def icorrelation(image, mask, dim, pivot, offset=0, use_zero=True):
    output = np.array(image, 'uint8')
    r = len(image)
    c = len(image[0])
    pool = ThreadPoolExecutor(8)
    futures = []
    for i in range(0, r, r // 2):
        for j in range(0, c, c // 2):
            start_pixel = (i, j)
            end_pixel = (i + r // 2, j + c // 2)
            # print(f'start: {start_pixel}, end: {end_pixel}')
            f = pool.submit(correlation_quadrant, image, start_pixel,
                            end_pixel, mask, dim, pivot, offset, use_zero, output)
            futures.append(f)

    
    for f in as_completed(futures):
        f.result()

    return output
