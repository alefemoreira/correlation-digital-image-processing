from math import ceil, floor

def partition(v, s, e):
    p = e
    i = s
    for j in range(s, e):
        if v[j] <= v[p]:
            (v[j], v[i]) = (v[i], v[j])
            i+=1
    v[p], v[i] = v[i], v[p]
    return i    

def quicksort(v, s, e):
    if e <= s:
        return
    p = partition(v, s, e);
    quicksort(v, s, p - 1)
    quicksort(v, p + 1, e)

def median(v):
    a = v.copy()
    quicksort(a, 0, len(a) - 1)
    mid = floor(len(a) / 2)
    if len(a) % 2 == 0:
        return (a[mid] + a[mid-1]) // 2
    return a[mid]

def fit0_255(value):
    v = ceil(value)

    if v < 0: return 0
    if v > 255: return 255

    return v

def normaliza(r,g,b):
    r = 0 if r < 0 else r
    r = 255 if r > 255 else r

    g = 0 if g < 0 else g
    g = 255 if g > 255 else g
        
    b = 0 if b < 0 else b
    b = 255 if b > 255 else b
    return r,g,b
