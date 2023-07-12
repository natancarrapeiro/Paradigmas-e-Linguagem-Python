numero=int(input("me de um numero e eu vou e falar se ele é IMPAR ou PAR : "))


#função pra ver se o numero é impar ou par 
def imparPar(numero):
   
   if(numero %2 ==0):
    print(f'{numero} é um numero par')
   else:
    print(f"{numero} é numero impar")

imparPar(numero)