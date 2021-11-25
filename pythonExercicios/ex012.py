#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o Valor do Produto:R$ '))
novo = preço - (preço * 5 / 100)
print('O valor do produto com desconto de 5% é : R$', preço - (preço * 0.05))
print('O produto custava  R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))