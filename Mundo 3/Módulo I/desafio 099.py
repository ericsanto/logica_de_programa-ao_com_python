import random

def maior(* numero):
    cont = maior = 0
    print(f'Analisando os valores passados...')
    for valor in numero:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(12, 34, 5, 6, 7, 8, 22)