import random
from time import sleep

numero = int(input('Digite um número: '))
x = random.randint(0, 5)
print('PORCESSANDO...')
sleep(3)
if numero == x:
    print('Você ganhou. Parabéns!!')
else:
    print(f'Você perdeu. Eu pensei no número {x} e não no {numero}. Tente novamente')
print('Obrigado po tentar!')