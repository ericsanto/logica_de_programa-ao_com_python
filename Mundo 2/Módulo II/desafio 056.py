totalIdade = 0
homemmaisvelho = 0
nomemaisvelho = ''
mulheresmenos20 = 0
for dados in range(1, 5):
    print('-'*5, '{} PESSOA'.format(dados), '-'*5)
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    totalIdade = totalIdade + idade
    media = totalIdade / dados

    if dados == 1 and sexo in 'Mm':
        homemmaisvelho = idade
        nomemaisvelho = nome

    if sexo in 'Mm' and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheresmenos20 = mulheresmenos20 + 1

    if mulheresmenos20 > 1:
        mulheres = 'são'
    else:
        mulheres = 'é'

print(f'A média de idade dessas pessoas é de {media} anos!')
print(f'O homem mais velho é {nomemaisvelho}')
print(f'A quantidade de mulheres com menos de 20 anos {mulheres} {mulheresmenos20}')
