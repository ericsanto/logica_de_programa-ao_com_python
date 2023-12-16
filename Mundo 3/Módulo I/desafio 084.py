pessoas = []
dados = []
maior_peso = menor_peso = totpessoas = 0
while True:
    dados.append((str(input('Nome: '))))
    dados.append((int(input('Peso: '))))
    if len(pessoas) == 0:
        menor_peso = maior_peso = dados[1]
    if len(pessoas) > 0:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    totpessoas += 1
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Ao todo você cadastrou {totpessoas} pessoas.')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'O menor peso foi de {menor_peso}KG. Peso de {p[0]}')
    if p[1] == maior_peso:
        print(f'O maior peso foi de {maior_peso}. Peso de {p[0]}')


