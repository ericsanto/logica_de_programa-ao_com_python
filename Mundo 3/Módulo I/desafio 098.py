from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'\nContagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo


contador(1, 10, 1)
contador(10, 0, 2)
print()
print('AGORA É A SUA VEZ DE PERSONALIZAR')
i = int(input('Inicio:   '))
f = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(i, f, pas)