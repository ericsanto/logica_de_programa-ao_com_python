def notas(*n, sit):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n:uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional indicando se deve ou não adicionar a situação
    :return: dicioonário com várias informações sobre a situação da turma
    """
    caderneta = {}
    caderneta['total'] = len(n)
    caderneta['maior'] = max(n)
    caderneta['menor'] = min(n)
    caderneta['média'] = sum(n) / len(n)
    if sit == True:
        caderneta['situação'] = sit
        if caderneta['média'] > 7:
            caderneta['situação'] = 'ÓTIMA'
        elif caderneta['média'] > 5:
            caderneta['situação'] = 'RAZOÁVEL'
        else:
            caderneta['situação'] = 'PÉSSIMA'
    return caderneta



resp = notas(10, 10, 10, sit=False)
print(resp)
help(notas)

