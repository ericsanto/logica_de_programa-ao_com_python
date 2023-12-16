from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if 18 <= idade <= 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 16 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: NÃO VOTA'


nasc = int(input('EM qual ano você nasceu? '))
print(voto(nasc))

