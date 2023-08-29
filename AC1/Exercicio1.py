"""
1 - Elabore um código em Python que resolva uma equação do segundo grau ax² + bx + c = 0.
O programa deve pedir os parâmetros a, b e c da equação e deve calcular as raízes pela fórmula de Bhaskara.
Considere que as raízes são reais. Exemplo: a = 1, b = -6, c = 8 dá como raízesdelta

"""
a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

delta = (b**2)-4*a*c

print("\n**************************\n")

numero1 = (-b + delta**(1/2))/ 2 * a
numero2 = (-b - delta**(1/2))/ 2 * a

print(f"A raizes são {numero1:.2f} e  {numero2:.2f}")

