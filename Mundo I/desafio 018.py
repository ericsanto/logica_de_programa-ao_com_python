import math

numero = float(input('Digite o valor do ângulo: '))
rad = math.radians(numero)
print(' O seno do ângulo de {:.2f}\n é {:.2f}\n O coseno é {:.2f}\n A tangente é {:.2f}'.
      format(numero, math.sin(rad), math.cos(rad), math.tan(rad) ))