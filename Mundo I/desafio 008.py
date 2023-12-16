a = float(input('Digite um valo em metros: '))
valorConvertidoEmDecimetro = a * 0.1
valorConvertidoEmCentimetros = a * 100
valorConvertidoEmMilimetros = a * 1000
valorConvertidoEmDecametro = a / 10
valorConvertidoEmQuilometros = a / 1000
valorConvertidoEmHectometros = a / 100
print(' O valor em Decimetro é {}dm\n em Centímetros é {}cm\n em Milimetros é {}mm\n'
      ' em Decâmtro é {}dam\n em Quilômetro é {}Km\n em Hectômetro é {}Hm'
      .format(valorConvertidoEmDecimetro, valorConvertidoEmCentimetros,
              valorConvertidoEmMilimetros, valorConvertidoEmDecametro,
              valorConvertidoEmQuilometros, valorConvertidoEmHectometros))
