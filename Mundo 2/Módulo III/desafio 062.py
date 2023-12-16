print('Gerador de PA')
print('-=' * 10)
primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeirotermo
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo = termo + razao
    cont = cont + 1
adicaodetermos = int(input('\nQuantos termos você quer adicionar a mais? '))
while adicaodetermos <= 100:
    print(f'{termo} - ', end='')
    termo = termo + razao
    cont = cont + 1
print('FIM')
