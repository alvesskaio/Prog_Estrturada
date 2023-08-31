"""

Elabore uma função com as mesmas regras do exercício anterior,
porém retornando os três resultados, ao invés de exibi-los na tela.

"""

def calcula(n1, n2, n3):
    Resultado1 = int((2*n1) * (n2/2))
    Resultado2 = (3*n1) + n3
    Resultado3 = n3**3
    expressao = Resultado1, Resultado2, Resultado3
    return expressao


def main():
    print(calcula(4,5,6))

main()
