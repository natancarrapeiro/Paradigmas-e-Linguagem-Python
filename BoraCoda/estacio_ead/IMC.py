print("ola vamos calcular seu IMC")
peso=eval(input('Poderiamos comesar com qual o seu peso atual?'))
altura=eval(input('Qual a sua atura?'))
imc=peso/altura ** 2 
print(f"ola como vc colocou pra gengte seu peso de {peso} e sua altura de {altura} seu imc é {round(imc,2)}")