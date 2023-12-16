precoNormal = float(input('Qual o valor do produto? '))
print('[1]: À vista com 10% de desconto\n'
      '[2]: À vista no cartão com 5% de desconto\n'
      '[3]: Em até 2x no cartão\n'
      '[4]: 3x ou mais no cartão\n')
num = int(input('Escolha a forma de pagamento: '))
if num == 1:
    print(f'O novo valor do produto com 10% de desconto é R${precoNormal - (precoNormal * (10/100))}')
elif num == 2:
    print(f'O valor do produto com 5% de desconto é R${precoNormal - (precoNormal * (5/100))}')
elif num == 3:
    print(f'Sua compra será parcelada em 2x no cartão. '
          f'O valor da parcela é de R${precoNormal / 2}. '
          f'Dessa forma, o valor total da compra foi de R${precoNormal}')
elif num == 4:
    num2 = int(input('Quantas parcelas? '))
    precoComJuros = precoNormal + (precoNormal * (20/100))
    valordaparcela = precoComJuros / num2
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(num2, valordaparcela))
    print(f'O valor total do produto com 20% de juros é R${precoComJuros}')
else:
    print('\033[0;31mVocê escolheu uma opção inválida. Tente novamente!')

