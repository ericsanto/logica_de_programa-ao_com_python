print('=' * 20)
print(' 10 TERMOS DE UMA PA ')
print('=' * 20)
primeiroTermo = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimoTermo = primeiroTermo + (11 - 1) * r
for i in range(primeiroTermo, decimoTermo, r):
    print(f'{i}', end=' -')
print('FIM!')
