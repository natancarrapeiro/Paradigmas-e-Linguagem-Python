
class minhaExcecao(Exception,):
     pass
x=1
if x <0:
     raise Exception("valor negativo")

x="hello"
if not type(x)is int:
     raise TypeError("Use apenas numeros inteiros")


# try: 
#      print(hello)
     
# except:
#     print ("Excecao lançada")

