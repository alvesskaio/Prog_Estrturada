"""
1-Elaborar uma função conta_pares(min, max) para exibir todos os valores
entre min e max, com um incremento de 2, separando-os com um hífen.
Ex.: 2 – 4 – 6 – 8 – 10 – 12 – 14.

"""

def conta_pares(min, max):

    if min % 2 != 0:
        min += 1

    if max % 2 != 0:
        max -= 1

    for num in range(min, max + 1, 2):
        if num < max:
            print(num , end=" - ")
        else:
            print(num)

conta_pares(2,10)

