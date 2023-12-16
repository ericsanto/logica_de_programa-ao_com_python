nome = str('Ana Maria').strip()

#Nome em letras Maiúsculas
nomeMaius = nome.upper()
print(f' O nome em letras maiúsculas é {nomeMaius}')

#Nome em letras Minúsculas
nomeMinus = nome.lower()
print(f' O nome em letras mnúsculas é {nomeMinus}')

#Quantidade de letras em Nome considerando os espaços
print(len(nome))

#Tramsformando o nome em uma lista
dividido = nome.split()

#Mostrando o primeiro nome a quantidade de letras
print(f'O primeiro nome: {dividido[0]}, contém {len(dividido[0])} letras')

#Quantidade de letras em nome sem considerar os espaços
quantidadeDeLetra = len(nome.replace(' ', ''))
print(quantidadeDeLetra)

