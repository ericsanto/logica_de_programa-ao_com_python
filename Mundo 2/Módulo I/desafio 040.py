nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
if media < 5:
    print('\033[0;31m O aluno foi reprovado!')
elif media == 5 or media <= 6.9:
    print('\033[0;33m O aluno está de recuperação!')
else:
    print('\033[0;32m O aluno foi aprovado!')