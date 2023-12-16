def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'{msg.center(tam)}')
    print('~' * tam)


while True:
    escreva(str(input('Digite a mensagem que você deseja: ')))
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!')
    if resp == 'N':
        break

