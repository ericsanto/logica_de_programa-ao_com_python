def multiplicacao(largura, comprimento):
    m = largura * comprimento
    print(f'O valor da área de um terreno {largura}x{comprimento} é igual a:', end=' ')
    print(f'{m} metros²')


print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
multiplicacao(largura, comprimento)
