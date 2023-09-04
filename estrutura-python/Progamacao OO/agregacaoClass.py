class Salario:
    def __init__(self,base,bonus) :
        self.base=base
        self.bonus=bonus
    
    def salario_anual(self):
        return(self.base*12)+self.bonus
    
class Emrpegado:
    def __init__(self,nome,idade,salario): 
        self.nome=nome
        self.idade=idade
        self.salario_agregado=salario #agregacao

    def salario_total(self):
        return self.salario_agregado.salario_anual()
    
natan_salario =Salario(10000,700)
natan_emrpegado=Emrpegado('natan',46,natan_salario)

print(natan_emrpegado.salario_total())
