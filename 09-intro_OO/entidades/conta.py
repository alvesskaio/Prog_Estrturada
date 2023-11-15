class Conta :
    # titular, agencia, saldo,

    saldo = 0

    # Metodo construtor
    def __init__(self, titular, agencia ):
        self.titular = titular
        self.agencia = agencia

    # Metodos

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def ver_saldo(self):
        return self.saldo

    def __str__(self):
        return f"{self.titular}: saldo R${self.saldo:.2f}"

    def __eq__(self, obj):
        if isinstance(obj, Conta):
            return self.titular == obj.titular and self.saldo == obj.saldo
        return False

