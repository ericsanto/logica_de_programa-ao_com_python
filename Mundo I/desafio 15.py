kmPercorrido = float(input('Quantos Km rodados? '))
diasAlugados = int(input('Quantos dias alugados? '))
preçoPorKmPercorrido = kmPercorrido * 0.15
preçoPorDiasAlugados = diasAlugados * 60
preçoFinal = preçoPorKmPercorrido + preçoPorDiasAlugados
print('O total a pagar é de {:.f}R$'.format(preçoFinal))