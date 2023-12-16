import json
classes = 'aula127.json'
class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoas('Éric', 21)
p2 = Pessoas('Tauane', 19)
p3 = Pessoas('Ane Cleide', 38)
p4 = Pessoas('Elielson', 42)
dados = [p1.__dict__, p2.__dict__, p3.__dict__, p4.__dict__]

with open(classes, 'w') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)