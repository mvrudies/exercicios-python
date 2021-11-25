#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

número = int(input('Digite um número ='))
div = número % 2
if div == 0:
    print('O Número {} é PAR '.format(número))
else:
    print('O Número {} é ÍMPAR '.format(número))


