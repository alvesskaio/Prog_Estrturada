"""
Programação Estrutura
2023.2

Estrutura de seleção

if <Teste logico>:
    <codigo>
else:
    <codigo>

"""

def e_par(num):
    if num % 2 == 0:
        print(num, "é par")
    else:
        print(num, "é ímpar")

    print("Fim da função")

# e_par(4)
# e_par(5)

def conceito(nota):
    if nota > 9:
        print("Conteito A")
    elif nota > 8:
        print("Conceito B")
    elif nota > 7:
        print("Conceito C")
    else:
        print("Conceito D")

# conceito(9.5)
# conceito(5)

# Pesquisar sobre o match

# def cli():
#     opcao = input("Digite 1 para inserir nome, 2 para nota, ou "
#                   "qualquer outro caractere para sair:")

#     match opcao:
#         case "1":
#             print("Opção 1")
#         case "2":
#             print("Opção 2")
#         case _:
#             print("Sair")

# Exercicios

# def e_par2(num):
#     return num % == 0

def maior (num1, num2):
    if num1 > num2:
        return num1

    return num2

# Ternário
def maior2(num1, num2):
    return num1 if num1 > num2 else num2

def ve_num(num):
    if num > 0:
        return "positivo"

    return "negativo"


# ve_num(-5)
# ve_num(5)


def ve_vogal(v):
    if v == "a" or v == "e" or v == "i" or v == "o" or v =="u":
        return "Vogal"

    return "Consoante"

# ve_vogal("i")


def media_nota(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3

    if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0 or nota3 > 10 or nota3 < 0:
        print ("valor inválido")
        return False
    elif media == 10:
        print ("Aprovado com Distinção")
    elif media >= 7:
        print ("Aprovado")
    elif media < 7:
        print ("Reprovado")


media_nota(-2,10,10)








