posicao = [0,0]

def movimenta(direcao):
    global posicao
    match direcao:
        case "W":
            if posicao[1] > 0:
                posicao[1] -= 1
        case "S":
            if posicao[1] < 5:
                posicao[1] += 1
        case "A":
            if posicao[0] > 0:
                posicao[0] -= 1
        case "D":
            if posicao[0] < 5:
                posicao[0] += 1

# if __name__ == "__main__":

