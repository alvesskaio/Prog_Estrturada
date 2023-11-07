def desenha(pos_personagem, pos_tesouro):
    for y in range(6):
        for x in range(6):
            if [x,y] == pos_personagem:
                print("@", end=" ")
            elif [x,y] == pos_tesouro:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

if __name__ =="__main__":
    desenha([1,0], [3,4])