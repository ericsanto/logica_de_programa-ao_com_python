tot18 = 0
homens = 0
mulheresMenor20 = 0
while True:
    print('=-' * 30)
    print('CADASTRO DE PESSOAS')
    print('=-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        tot18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheresMenor20 += 1
    continuar = ' '
    while continuar not in 'SN':
        print('-' * 30)
        continuar = str(input('Quer continuar? [N/S] ')).upper().strip()
    if continuar == 'N':
        break
print(f'Total de pessoas maiores de 18 anos: {tot18}')
print(f'Tivemos um total de {homens} homens cadastrados')
if mulheresMenor20 == 1:
    print(f'Tivemos um total de {mulheresMenor20} mulher com menos de 20 anos')
else:
    print(f'Tivemos um total de {mulheresMenor20} mulheres com menos de 20 anos')



