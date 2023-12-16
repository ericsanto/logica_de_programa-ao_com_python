import random

a = input('Digite o anome do aluno: ')
b = input('Digite o nome do aluno: ')
c = input('Digite o nome do aluno: ')
d = input('Digite o nome do aluno: ')
list = [a, b, c, d]
sorteio = random.choice(list)
print(f'O aluno sorteado foi: {sorteio}')