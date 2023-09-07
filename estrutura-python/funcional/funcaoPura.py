# LAMBDA que permite a criação de funções anônimas, ou seja, sem necessidade de dar um nome para elas. 

# lambda atributos:function

veiculos =['aviao','navio','carro','onibus']
#funçao 

f_maiuscula= lambda x: str.upper(x)
#nova lista ja com a função para tronar maiuscula
#map para caminhar pela list
nomes_maiusculos= list(map(f_maiuscula, veiculos))

print(f'nomes maiusculos ={nomes_maiusculos}')


lista =[0,1,2,34,4,3,6,45,36]

f_separando_par=lambda x: x % 2 ==0
f_separando_impar = lambda x: x % 2 !=0

pares =list(filter(f_separando_par,lista))
impar =list(filter(f_separando_impar,lista))
print(f'lista de numeros pares = {pares}')
print(f'lista de numeros impar = {impar}')

print(2**4)