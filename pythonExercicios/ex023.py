#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

'''POR STRING'''
#numero =  str(input('Digite um número: '))
#print('Analizando o número {} podemos afirmar que ele possui ...'.format(numero))
#print('Unidade:  {}'  .format(numero[3]))
#print('Dezena:   {}'  .format(numero[2]))
#print('Centena:  {}'  .format(numero[1]))
#print('Milhar:   {}'  .format(numero[0]))

'''Forma matematica '''
num = int(input('Informe um número: '))
u = num // 1    % 10
d = num // 10   % 10
c = num // 100  % 10
m = num // 1000 % 10

print('Analizando o número {} podemos afirmar que ele possui ...'.format(num))
print('Unidade:  {}'  .format(u))
print('Dezena:   {}'  .format(d))
print('Centena:  {}'  .format(c))
print('Milhar:   {}'  .format(m))