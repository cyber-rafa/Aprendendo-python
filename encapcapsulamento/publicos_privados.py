class Conta:
    def __init__(self,nmr_conta, saldo=0):
        self._nmr_conta = nmr_conta
        self._saldo = saldo

    def deposito(self, valor):
        self._saldo += valor

    def saque(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta1 = Conta(1000, 100)
conta1.deposito(100)
print(conta1._nmr_conta)
print(conta1.mostrar_saldo())

