numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quartoze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numeros[n]}')
while True:
    resp = str(input('Você quer continuar? [S/N]')).upper().strip()
    if resp == 'S':
        while True:
            n = int(input('Digite um novo número entre 0 e 20: '))
            if 0 <= n <= 20:
                break
            print('Tente novamente. ')
        print(f'Você digitou o número {numeros[n]}')
    if resp == 'N':
        print('ACABOU!. MUITO OBRIGADO POR USAR NOSSO PROGRAMA')





