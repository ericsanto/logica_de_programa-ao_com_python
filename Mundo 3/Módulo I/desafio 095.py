jogadores = {}
gols = []
conjunto_de_jogadores = []
tot_gols = 0
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogadores['gols'] = gols[:]
    jogadores['total'] = sum(gols)
    gols.clear()
    conjunto_de_jogadores.append(jogadores.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S(para SIM) ou N(para NÃO)')
    if resp == 'N':
        break
    print('-=' * 30)
print()
for i in jogadores.keys():
    print(f'{i.capitalize():<15}', end=' ')
print()
print('-' * 30)
for k, v in enumerate(conjunto_de_jogadores):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<12}', end=' ')
    print()
while True:
    dados = int(input('Mostrar dados de qual jogador? [999] para encerrar!'))
    if dados == 999:
        break
    if dados >= len(conjunto_de_jogadores):
        print(f'ERRO! Não existe jogador referente ao código da busca')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {conjunto_de_jogadores[dados]["nome"]}')
        for i, g in enumerate(conjunto_de_jogadores[dados]['gols']):
            print(f'    => Na partida {i + 1} fez {g} gols')