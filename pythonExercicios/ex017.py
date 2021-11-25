#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input('Digite o comprimento do cateto oposto : '))
ca = float(input('Digite o comprimento do cateto adjacente'))
hi = math.hypot(co, ca)
''' hi = (co ** 2 + ca ** 2) ** (1/2) FORMULA MATEMATICA '''
print('A Hipotenusa  vai medir {:.2f}'.format(hi))
