n = int(input('Digite um número: '))
s = 1
print(f'Calculando {n}!', end='')
for c in range(n, 0, -1):
    print(c, 'x ' if c > 1 else '=', end='')
    s = s * c
    c = c - 1
print(s)
