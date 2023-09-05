"""
Elabore uma função que receba três números e exiba na tela:
(1) o produto do dobro do primeiro com metade do segundo;
(2) a soma do triplo do primeiro com o terceiro;
(3) o terceiro elevado ao cubo.

"""


def calcula(n1, n2, n3):
    Resultado1 = int((2*n1) * (n2/2))
    Resultado2 = (3*n1) + n3
    Resultado3 = n3**3
    expressao = Resultado1, Resultado2, Resultado3
    print (expressao)


calcula(2,4,5)


