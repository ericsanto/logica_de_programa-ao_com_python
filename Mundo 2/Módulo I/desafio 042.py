ladoA = float(input('\033[0;31m Digite o valor do lado "a": '))
ladoB = float(input('\033[1;32m Digite o valor do lado "b": '))
ladoC = float(input('\033[3;35m Digite o valor do lado "c": '))
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoC + ladoB > ladoA:
    print('A soma das retas formam um triângulo', end='')
else:
    print('\033[1;34mA soma das retas não formam um triângulo')
    exit()
if ladoA == ladoB == ladoC:
    print(' Equilátero')
elif ladoA != ladoB != ladoC != ladoA:
    print(' Escaleno')
else:
    print(' ISÓCELES')
