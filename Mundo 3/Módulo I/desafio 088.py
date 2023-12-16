import random
from random import sample
from time import sleep
jogos = list()
print(f'-' * 30)
print('     JOGO DA MEGA SENA     ')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie?' ))
print(f'-=' * 3,  f'SORTEANDO {n} JOGOS',  '-=' * 3)
sleep(1)
for c in range(0, n):
    lista = list(sample(range(61), 6))
    jogos.append(lista[:])
    lista.clear()
for i, l in enumerate(jogos):
    sleep(1)
    l.sort()
    print(f'JOGO{i + 1}: {l}')
print(f'{jogos}')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
