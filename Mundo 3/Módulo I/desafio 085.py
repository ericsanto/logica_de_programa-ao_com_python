dados = [[], []]
num = 0
for c in range(1, 8):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        dados[0].append(num)
    elif num % 2 == 1:
        dados[1].append(num)
dados[0].sort()
dados[1].sort()
print(f'Todos os valores: {dados}')
print(f'Os números impares digitados foram: {dados[1]}')
print(f'Os números pares digitados foram: {dados[0]}')


