#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# , que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
total = 0
num = 0
num = int(input('Digite um número [999 para parar] : '))
while num != 999:
      cont += 1
      total = total + num
      num = int(input('Digite um número [999 para parar] : '))
print('Você digitou {} números e a soma entre eles foi {} !'.format(cont,total))