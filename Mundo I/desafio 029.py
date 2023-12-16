velocidadeDoCarro = float(input('Qual a velocidade do veículo? '))
limiteDevelocidade = 80
if velocidadeDoCarro > limiteDevelocidade:
    print('Você foi multado na quantia de', (velocidadeDoCarro - 80) * 7,
          'Reais por ultrapassar o limite de velocidade permitido.')

else:
    print('Você não ultrapassou o limite de velocidade estabelecido. Logo, não foi multado')
