mai = men = 0
lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        mai = men = lista[cont]
    else:
        if lista[cont] > mai:
            mai = lista[cont]
        if lista[cont] < men:
            men = lista[cont]
print(f'Você digitou os valores {lista}')
print(f'O menor valor é {men} na posição', end= ' ')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}', end=' ')
print(f'\nO maior valor é {mai} na posição', end=' ')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}', end=' ')





