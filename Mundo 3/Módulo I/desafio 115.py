from time import sleep
from desafio115.lib.interface import *
while True:
    resposta = menu(['Criar arquivo', 'Cadastrar nova pessoa', 'Sair do programa'])
    sleep(1)
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do programa')
        break
    else:
        print('ERRO! Digite uma opção válida!')