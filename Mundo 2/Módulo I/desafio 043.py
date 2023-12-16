altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura**2)
print('Seu Indice de massa corporal é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Você está com o peso ideal')
elif imc >= 25 and imc <= 30:
    print('Você está com sobrepeso')
elif imc >=30 and imc <= 40:
    print('ALERTA!. Você está com obesidade')
elif imc > 40:
    print('ALERTA!. Você está com obesidade mórbida')
