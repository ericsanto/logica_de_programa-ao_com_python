exp = str(input('Digite a expressão: ')).strip()
if exp.count('(') == exp.count(')'):
    print('A expressão é válida')
else:
    print('A expressão é inválida ')