import random
from time import sleep

def sortear(lista):
    print('SORTEANDO OS NÚMEROS')
    for c in range(0, 5):
        n = random.randrange(0, 10)
        print(f'{n}', end=' ')
        sleep(0.5)
        lista.append(n)

def soma_Par(numeros):
    soma = 0
    print('Número par sorteado:', end=' ')
    for i, v in enumerate(numeros):
        if v % 2 == 0:
            soma += v
            print(f'{v}', end=' ')
    print(f'\nA soma entre os pares é: {soma}')


numeros = list()
sortear(numeros)
print(f'\nOs numeros sorteados foram {numeros}')
soma_Par(numeros)
