"""
3- Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos:
[0-25], [26-50], [51-75] e [76-100].
 A entrada de dados deverá terminar quando for lido um número negativo.

"""
def pula_linha():
    print("\n")

def leia_numero():

    intervalo_1 = 0
    intervalo_2 = 0
    intervalo_3 = 0
    intervalo_4 = 0

    while True:

        pula_linha()
        n_input = int(input("Digite um número - "))
        # pula_linha()

        if n_input >= 0 and n_input <= 25:
            intervalo_1 += 1
        elif n_input >= 26 and n_input <= 50:
            intervalo_2 += 1
        elif n_input >= 51 and n_input <= 75:
            intervalo_3 += 1
        elif n_input >= 76 and n_input <= 100:
            intervalo_4 += 1


        if n_input < 0:
            pula_linha()
            print(f"Intervalo entre [0-25]   = {intervalo_1} \n"
                  f"Intervalo entre [26-50]  = {intervalo_2} \n"
                  f"Intervalo entre [51-75]  = {intervalo_3} \n"
                  f"Intervalo entre [76-100] = {intervalo_4}")
            pula_linha()
            break
        else:
            continue


leia_numero()

