dicionario = {}
gols = []
somgols = 0
dicionario['nome do jogador'] = str(input('Nome do Jogador: '))
quantidade_partidas = int(input(f'Quantas partidas {dicionario["nome do jogador"]} jogou? '))
for c in range(0, quantidade_partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
dicionario['gols'] = gols
for i, l in enumerate(gols):
    somgols += l
dicionario['total'] = somgols
print('-=' * 30)
print(f'{dicionario}')
print('-=' * 30)
for k, v in dicionario.items():
    print(f'campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {dicionario["nome do jogador"]} jogou {quantidade_partidas} partidas.')
for q, p in enumerate(gols):
    print(f'    => Na partida {q + 1}, fez {p} gols')
print(f'Foi um total de {somgols}')
