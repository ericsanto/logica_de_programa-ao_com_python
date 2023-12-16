distanciaDaViagem = float(input('Qual a distância da viagem? '))
precoDaPassagem = 0.50 * distanciaDaViagem
if distanciaDaViagem <= 200:
    print(f'O preço da passagem foi {precoDaPassagem} $')
else:
    print('O preço da passagem foi', distanciaDaViagem * 0.45)