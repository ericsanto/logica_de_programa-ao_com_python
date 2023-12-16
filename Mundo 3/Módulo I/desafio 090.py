estudante = dict()
estudante['Nome'] = str(input('Nome: ').capitalize())
estudante['Media'] = float(input(f'Média de {estudante["Nome"].capitalize()}: '))
if estudante['Media'] >= 7:
    estudante['situação'] = str('Aprovado')
elif 5 <= estudante['Media'] < 7:
    estudante['situação'] = str('Recuperação')
else:
    estudante['situação'] = str('Reprovado')
for k, v in estudante.items():
    print(f'{k} é igual a {v}')