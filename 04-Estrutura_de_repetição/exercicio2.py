"""
Faça um programa que peça um nome de usuário e a sua senha,
e exiba uma mensagem de erro caso os dois valores sejam iguais.

O programa deve continuar pedindo uma nova senha até que o valor seja válido.
"""

def login():
    user = input("Digite o user: ")
    password = input("Digite o password: ")

    while user == password:
        user = input("erro, informe uma nova senha: ")
        if user != password:
            print("Você foi cadastrado parabéns!")




login()