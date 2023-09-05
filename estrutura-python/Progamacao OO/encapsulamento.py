class Conta:
    def __init__(self, numero, saldo):
     self.__numero = numero#privadoa
     self.__saldo = saldo#privado

    def depositar(self,valorDeposito):
      if( valorDeposito < self.__saldo):
        self.__saldo +=valorDeposito
        print("transferencia feita")
        print(self.__saldo)
        return 
      else:
        print("saldo inferior")  
    
    def pega_saldo(self):
        return self.__saldo
    

conta = Conta(1, 1000)
# print(conta.__saldo=500) #atributo privado
conta.depositar(300)

conta.pega_saldo()
    