# LISTAS
'''num = [2, 5, 9, 1]
num[2] = 3
num.insert(1, 5)
num.append(6)
num.append(2)
num.sort()
while 2 in num:
    num.remove(2)
print(num)
print(len(num))'''

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor para adicionar a sua lista: ')))
for c, v in enumerate(valores):
    print(f'O valor {v} foi encontrado na posição {c}!')
for v in valores:
    print(f'{v}', end=' ')
