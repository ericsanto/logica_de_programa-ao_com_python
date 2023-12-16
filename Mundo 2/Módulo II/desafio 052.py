n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1): #n+1, pois o python sempre conta um a menos no caso do FOR. Então, se a pessoa digitar 9, se não tivesse o n+1, o python leria como 8.
   if n % c == 0:
       print(f'\033[0;32m', end='')
       cont = cont + 1
   else:
       print(f'\033[0;31m', end='')
   print(f'{c}', end=' ')
if cont == 2:
    print(f'\nO {n} foi divisível somente duas vezes. Portanto, ele é primo!')
else:
    print('\nO número foi divisível mais de duas vezes. Logo, ele não é orimo!')


