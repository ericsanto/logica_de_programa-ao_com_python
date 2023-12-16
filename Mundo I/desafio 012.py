precoNormal = float(input('Digite o preço do produto R$: '))
desconto = precoNormal * (5/100)
novoPreco = precoNormal - desconto
print('O preço do produto com 5% de desconto é de {:.2f}R$'.format(novoPreco))