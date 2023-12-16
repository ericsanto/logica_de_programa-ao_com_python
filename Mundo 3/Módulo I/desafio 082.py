lista = []
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A lista completa é {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os valores pares da lista são: {par}')
print(f'Os valores impares da lista são: {impar}')


