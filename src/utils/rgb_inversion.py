
"""
Essa função rgb_inversion(rgb) recebe uma tupla rgb com os valores das componentes de cor 
vermelho (R), verde (G) e azul (B) em um sistema de cores RGB (Red, Green, Blue) e retorna 
uma nova tupla com as componentes de cor invertidas, ou seja, cada valor de componente é 
subtraído de 255.

Por exemplo, se a tupla rgb é (100, 150, 200), a função retornará (155, 105, 55), que é a 
inversão das componentes de cor originais. Essa operação de inversão é para criar efeitos de negativo 
ou inversão de cores.
"""
def rgb_inversion(rgb):
    r, g, b = rgb

    return (255 - r, 255 - g, 255 - b)
    