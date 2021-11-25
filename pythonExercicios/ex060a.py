# Exercício Python 060a: Faça um programa que leia um número qualquer e mostre o seu fatorial. (usando for)

f = 1
num = int(input('Digite um número pra mostrar seu fatorial : '))
print('Calculando {}! = '.format(num), end='')
for c in range(1,num):
    print('{} X '.format(num), end='')
    f *= num
    num -= 1
print('= {}'.format(f))
