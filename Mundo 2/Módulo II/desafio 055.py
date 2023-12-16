menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p} pessoa: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O maior peso foi {maior}Kg\nO menor peso foi {menor}Kg')