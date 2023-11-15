from   entidades.agencia import Agencia
from   entidades.conta import Conta

def main():
    c1 = Conta("Victor","12345-3")
    c2 = Conta("Kaio","12245-3")
    ag = Agencia("1234-5", "Rua-x")

    ag.add_conta(c1)
    ag.listar_contas()
    print(ag.transferir(c1, c2, 50))
    ag.listar_contas()
    ag.add_conta(c2)
    print(ag.transferir(c1, c2, 50))
    ag.listar_contas()



if __name__ == "__main__":
    main()