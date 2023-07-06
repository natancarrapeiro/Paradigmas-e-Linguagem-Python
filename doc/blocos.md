<h1>Blocos</h1>
<p>Em Python, os blocos são definidos pela indentação. Diferente de C e Java, que usam as chaves { e } para delimitar os blocos, em Python todos os blocos são iniciados com o símbolo : (dois pontos) na linha superior e representados pelo acréscimo de 4 (quatro) espaços à esquerda.</p>


a = 0
for i in range(30):
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print (a)
