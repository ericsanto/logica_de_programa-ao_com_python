from pacote import moeda, dados

p = dados.leiaDinheiro('Digite o preço: ')
print(moeda.resumo(p, 20, 12))