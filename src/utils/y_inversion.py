"""
recebe uma tupla yiq com as componentes de cor YIQ de um pixel de imagem e retorna uma nova tupla com a inversão 
da componente Y, mantendo as componentes de cor I e Q inalteradas.

A componente de cor Y representa o brilho do pixel, portanto, inverter seu valor resulta em uma imagem com uma 
inversão de brilho, ou seja, áreas mais claras se tornam mais escuras e vice-versa. As componentes de cor I e Q, 
por outro lado, representam a cor do pixel, então não há mudança na inversão delas.

A função extrai a componente Y da tupla yiq e retorna uma nova tupla com a componente Y invertida em relação a 255 
(valor máximo da componente Y). As outras componentes de cor I e Q são mantidas na nova tupla retornada, 
sem alteração.
"""
def y_inversion(yiq):
    y, i, q = yiq

    """A função extrai a componente Y da tupla yiq e retorna uma nova tupla com a componente Y invertida em 
    relação a 255 (valor máximo da componente Y). As outras componentes de cor I e Q são mantidas na nova 
    tupla retornada, sem alteração.
    """
    return (255-y, i, q)