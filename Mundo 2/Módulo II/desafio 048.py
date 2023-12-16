soma = 0
cont = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        cont = cont + 1
        soma = soma + count
print(f'A soma dos {cont} números múltiplos de 3 é {soma}')




