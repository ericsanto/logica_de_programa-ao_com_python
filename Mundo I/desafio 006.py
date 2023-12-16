number = int(input('Digite um valor: '))
dobroNumber = number * 2
triploNumber = number * 3
raizNumber = number ** 0.5
print('O dobro do número é {}{}{},\no triplo é {}{}{}\na raiz quadrada é {}{:.2f}{}'
      .format('\033[3;33m', dobroNumber,'\033[m', '\033[3;35m', triploNumber, '\033[m',
             '\033[3;31m', raizNumber, '\033[m'))
