def fatorial(num, show):
    """
    fatorial(n, show=False)
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c} x ', end=' ')
            if c == 1:
                print('=', end=' ')
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a: {fatorial(n, True)} ')
help(fatorial)