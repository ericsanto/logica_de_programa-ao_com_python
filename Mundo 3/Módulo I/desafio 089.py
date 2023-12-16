ficha = []
while True:
    nome = str(input('Nome: '))
    capitalize = nome.capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([capitalize, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, l in enumerate(ficha):
    print(f'{i:<4}{l[0]:<10}{l[2]}:>8')
while True:
    opc = int(input('Deseja saber as notas de qual aluno? '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'A nota do aluno {ficha[opc][0]} foram: {nota1} e {nota2}')