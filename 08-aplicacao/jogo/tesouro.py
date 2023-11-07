import random

def gera_posicao():
    while True:
        x = random. randint(0,5)
        y = random. randint(0,5)
        if x != 0 and y != 0:
            break

    return [x,y]

posicao = gera_posicao()
