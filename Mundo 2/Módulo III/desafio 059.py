from time import sleep
saida = False
primeiroValor = int(input('Primeiro valor: '))
segundoValor = int(input('Segundo valor: '))
while not saida:
    print('\n[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa\n')
    opção = int(input('Qual é sua opção?: '))
    if opção == 1:
        soma = primeiroValor + segundoValor
        print(f'A soma dos valores é igual a {soma}')
    elif opção == 2:
        multiplicação = primeiroValor * segundoValor
        print(f'A multiplicação dos valores é {multiplicação}')
    elif opção == 3:
        if primeiroValor > segundoValor:
            print(f'{primeiroValor} é maior que {segundoValor}')
        elif segundoValor > primeiroValor:
            print(f'{segundoValor} é maior que {primeiroValor}')
    elif opção == 4:
        n1 = int(input('Digite o novo número: '))
        n2 = int (input('Digite outro novo número: '))
    elif opção == 5:
        saida = True
    elif opção != 1 and 2 and 3 and 4 and 5:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Você saiu do programa!')
