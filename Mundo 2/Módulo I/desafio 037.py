num = int(input('Digite um número inteiro: '))
print('Escolha um das bases para conversão: \n'
      '[1] Converter para BINÁRIO \n'
      '[2] Converter para OCTAL \n'
      '[3] Converter para HEXADECIMAL')
num2 = int(input('Sua opção: '))
if num2 == 1:
    print(bin(num)[2:])
elif num2 == 2:
    print(oct(num)[2:])
elif num2 == 3:
    print(hex(num)[2:])
else:
    print('OPÇÃO INVÁLIDA. Escolha de 1 a 3')