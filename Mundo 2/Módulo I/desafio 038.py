x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
if x > y:
    print(f'{x} é maior que {y}')
elif x < y:
    print(f'{y} é maior que {x}')
elif x == y:
    print(f'Não existe valor maior, os dois são iguais.')
