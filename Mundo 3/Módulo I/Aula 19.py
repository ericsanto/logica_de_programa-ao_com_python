'''pessoas = {'nome': 'Éric', 'idade': 21}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['nome'], ['idade'])
for k, v in pessoas.items():
    if k == 'idade':
        print(f'e a {k} é {v} anos')
    else:
        print(f'O {k} é {v}', end=' ')'''

#COPIANDO DICIONÁRIOS EM LISTAS
estados = dict()
brasil = list()
for c in range(0, 3):
    estados['UF'] = str(input('Unidade Federativa: ')).upper().strip()
    estados['Sigla'] = str(input('Sigla do Estado: ')).upper().strip()
    brasil.append(estados.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
