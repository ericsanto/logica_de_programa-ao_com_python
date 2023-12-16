def ficha(nome='', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


jogador = str(input('Nome do Jogador: '))
numgols = str(input('Gols: '))
if numgols.isnumeric():
    numgols = int(numgols)
else:
    numgols = 0
if jogador.strip() == '':
    ficha(gols=numgols)
else:
    ficha(jogador, numgols)

print(ficha())
