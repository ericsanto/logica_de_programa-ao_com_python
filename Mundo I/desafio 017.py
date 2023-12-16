from math import sqrt

catetoOposto = float(input('Digite o valor do Cateto Oposto: '))
catetAdjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = sqrt(catetAdjacente ** 2 + (catetoOposto ** 2))
print('O valor da hipotenusa é {:.2f}cm'.format(hipotenusa))
