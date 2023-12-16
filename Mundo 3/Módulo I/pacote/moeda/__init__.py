'''def aumentar(preco=0, taxa=0, format=False):
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preco=0, format=False):
    res = preco * 2
    return res if format is False else moeda(res)


def metade(preco=0, format=False):
    res = preco / 2
    return res if format is False else moeda(res)
'''


def resumo(preco=0, crescimento=10, reducao=5, moeda='R$', formato=False):
    metade = preco / 2
    dobro = preco * 2
    aumento = preco + (preco * crescimento / 100)
    diminuindo = preco - (preco * reducao / 100)
    def moeda(preco=0, moeda='R$'):
        return f'{moeda}{preco:>.2f}'.replace('.', ',')
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Metade do preço: \t{moeda(metade)}')
    print(f'Dobro do preço: \t{moeda(dobro)}')
    print(f'{reducao}% de redução: \t{moeda(diminuindo)}')
    print(f'{crescimento}% de aumento: \t{moeda(aumento)}')
    print('-' * 30)