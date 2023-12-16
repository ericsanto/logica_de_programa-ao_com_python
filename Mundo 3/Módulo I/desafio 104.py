def leiaInt(a: str):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('ERRO! Digite um valor numérico inteiro!')


n = leiaInt('Digite um valor numérico: ')
print(f'O valor digitado foi {n}')


