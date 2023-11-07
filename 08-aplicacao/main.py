from jogo import mapa, personagem, tesouro

def movimenta(direcao):
    personagem.movimenta(direcao)

    # Renderizar na tela
    mapa.desenha(personagem.posicao, tesouro.posicao)


def processa_input(op):
    match op:
        case "Q":
            return False
        case "W"|"A"|"S"|"D":
            movimenta(op)
        case _:
            print("O comando passado é inválido")

    return True

def jogo_acabou():
    return personagem.posicao == tesouro.posicao


def main():

    mapa.desenha(personagem.posicao, tesouro.posicao)
    while True:
        # Lê input do usuário
        op = input("\nInforme o que deseja fazer (WASD ou Q para sair): ").upper()
        if not processa_input(op):
             break
        if jogo_acabou():
            print("Encontrou o tesouro!")
            break

if __name__=="__main__":
    main()