x = int(input('Digite um número: '))
y = int(input('Digite mais um número: '))
z = int(input('Digite outro número: '))
menor = x

if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
print(f'O menor número é {menor}')
maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
print(f'O maior número é {maior}')
