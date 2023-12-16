while True:
    n = int(input('Quer ver a tabuada de qual valor? :'))
    print('-' * 20)
    if n > 0:
        for c in range (0, 11):
            print(f'{n} x {c} = ', n * c)
    elif n < 0:
        break
print('PROGRAMA DE TABUADA ENCERRADO! Volte sempre!')
