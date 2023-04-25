from math import ceil, floor

"""
função auxiliar que é usada pela função de classificação quicksort(v, s, e) para dividir um vetor v em duas partes, 
uma com elementos menores ou iguais a um pivô e outra com elementos maiores. A função retorna o índice do pivô.
"""
def partition(v, s, e):
    p = e
    i = s
    for j in range(s, e):
        if v[j] <= v[p]:
            (v[j], v[i]) = (v[i], v[j])
            i += 1
    v[p], v[i] = v[i], v[p]
    return i

"""
implementação do algoritmo de classificação quicksort que classifica o vetor v entre as posições s e e 
em ordem crescente, usando a função auxiliar partition.
"""
def quicksort(v, s, e):
    if e <= s:
        return
    p = partition(v, s, e)
    quicksort(v, s, p - 1)
    quicksort(v, p + 1, e)

"""
usa o quicksort para classificar um vetor v e retorna a mediana, que é o valor que está no meio do vetor ordenado.
Se o vetor tiver um número par de elementos, a mediana é a média dos dois valores centrais.
"""
def median(v):
    a = v.copy()
    quicksort(a, 0, len(a) - 1)
    mid = floor(len(a) / 2)
    if len(a) % 2 == 0:
        return (a[mid] + a[mid-1]) // 2
    return a[mid]


"""
uma função auxiliar que recebe um valor value e o ajusta para que ele esteja no intervalo de 0 a 255. 
Se o valor estiver abaixo de 0, a função retorna 0. Se o valor estiver acima de 255, a função retorna 255. 
Caso contrário, a função retorna o próprio valor value.
"""
def fit0_255(value):
    v = ceil(value)

    if v < 0:
        return 0
    if v > 255:
        return 255

    return v

"""
recebe as componentes de cor RGB de um pixel de imagem e retorna uma nova tupla de componentes de cor RGB 
normalizadas. Cada componente de cor é ajustada usando a função fit0_255(value).
"""
def normaliza(r, g, b):
    return (
        fit0_255(r),
        fit0_255(g),
        fit0_255(b),
    )
