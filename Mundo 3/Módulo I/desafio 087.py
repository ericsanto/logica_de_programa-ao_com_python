matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scoluna = menl = simpar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a linha {l} e para a coluna {c}: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        elif matriz[l][c] % 2 == 1:
            simpar += matriz[l][c]
    print()
print(f'A soma dos valores pares é: {spar}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print(f' O maior valor da segunda linha é: {mai}')
for l in range(0, 3):
    scoluna += matriz[l][2]
print(f'A soma dos valores da coluna 3 é: {scoluna}')
for c in range(0, 3):
    if c == 0:
        menl = matriz[0][c]
    else:
        if matriz[0][c] < menl:
            menl = matriz[0][c]
print(f'O menor valor da linha 1 é: {menl}')
print(f'A soma dos valores impares é: {simpar}')