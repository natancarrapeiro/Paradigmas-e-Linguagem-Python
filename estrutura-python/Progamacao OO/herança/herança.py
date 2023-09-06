class Conta():
    def __init__(self,numeroDaConta,saldo) :
        self.numeroConta=numeroDaConta
        self.__saldo=saldo

    def saldo(self):
        return self.__saldo

class Criente(Conta,):
    def __init__(self,nome,idade, numeroDaConta, saldo):
        self.nome=nome
        self.idade=idade
        super().__init__(numeroDaConta, saldo)
       



natan=Criente("natan",22,222,500.0)
print(natan.saldo())
