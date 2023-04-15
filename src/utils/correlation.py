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
    
    pass