pessoas = {}
lista_de_pessoas = []
c = media = tot_mulheres = tot_idades = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    tot_idades += pessoas['idade']
    lista_de_pessoas.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if resp == 'N':
        break
print(f'{lista_de_pessoas}')
for p, q in enumerate(lista_de_pessoas):
    c += 1
print(f'Ao todo temos o total de {c} pessoas')
for p in lista_de_pessoas:
    if p["sexo"] in 'F':
        print(f'As mulheres cadastradas foram: {p["nome"]}')
media = tot_idades / c
print(f'A média de idade é de {media}')
print('As pessoas acima da média de idade foram: ', end=' ')
for p in lista_de_pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')


