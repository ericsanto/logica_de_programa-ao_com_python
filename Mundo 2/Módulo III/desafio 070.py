totCompras = 0
tot1000 = 0
produtoMaisBarato = 0
nomeProdutoMaisBarato = ''
cont = 0
print('-' * 50)
print('LOJÃO DO ÉRIC')
print('-' * 50)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    totCompras += preco
    if cont == 1:
        produtoMaisBarato = preco
        nomeProdutoMaisBarato = produto
    else:
        if preco < produtoMaisBarato:
            produtoMaisBarato = preco
            nomeProdutoMaisBarato = produto
    if preco > 1000:
        tot1000 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total de compras foi de R${totCompras}')
print(f'Temos {tot1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato é {nomeProdutoMaisBarato} que custou {produtoMaisBarato}')