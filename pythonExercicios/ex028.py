#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-=-' * 20)
computador = int(randint(0,5)) #Faz o computador "pensar"
print('Vou pensar em um número entre 0 e 5 . Tente advinhar ....')
print('PROCESSANDO...')
sleep(1)
jogador = int(input('Em que número eu pensei ? '))
sleep(1)
if jogador == computador :
    print('\033[1:32m PARABÉNS VOCÊ CONSEGUIU VENCER! \033[m')
else:
    print('\033[1:31m EU GANHEI ! VOCÊ NÃO CONSEGUIU ME VENCER !\033[m')
print('O  número que eu pensei  foi {} e você falou {}...'.format(computador,jogador))
print('Tente novamente ! ')
print('-=-' * 20)



#
#if jogador == computador:
#    print("VOCÊ ACERTOU !")
#if jogador < computador:
#    print('VOCÊ CHUTOU BAIXO DEMAIS !')
#else:
#    print('VOCÊ CHUTOU ALTO DEMAIS')