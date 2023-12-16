import random
from time import sleep
print('[1] PEDRA\n'
      '[2] PAPEL\n'
      '[3] TESOURA\n')
num = int(input('Escolha uma das opções acima: '))
print('JO - \n'
      'KEN - \n'
      'PÔ...')
sleep(3)
print('-' * 20)
pc = random.randint(1, 3)
if pc == 1:
    print('Eu escolhir PEDRA')
elif pc == 2:
    print('Eu escolhir PAPEL')
elif pc == 3:
    print('Eu escolhir TESOURA')
if num == 1 and pc == 1:
    print(f'EMPATE!')
elif num == 1 and pc == 2:
    print('Você perdeu!')
elif num == 2 and pc == 1:
    print('Você ganhou!')
elif num == 2 and pc == 2:
    print('EMPATE!')
elif num == 3 and pc == 1:
    print('Você perdeu!')
elif num == 1 and pc == 3:
    print('Você ganhou!')
elif num == 3 and pc == 3:
    print('EMPATE!')
elif num == 2 and pc == 3:
    print('Você perdeu!')
elif num == 3 and pc == 2:
    print('Você ganhou!')
elif num == 3 and pc == 3:
    print('EMPATE!')
