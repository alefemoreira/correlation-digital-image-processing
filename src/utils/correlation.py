import numpy as np
from utils.stats import fit0_255
from concurrent.futures import ThreadPoolExecutor, as_completed


"""
A função neighborsRGB recebe uma matriz de pixels de imagem, uma posição de pixel (i, j), 
as dimensões da máscara dim, um ponto central da máscara pivot, e um sinalizador use_zero que 
indica se os pixels fora dos limites da imagem devem ser preenchidos com zeros. A função retorna 
uma tupla com três listas, que contêm os valores dos canais R, G e B dos pixels na vizinhança da 
posição (i, j) e do tamanho especificado pela máscara. A lista central é preenchida com o valor do 
pixel na posição (i, j), e os demais pixels da lista são preenchidos com zeros, se estiverem fora 
dos limites da imagem e use_zero=True. Se use_zero=False, a função retorna None se algum dos pixels 
estiver fora dos limites da imagem.
"""
def neighborsRGB(v, pos, dim, pivot, use_zero=True):
    m, n = dim # m linhas e n colunas
    i, j = pos # pixel (i, j) q está sendo processado
    i_0, j_0 = pivot # posição i0, j0 do pivot na MASCARA

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


"""
A função correlation recebe uma matriz de pixels de imagem, uma máscara, as dimensões da máscara dim, 
um ponto central da máscara pivot, um valor de deslocamento offset e um sinalizador use_zero. A função 
itera sobre cada pixel da imagem e aplica a máscara para obter um valor de correlação para cada canal 
de cor R, G e B. Os valores são limitados entre 0 e 255 usando a função fit0_255, e os valores resultantes 
são atribuídos a um novo pixel de saída na mesma posição da imagem original.
"""
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


"""
A função correlation_quadrant é semelhante à correlation, mas é otimizada para ser executada em paralelo. 
Em vez de iterar sobre todos os pixels da imagem, a função itera sobre uma seção retangular da imagem, 
definida pelos pontos inicial e final. Esta função é chamada por threads em paralelo na função icorrelation.
"""
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



""""
A função icorrelation é semelhante à correlation, mas divide a imagem em quatro seções retangulares iguais e 
chama a função correlation_quadrant em cada seção em paralelo, usando a biblioteca 
concurrent.futures.ThreadPoolExecutor. A função retorna a imagem de saída com a correlação aplicada.
"""
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
