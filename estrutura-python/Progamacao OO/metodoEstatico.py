from datetime import date
class Pessoa:
    def __init__(self,nome,idade) :
        self.nome=nome
        self.idade=idade
#metodo de class pra criar
#obj Pessoa atrasvbes do ano de nacimento

    @classmethod
    def apartirAnoNacimento(cls,nome,ano):
     return cls(nome,date.today().year - ano)

#metodo Estatico:verificar se é maior de idade
    @staticmethod
    def MaiorIdade(idade):
     return idade>=18


pessoa1=Pessoa('natan',23)
pessoa2=Pessoa.apartirAnoNacimento('carrapeiro',1995)
print(pessoa1.idade)
print(pessoa2.idade)

print(Pessoa.MaiorIdade(pessoa2.idade))