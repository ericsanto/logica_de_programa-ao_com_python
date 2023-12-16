lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

print(f'-=' * 50)
lista.sort(reverse=True)
print(f'Você digitou {cont} elementos')
print(f'Os valores em ordem decresencte são {lista}')
if 5 not in lista:
    print('O valor 5 não foi encontrado na lista!')
else:
    print('O valor 5 foi encontrado na lista!')

