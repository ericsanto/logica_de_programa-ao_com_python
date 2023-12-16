def leiaDinheiro(msg):
    valido=False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERRO! DIGITE UM NÚMERO VÁLIDO!!')
        if entrada.isnumeric():
            valido = True
            return float(entrada)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return int(n)



def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('ERRO! por favor, digite um numero real válido.')
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar os dados!!')
            return 0
        else:
            return float(n)

