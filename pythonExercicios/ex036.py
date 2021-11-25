#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Valor do Imovél : R$ '))
valor_salario = float(input('Qual o Salário do comprador : R$ '))
anos_pgto = int(input('Quantos anos de Financiamento : '))

anos_meses = anos_pgto * 12
financiamento = valor_casa / anos_meses
#prestação = valor_casa / (anos *12)
minimo = valor_salario * 30/100
print(minimo)
if financiamento <= valor_salario * 0.30:
    print('Para pagar um imovél de R${:.2F} em {} anos a prestação será de RS{:.2f}'.format(valor_casa, anos_pgto,financiamento))
    print('Financiamento foi CONCEDIDO!')
else:
    print('Para pagar um imovél de R${:.2F} em {} anos a prestação será de RS{:.2f}'.format(valor_casa, anos_pgto,financiamento))
    print('Financiamento NEGADO ')
