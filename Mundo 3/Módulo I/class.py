import copy

'''class Pessoas:


p1 = Pessoas()
p1.nome = str(input('Digite seu none: '))
p1.sobrenome = str(input('Digite seu sobrenome: '))
p1.idade = int(input('Digite sua idade: '))
print(f'{p1.nome}{p1.sobrenome}')'''


'''class ControleRemoto:
    def __init__(self, cor='', altura=0, profundidade=0, largura=0):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura


controle_remoto = ControleRemoto('vermelho', 10, 2, 2)
print(
    f'O controle remoto possui as características:{controle_remoto.cor}, {controle_remoto.altura}cm de altura,'
    f' {controle_remoto.largura}cm de largura e '
    f'{controle_remoto.profundidade}cm de profundidade')'''


'''class Clientes:
    def __init__(self, nome, email='', plano=''):
        self.nome = nome
        self.email = email
        self.plano = plano

    def alimento(self, alimento=''):
        return f'{self.nome} está comendo {alimento}'

    def Complemento(self, complemento):
        return f'{complemento}'


cliente = Clientes('Éric Santos')
alimento = cliente.alimento()
complemento = cliente.Complemento('Chocolate')
print(f'{cliente.alimento("Maçã")} com {cliente.Complemento(complemento)}')'''

class Camera:
    def __init__(self, nome, filmando=False, fotografar=False):
        self.nome = nome
        self.filmando = filmando
        self.fotografar = fotografar

    def filmar(self):
        if not self.filmando:
            print(f'A {self.nome} iniciou a gravação')
            self.filmando = True
        else:
            if self.filmando == True:
                print(f'A {self.nome} já está filmando')

    def fotografia(self):
        if not self.filmando:
            print(f'A {self.nome} fotografou o momento mais querido (:')
            self.fotografar = True
        else:
            if self.filmando == True:
                print(f'A {self.nome} não consegue fotografar quando esyá gravando')
                return




c1 = Camera('Sony')
c1.filmar()
c1.fotografia()
c1.filmar()
c2 = Camera('Canon')
c2.filmar()
c2.fotografia()