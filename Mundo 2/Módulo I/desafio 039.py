import os

print('Qual o seu gênero? \n'
      '[1] Masculino \n'
      '[2] Feminino \n')

num = int(input('Escolha uma das opções acima: '))
if num == 2:
    print('Apenas pessoas do sexo masculino têm a obrigação de servir.')
    exit()
dataDeNascimento = int(input('Digite o ano de nascimento: '))
dataDeAlistamento = 2023 - dataDeNascimento
QuantidadedeAnosQuePassou = dataDeAlistamento - 18
if 2023 - dataDeNascimento < 18:
    print('\033[0;33mAinda não está no momento de se alistar!!')
    print('Faltam', 18 - dataDeAlistamento, 'anos para você poder se alistar!')
    print('Seu alistamento será no ano de ', 18 - dataDeAlistamento + dataDeNascimento)
elif 2023 - dataDeNascimento == 18:
    print('\033[0;32mJá está no momento de você se alistar!!')
elif 2023 - dataDeNascimento > 18:
    print('\033[0;31mJá passou do momento de se alistar')
    print(f'Passaram-se {QuantidadedeAnosQuePassou} anos do seu alistamento!')
