from datetime import date
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de Nascimento: '))
dados['carteira de trabalho '] = int(input('Carteira de Trabalho (0 não tem): '))
idade = date.today().year - dados['idade']
dados['idade'] = idade
aposentadoria = (dados['idade'] + (dados['ano de contratação'] + 35) - datetime.now().year)
if dados['carteira de trabalho '] == 0:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
    print(f'Pessoa não possui carteira de trabalho!')
else: 
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: '))
    dados['aposentadoria'] = aposentadoria
    print('-=' * 30)
    print(f'{dados}')
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')