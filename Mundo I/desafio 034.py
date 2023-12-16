salario = float(input('Qual o valor do seu salário?'))
if salario >= 1250:
    aumento = salario * (10 / 100)
else:
    aumento = salario * (15 / 100)
print(f'O salário teve um aumento de {aumento} R$. '
      f'Logo, seu novo salário será {salario + aumento} R$ ')
