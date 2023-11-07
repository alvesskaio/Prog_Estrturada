from projeto.ator import ator1
from . import menu #Referencia relativa -> um ponto indica que os módulos estão na mesma pasta

NUMERO_MAXIMO_ITENS = 50


def le_nome():
    return input("Informe o seu nome: ")

def interface():
    print(menu.OPCOES)
    op = input("Você quer falar com o ator (s/n)?")
    if op.lower() == "s":
        ator1.fala()

if __name__ =="__main__":
    teste = le_nome()
    print(teste)