class A:
    def __init__(self,nome) :
        self.nome=nome
    
    def ola(self):
        pass# significa que sera definido o que ele faz pelo filho
                    

class B(A):
    def __init__(self, nome):
        super().__init__(nome)
    def ola(self):
        print(self.nome) 
        
class C(A):
    def __init__(self, nome,sobrenome):
        self.sobrenome=sobrenome
        super().__init__(nome)
    def ola(self):
        print(self.nome,self.sobrenome) 


d=B("natan")
d.ola()   

e=C("natan","carrapeiro")
e.ola()