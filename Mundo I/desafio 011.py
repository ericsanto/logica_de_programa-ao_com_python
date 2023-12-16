largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
quantidadeDeTinta = area / 2
print('A área da parede é {}m². A quantidade mínima de tinta necessária para pintar essa parede é de {}L'
      .format(area, quantidadeDeTinta))
