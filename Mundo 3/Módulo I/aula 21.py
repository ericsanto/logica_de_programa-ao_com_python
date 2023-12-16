#help(input)

'''docstrings

Exemplo:
def contador(i, f, p)
"""
->fAZ UMA CONTAGEM E MOSTRA NA TELA.
:parametro i: inicio da contagem
:parametro f: fim da contagem
:parametro p: passo da contagem
:return: sem retorno
"""
    c = i
    while c <= f
    print(f'{c}', end='')
    c += p

docstring é a explicação de uma função. Deve-se uutilizar
aspas duplas 3x como no exemplo acima.
'''

'''def contador(i, f, p):
    """
    ->fAZ UMA CONTAGEM E MOSTRA NA TELA.
    :parametro i: inicio da contagem
    :parametro f: fim da contagem
    :parametro p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p


help(contador)'''


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é: {s}')


somar(2, 4, 6)