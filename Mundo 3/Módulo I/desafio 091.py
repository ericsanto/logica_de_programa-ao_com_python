import random
import time
from time import sleep
from random import randint
valores = {'jogador1': random.randint(0, 6), 'jogador2': randint(0, 6),
           'jogador4': randint(0, 6), 'jogador5': randint(0, 6),
           'jogador6': randint(0, 6)}
print('Valores sorteados')
for k, v in valores.items():
    time.sleep(1)
    print(f'O {k} tirou {v} no dado')

print('Ranking dos jogadores:')
posição = 0
for i in sorted(valores, key=valores.get, reverse=True):
    time.sleep(1)
    posição += 1
    print(f'{posição} lugar: ', end=' ')
    print(f'{i} com {valores[i]}')


