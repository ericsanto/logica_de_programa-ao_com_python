valorDaCasa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o seu salário: '))
tempo = float(input('Em quantos anos o sr(a) pretende quitar o imóvel?: ')) * 12
valorMensal = valorDaCasa / tempo
print(f'O valor da prestação mensal é de R$\033[1;33m{valorMensal}\033[m')
if valorMensal < salario * (30/100):
    print('\033[1;32mParabéns. O empréstimo foi aprovado')
elif valorMensal == salario * (30/100):
    print('\033[1,32mParabéns. O emprestimo foi aprovado')
else:
    print('\033[1;31mO empréstimo não foi aprovado')