carteira = float(input('Quantos reais você tem na carteira? R$ '))
dolar = carteira / 3.27
print('Você pode comprar {:.2f}US$ dólares com o dinheiro contido na carteira!'
      .format(dolar))
