#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('-' * 50)
print('LOJA BARATO DEMAIS'.center(50))
print(('-'* 50))
total = 0
menorValor = 0
maior1000 = 0
menorValor = 0
menorProduto = ' '
cont = 0
while True:
    produto = str(input('Qual o nome do produto : ')).strip()
    valor = float(input('Qual o preço: R$'))
    total += valor
    cont += 1
    if valor >= 1000:
     maior1000 += 1
    if cont == 1 or valor < menorValor:
        menorValor = valor
        menorProduto = produto
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N] : ')).strip().upper()[0]
    if continua == 'N':
        break
print('-' * 25, 'FIM DO PROGRAMA'.center(0), '-' * 25)
print(f'O Total das compras é R${total:.2f}')
print(f'Temos {maior1000} produtos custando mais que R$1000.00 ')
print(f'O produto mais barato foi {menorProduto} que custa R${menorValor:.2f}')