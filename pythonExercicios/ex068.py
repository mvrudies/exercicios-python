#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)

while True:
    pessoa = int(input('Diga o Valor: '))
    computador = randint(0, 10)
    soma = (computador + pessoa)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar ? [P/I]')).strip().upper()[0]
    print(f'Você jogou {pessoa} e i computador {computador}. A soma foi de {soma}')
    print('DEU PAR' if soma % 2 == 0 else ' DEU ÍMPAR')
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
         if soma % 2 == 1:
             print(f'Você VENCEU !')
             v +=1
         else:
             print('Você PERDEU !')
             break
    print('Vamos Jogar novamente ...')
print(f'Você venceu {v} vezes ! ')


