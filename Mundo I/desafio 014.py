tempEmCelsius = float(input('Informe a temperatura em C: '))
clesiusParaFahrenheit = (tempEmCelsius * 9/5) + 32
print('A temperatura em graus Fahrenheit é {}F'.format(clesiusParaFahrenheit))
celsiuParaKelvin = tempEmCelsius + 273.15
print('O resultado da conversão de Celsius para Kelvin é {}K'.format(celsiuParaKelvin))
tempEmFaharenheit = float(input('Informe a temperatura em F: '))
fahrenheitParaCelsius = (tempEmFaharenheit - 32) / 1.8000
print('A temperatura em graus Celsius é {:.1f}C'.format(fahrenheitParaCelsius))
fahrenheirParaKelvin = (tempEmFaharenheit + 459.67) * 5/9
print('A temperatura em Kelvin é {:.2f}K'.format(fahrenheirParaKelvin))
tempEmKelvin = float(input('Digite a temperatura em Kelvin: '))
kelvinParaCelsius = 273.15 - tempEmCelsius
print('O resultado da conversão de Kelvin para Celsius é {}'.format(kelvinParaCelsius))
kelvinParaFahrenheit = (tempEmKelvin * 9 / 5) - 459.67
print('O resultado da conversão de Kelvin para Fahrenheit é{}'.format(kelvinParaFahrenheit))