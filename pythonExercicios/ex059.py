#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
valor_1 = int(input('DIGITE O PRIMEIRO VALOR :'))
valor_2 = int(input('DIGITE O SEGUNDO VALOR  :'))
escolha = 0
while escolha != 5:
    print('''
          [1] Somar 
          [2] Multiplicar
          [3] Mostar o maior 
          [4] Novos números 
          [5] Sair do Programa''')
    escolha = int(input('Qual sua opção : '))
    if escolha == 1:
        soma = valor_1 + valor_2
        print('A soma entre {} + {} é {}'.format(valor_1,valor_2,soma))
    elif escolha == 2:
        multi= valor_1 * valor_2
        print('A multiplicação entre {} x {} é {}'.format(valor_1,valor_2,multi))
    elif escolha == 3:
        if valor_1 > valor_2:
            print('O Valor 1 é o maior !')
        elif valor_1 < valor_2:
            print('O Valor 2 é maior !')
        else:
            print('Os valores são iguais!')
    elif escolha == 4:
        print('Você pode escolher os valores novamente ! ')
        valor_1 = int(input('DIGITE O PRIMEIRO VALOR :'))
        valor_2 = int(input('DIGITE O SEGUNDO VALOR  : '))
    elif escolha == 5:
        print('Finalizando')
        sleep(3)
    else:
        print('Opção Inválida. Tente novamente !')
    print('=-'*15)
print('Fim do Programa ...')


