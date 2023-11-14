from   entidades.conta import Conta

def main():
    c1 = Conta("Victor","12345-3")
    c2 = Conta("Victor","12345-3")
    print(c1)
    print(c2)

    c1.depositar(50)
    c2.sacar(60)
    print("-" * 38)
    print(c1.ver_saldo())
    print(c2.ver_saldo())

if __name__ == "__main__":
    main()