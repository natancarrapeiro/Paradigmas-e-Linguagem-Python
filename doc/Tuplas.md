Tuplas são sequências imutáveis, tipicamente usadas para armazenar coleções de itens heterogêneos. Elas são aplicadas também quando é necessário utilizar uma sequência imutável de dados homogêneos. Uma tupla pode ser criada de algumas maneiras, tais como:

()
Usando um par de parênteses para denotar uma tupla vazia.

a, b, c ou (a, b, c)
Separando os itens por vírgulas.

tuple() ou tuple(iterable)
Usando o construtor do tipo tuple.

Novamente, iterable pode ser uma sequência, um container que suporte iteração ou um objeto iterador. Por exemplo, tuple('abc') retorna ('a', 'b', 'c') e tuple( [1, 2, 3] ) retorna (1, 2, 3). Se nenhum argumento for passado, o construtor cria uma tupla vazia: ().