sexo = str(input('Digite o sexo: [M/F]: ')).upper().strip()[0]
while sexo == 'M' or 'F':
    if sexo == 'M':
        print('Seu sexo é masculino')
        break
    elif sexo == 'F':
        print('Seu sexo é feminino')
        break
    else:
        if sexo != 'M' or 'F':
            sexo = str(input('Digite o sexo novamente. Só é aceito'
                             '\nMasculino = [M]\nFeminino = [F]\n')).upper().strip()[0]
        elif sexo == 'M':
            print('Seu sexo é masculino')
        elif sexo == 'F':
            print('Seu sexo é feminino')
print('OBRIGADO!')