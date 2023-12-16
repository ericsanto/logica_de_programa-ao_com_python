from datetime import date
anoAtual = date.today().year
dataDeNascimeto = int(input('Em que ano você nasceu? '))
idade = anoAtual - dataDeNascimeto
print(f'O atela tem {idade} anos', end='')
if idade <= 9:
    print('. Por isso, ele é mirim')
elif idade > 9 and idade <= 14:
    print('. Por isso, ele é infantil')
elif idade > 14 and idade <= 19:
    print('. Por isso, ele é junior')
elif idade == 20:
    print('. Por isso, ele é sênior')
elif idade > 20:
    print('. Por isso, ele é master')

