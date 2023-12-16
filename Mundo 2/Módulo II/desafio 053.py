frase = str(input('Digite uma frase: ')).strip().upper()
separada = frase.split()
junta = frase.replace(' ', '')
inverso =''
for letra in range(len(junta) -1, -1, -1):
    inverso = inverso + junta[letra]
if junta == inverso:
    print(f'A frase {junta} é um palíndromo. Pois, seu inverso {inverso} tem o mesmo sentido!')
else:
    print(f'A frase {junta} não é um palíndromo. Pois seu inverso {inverso} não tem o mesmo sentido!')





