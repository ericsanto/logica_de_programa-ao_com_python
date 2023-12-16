n = int(input('Digite um número: '))
resp = str(input('Quer continuar?: [S/N]')).upper().strip()
c = 1
media = soma = menor = maior = 0
while resp == 'S':
    c += 1
    n1 = int(input('Digite um número: '))
    resp = str(input('Quer continuar?: [S/N]')).upper().strip()
    soma = soma + n + n1
    media = soma/c
if c == 1:
    maior = menor = n = n1
else:
    if n > n1:
        maior = n
    elif n1 > n:
        maior = n1
    if n1 < n:
        menor = n1
    elif n1 > n:
        menor = n
if resp == 'N':
    print(f'Você digitou {c} números e a media entre eles foi {media}')
    print(f'O maior valor foi {maior} e o menor foi {menor}')


