#para se abrir um dicionario(chave/valor)abre com {}
#se separa a chave (chave :[valor],chave2:[valor2])
pessoas={111:['pessoa 01'],222:['pessoa 02'],333:['natan','carrapeiro']} 
print(pessoas)
print(f"chave 222 = {pessoas[333]}")
print()
#para add uma nova chave/valor 
pessoas [444]="pessoa 04"
print(f"pessoa add nova {pessoas} => pessoa 04")
print()
#copiar dicionario
copia_pessoas=pessoas.copy()
print(f"copia exata do dicionario pessoas {copia_pessoas}")
#limpar um diciomario
pessoas.clear()
print("limpando dicionario")
print(pessoas)
print(2 + 3 – 4 ** 2 + 5 / 2 – 5 // 2)