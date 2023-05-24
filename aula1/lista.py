#nome = [abre a lista] cada dado separado por (,)é um local de memoria na lista começa por [0][1][2]...
frutas=["banana","pera","uva","tomate",]
        #[0]      [1]    [2]    [3]  

print(f"LISTA DAS FRUTAS {frutas}")
#Para acessar um elemento da lista, é só usar o seu índice. O índice começa em 0 para o primeiro elemento.
print() 
print(F"FRUTA QUE ESTA NO LUGAR [2] {frutas[2]}")
#para usar ele também
fruta=frutas[2]
print()
print(F"FRUTA QUE FOI PEGA POR UMA VARIAVEL {fruta}")
#Para alterar um elemento da lista, basta acessá-lo pelo índice e atribuir um novo valor a ele. Exemplo:
frutas[2] = "limão"
fruta=frutas[2]
print()
print(f"FRUTA ALTERADA NA LISTA E A VARIAVEL ALTEROU O SEU VALOR PARA {fruta}")
#Para adicionar um elemento ao final da lista, podemos usar o método append. Exemplo:
frutas.append("BATATA")#fruta add 
print()
print(f"novo dado a lista fruta {frutas} ")
#Para remover um elemento da lista pelo índice, podemos usar o comando del. Exemplo:
del frutas[4]#exclui o item localisado entre os []
print()
print(f"BATATA nao é uma fruta e foi retirada da lista {frutas}")

