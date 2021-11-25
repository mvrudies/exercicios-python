#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
palpite = 0
print('=-' * 6, 'JOGO DA ADVINHAÇÃO', '=-' *6)
computador = int(randint(0,10))
print('Vou pensar num número entre 0 e 10 tente adivinhar ')
print('Processando...')
acertou = False
while not acertou:
    palpite += 1
    jogador = int(input('Em que número em pensei ?'))
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente mais uma vez !')
        else:
            print('Menos...tente novamente !')
print('Você falou {} e eu pensei {} VOCÊ ACERTOU !'.format(jogador,computador))
print('Precisou de {} palpites para me vencer ! '.format(palpite))