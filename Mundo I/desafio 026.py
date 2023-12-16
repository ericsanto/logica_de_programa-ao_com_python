frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra (A) apareceu {} vezes na frase'.format(frase.count('A')))
print('A letra (A) aparceu pela primeira vez na {} posição'.format(frase.find('A')+1))
print('A letra (A) aparecu pela última vez na posição {}'.format(frase.rfind('A')+1))


