"""
    Programação estruturada
    29/08/2023

    Funções
"""

# Parametros posicionais

# Tamanho definido um valor default
def cabecalho(titulo, sep = "-", tamanho = 30):
    print(sep * tamanho)
    print(titulo)
    print(sep * tamanho)

# cabecalho("Relatório de despeses", "-")
# cabecalho("Folha de ponto", "=")


def soma(x,y):
    return x + y


# print(16 - soma(10,32) * soma(1,2))

# Escopo local vs escopo global de variáveis

a = 2 #escopo local
PI = 3.14

def func():
    global a #não é uma boa prática
    a = 3 #escopo local
    print(a)

def func2():
    print(a)

# print(a)
# func()
# print(a)
# func2()