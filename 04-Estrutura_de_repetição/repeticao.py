"""
Programação Estruturada

12/09/2023
Estruturas de Repetição
"""

def contagem_regressiva(num):
    while num > 0:
        print(num)
        num -= 1

# contagem_regressiva(5)

def pede_nome():
    nome = input("Informe o seu nome: ")

    while nome == "":
        nome = input("Texto passado é inválido! Informe um nome: ")

    print("Olá, ", nome)


# pede_nome()

def numero():
    while True:
        numero = int(input("Informe um número: "))

        if numero == 3:
            print("Escreveu 3!")
            continue # Interrompe a interação corrente

        if numero == 5:
            break #Interrompe por completo a estrutura de repetição

        print("Próximo número")

# numero()


# While _ Else

def tentativa():
    num_tentativas = 0

    while num_tentativas < 3:
        nome = input("Informe um nome: ")

        if nome != "":
            print("Olá", nome)

        num_tentativas += 1
    else: # Só vai ser executado caso não tenha passado pela break
        print("Nenhum nome foi inserido!")
        nome = "erro"

    print(nome)

# tentativa()

def contagem_regressiva2(num):
    for cont in range(num, 0, -1):
        print(cont)

# contagem_regressiva2(5)

def imprime_texto():
    # Quando não quiser usar uma variavel usar o underscore
    for _ in range(5):
        print("Texto")