from random import randint
n1 = randint(0, 9)
n2 = randint(0, 9)
n3 = randint(0, 9)
n4 = randint(0, 9)
n5 = randint(0, 9)
numeros = (n1, n2, n3, n4, n5)
print('Os valores sorteados foram:', end='')
for n in numeros:
    print(f'{n}', end='')
print(f'\nO maior número sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)}')




