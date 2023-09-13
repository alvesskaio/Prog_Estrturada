"""

1- Elabore uma função e_primo(num) que retorna se um número num é primo ou não.
 Caso num não seja primo, liste todos os números pelos quais num é divisível.
"""

def pula_linha():
    print("\n")
    print("\n")


def e_primo(num):
    primo = True
    divisores = []
    for div in range(2,num):

        if num % div ==0:
            divisores.append(div)
            primo = False

    if primo == False:
        pula_linha()
        print (f"O número {num} não é primo, pois ele é divisivel por {divisores}")
        pula_linha()
    else:
        pula_linha()
        print(f"O número {num} é primo")
        pula_linha()

# e_primo(7)
# e_primo(50)
e_primo(16)
# e_primo(7)