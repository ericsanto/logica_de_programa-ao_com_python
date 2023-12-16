def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        print(f'{c} x ', end=' ')
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3
