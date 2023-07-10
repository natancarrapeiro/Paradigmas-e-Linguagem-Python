a=['15']
b=["25"]
c=["15"]
resultadoString=a+b+c
print(f"resultado das listas strings a+b+c é {resultadoString}")
d=[12,25,50,40]
e=[15]
f=[50]
resultadoNum=d+e+f
print(f"resultado das listas nume d+e+f é {resultadoNum}")

g=['15']
h=[15]
resultadoMisto=g+h
print(f"resultado das listas mista g+h é {resultadoMisto}")

print('vamos usar as listas usando *')

teste1=d*2+e*4
print(f"resultado das lista  d*2+e*4 é {teste1}")
print('ao colocar * nas listas elas multiplica os seus valores fazendo copias da lista ')
