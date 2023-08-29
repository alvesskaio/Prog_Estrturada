"""
2 - Elabore um programa que leia uma variável inteira ano.
Em seguida, exiba na tela o resultado da expressão lógica que indica se um ano é ou não bissexto.
Um ano é bissexto se ele é múltiplo de quatro.
No entanto anos múltiplos de 100 que não são múltiplos de 400 não são bissextos.
Então 1995 não é bissexto, 2012 é bissexto, 1900 não é bissexto e 2000 é bissexto.

"""

ano = int(input("Entre com um ano: "))

resultado = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

print(resultado)
