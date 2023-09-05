"""
3- Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax^2 + bx + c.
O programa deverá receber os valores de a, b e c, e fazer as consistências,
informando ao usuário nas seguintes situações:

* Se o usuário informar o valor de a igual a zero, a equação não é do segundo
grau e o programa não deve fazer pedir os demais valores, sendo encerrado; feito

*Se o delta calculado for negativo, a equação não possui raízes reais.
Informe ao usuário e encerre o programa;

*Se o delta calculado for igual a zero a equação possui apenas uma raiz real,
informe-a ao usuário; feito

*Se o delta for positivo, a equação possui duas raízes reais,
informe-as ao usuário.

"""


def cal_raizes():

    a = float(input("Digite o valor de a: "))

    if a == 0:
        return False

    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c


    if delta > 0:
        raiz1 = (-b + (delta ** 0.5)) / (2*a)
        raiz2 = (-b - (delta ** 0.5)) / (2*a)
        print(f"As raízes são: {raiz1} e {raiz2}")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A raiz é: {raiz}")
    else:
        print("A equação não possui raízes reais.")

    return

cal_raizes()
