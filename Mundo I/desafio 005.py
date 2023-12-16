#Faça um programa que leia um número inteiro na tela
#e mostre na tela o seu sucessor e o seu antecessor

number = int(input('Digite um número: '))
antecessor = number - 1
sucessor = number + 1
print('O antecessor do número escolhido é {}{}{}'.format('\033[1;31m', antecessor, '\033[m'), 'e o sucessor é {}{}{}'.format('\033[1;32m', sucessor, '\033[m'))