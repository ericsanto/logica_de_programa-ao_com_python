import random
from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
#palpite = int(input('Qual é o seu palpite? '))
palpite = False
computador = random.randint(0, 10)
cont = 0
while not palpite:
    jogador = int(input('Qual o seu palpite? '))
    cont = cont + 1
    if jogador == computador:
        print(f'Você acertou com {cont} tentativa(s). Parabéns!!!!')
    elif jogador < computador:
        print('Mais... Qual o seu palpite?')
    elif jogador > computador:
        print('Menos... Qual o seu palpite?')