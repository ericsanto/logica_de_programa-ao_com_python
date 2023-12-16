n = int(input('Quantos termos você quer?: '))
t1 = 0
t2 = 1
print(f'{t1} - {t2} - ', end='')
t3 = t1 + t2
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f'{t3} - ', end='')
    cont = cont + 1
print(' FIM')

