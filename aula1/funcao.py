#def abre uma função 
def func():
    x = 1#variavel local
    print(x)
x = 10#variavel global
func()#chama a função para ser executada 
print(x)


def soma(z,y):
    num1=z
    num2=y
    resultado=num1+num2
    print(f"resultado {resultado}")
    
soma(2,2)#chama a função mas essa precisa dos atributos pedidos z,y para ele consiga executar

