#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Quanto você tem na carteita ? R$'))
c = r / 3.27

print('Você pode comprar {:.2f} dólares '.format(c))