#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('=-'* 5, ' JOKENPÔ','=-' * 5)
print('[0] PEDRA \n'
      '[1] PAPEL \n'
      '[2] TESOURA \n')
jogador = int(input('Qual sua jogada ?'))
sleep(1),print('JO'),sleep(1),print('KEN'),sleep(1),print('PO !!!')
print('=-' * 14)
print('computador jogou {}'.format(itens[computador]))
print('Jogador escolheu  {}' .format(itens[jogador]))
print('=-' * 14)
if computador == 0:   #Computador jogou PEDRA
      if   jogador == 0:# Jogador jogou PEDRA
            print('EMPATE!')
      elif jogador == 1:# Jogador jogou PAPEL
            print('JOGADOR VENCEU!')
      elif jogador == 2:# Jogador jogou TESOURA
            print('COMPUTADOR VENCEU!')
      else:
            print('JOGADA INVALIDA')
elif computador == 1: #Computador jogou PAPEL
      if   jogador == 0:# Jogador jogou PEDRA
            print('COMPUTADOR VENCEU!')
      elif jogador == 1:# Jogador jogou PAPEL
            print('EMPATE!')
      elif jogador == 2:# Jogador jogou TESOURA
            print('JOGADOR VENCEU"')
      else:
            print('JOGADA INVALIDA')
elif computador == 2 :#Computador jogou TESOURA
      if   jogador == 0:# Jogador jogou PEDRA
            print('JOGADOR VENCEU!')
      elif jogador == 1:# Jogador jogou PAPEL
            print('COMPUTADOR VENCEU')
      elif jogador == 2:# Jogador jogou TESOURA
            print('EMPATE!')
      else:
            print('JOGADA INVALIDA')



