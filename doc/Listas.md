Listas são sequências mutáveis, normalmente usadas para armazenar coleções de itens homogêneos. Uma lista pode ser criada de algumas maneiras, tais como:

[]
Usando um par de colchetes para denotar uma lista vazia.

[a], [a, b, c]
Usando colchetes, separando os itens por vírgulas.

[x for x in iterable]
Usando a compreensão de lista.

list() ou list(iterable)
Usando o construtor do tipo list.

Iterable pode ser uma sequência, um container que suporte iteração ou um objeto iterador. Por exemplo, list('abc') retorna ['a', 'b', 'c'] e list( (1, 2, 3) ) retorna [1, 2, 3]. Se nenhum argumento for passado, o construtor cria uma lista vazia: [ ].