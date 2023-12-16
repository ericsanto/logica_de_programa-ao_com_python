print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo1 = termo
cont = 1
while cont <= 10:
    print(f'{termo1} - ', end='')
    termo1 = termo1 + razao
    cont = cont + 1
print('FIM', end='')