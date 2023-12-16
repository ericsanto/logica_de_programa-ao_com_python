import random
from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
soma = cont = 0
print('=-' * 20)
while True:
    jogador = int(input('Diga um valor: '))
    pc = random.randint(0, 10)
    parOuImpar = str(input('Par ou Ímpar? [P/I]')).strip().upper()
    soma = pc + jogador
    print('-' * 30)
    if soma %2 == 0 and parOuImpar == 'P':
        print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu PAR')
        print('-' * 30)
        print('Você VENCEU')
        print('Vamos jogar novamente...')
        cont += 1
    elif soma %2 != 0 and parOuImpar == 'I':
        print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu ÍMPAR')
        print('VOCÊ VENCEU!!!')
        print('Vamos jogar novamente...')
        print('=-' * 20)
        cont += 1
    if soma %2 == 0 and parOuImpar == 'I':
        print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu PAR')
        print('Você PERDEU!!!')
        break
    elif soma %2 != 0 and parOuImpar == 'P':
        print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} deu ÍMPAR')
        print('Você PERDEU!!')
        print('-' * 30)
        break
print('ACABOU')
print('=-' * 290)
if cont > 1:
    print(f'Você ganhou {cont} vezes')
else:
    print(f'Você ganhou {cont} vez')





