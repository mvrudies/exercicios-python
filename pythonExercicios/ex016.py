#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
from math import trunc

real = float(input('Digite  um número real : '))
print('O Número digitado foi {} e sua porção inteira equivale a {:.0f}'.format(real, real))
print('O Número digitado foi {} e sua porção inteira equivale a {}'.format(real, trunc(real)))
print('O Número digitado foi {} e sua porção inteira equivale a {}'.format(real, int(real)))
