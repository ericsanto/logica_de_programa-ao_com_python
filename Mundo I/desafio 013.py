salary = float(input('Digite o seu salário R$: '))
newSalary = salary + (salary * (15/100))
print('Seu novo salário com 15% de aumento é de {:.2f}R$'
      .format(newSalary))
