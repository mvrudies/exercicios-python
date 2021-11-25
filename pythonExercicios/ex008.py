#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = int(input('Digite o valor em METROS: '))
c = m * 100
mi = m * 1000
print('O valor de {} METROS equivale a {} CENTIMETROS e {} MILIMETROS'.format(m, c, mi))