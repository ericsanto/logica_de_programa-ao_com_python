
times = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético MG', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Fluminense', 'Fortaleza', 'Bragantino',
         'Atlhetico PR', 'Santos', 'Internacional', 'Corinthians', 'Cuiabá',
         'Bahia', 'Goiás', 'Vasco', 'América MG', 'Coritiba')
print('-=' * 18)
print(f'Listas de times do Brasileirão 2023: {times}')
print('-=' * 18)
print('Os 5 primeiros são', times[0:5])
print('-=' * 18)
print('Os 4 útimos são', times[-5:-1])
print('-=' * 18)
print('Times em ordem alfabética:', sorted(times)) #sorted = organiza a tupla em ordem alfabética
print('-=' * 18)
print(f'O São Paulo está na', times.index('São Paulo') + 1, 'posição') #index = diz a posição da string na tupla
