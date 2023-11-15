class Agencia:

    contas = []

    def __init__(self, numero, endereco):
        self.numero = numero
        self.endereco = endereco

    def add_conta(self, conta):
        self.contas.append(conta)

    def transferir(self, origem, destino, valor):
        if origem in self.contas and destino in self.contas:
            origem.sacar(valor)
            destino.depositar(valor)
            return True

        return False

    def listar_contas(self):
        for conta in self.contas:
            print(conta)