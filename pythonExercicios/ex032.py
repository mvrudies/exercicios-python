#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Ano bissexto

from datetime import date

ano = int(input('Que ano você quer verificar ? coloque 0 para o atual  :  :'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É BISSEXTO !'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))
