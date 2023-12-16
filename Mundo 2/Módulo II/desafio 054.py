from datetime import date
maiores = 0
menores = 0
for i in range(1, 8):
    nascimento = int(input(f'Qual a data de nascimento da {i} pessoa? '))
    anoAtual = date.today().year
    idade = anoAtual - nascimento
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1

print(f'{maiores} são maiores de idade e {menores} são menores de idade')

