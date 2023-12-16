numero = int(input('Digite um número: '))
par = numero % 2 #(se resto da divisão por 2 for 0, o número é par)
if par == 0:
    print(f'{numero} é par')
else:
    print(f'{numero} é impar')