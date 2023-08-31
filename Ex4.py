"""

Elabore uma função que receba uma variável inteira ano.
Em seguida, retorne o resultado da expressão lógica que indica se um ano é ou não bissexto.
Um ano é bissexto se ele é múltiplo de quatro.
No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

"""

def verficiaAno(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano% 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



verficiaAno(2012)
