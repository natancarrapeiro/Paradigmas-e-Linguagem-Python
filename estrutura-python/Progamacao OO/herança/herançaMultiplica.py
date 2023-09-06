class A:
    def __init__(self,nome) :
        self.nome=nome

    def ola(self):
        print('ola '+self.nome)

class B:
    def __init__(self,sobrenome) :
        self.sobrenome=sobrenome

class Idade:
    def __init__(self,idade) :
        self.idade=idade
    
class Nomecompleto(A,B,Idade):
    def __init__(self, nome,sobrenome,idade):
       A.__init__(self,nome)
       B.__init__(self,sobrenome)
       Idade.__init__(self,idade)
    def meuNome(self):
        print(self.nome,self.sobrenome,self.idade)

oie=Nomecompleto("natan","carrapeiro",22)
oie.ola()
oie.meuNome()