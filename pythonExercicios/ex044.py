#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Digite o valor do produto : R$'))
print('Escolha o forma de pagamento \n'
      '[1] À vista no dinheiro ou cheque com 10% de desconto \n'
      '[2] À vista no cartão de débito ou crédito com 5% de desconto\n'
      '[3] Em até 2x no cartão de crédito com preço normal \n'
      '[4] Em 3x ou mais no cartão de crédito com juros de 20% ')

modo_ptgo = int(input('Insira a forma de pagamento : '))
print('O produto selecionado tem o valor de R${:.2f} '.format(valor_produto))
if modo_ptgo == 1:
    print('O valor do produto é de R${:.2f} e com desconto de 10% vai para R${:.2f}'.format(valor_produto,valor_produto - (valor_produto * 0.10)))
elif modo_ptgo == 2:
    print('O valor do produto é de R${:.2f} e com desconto de 5% vai para R${:.2f}'.format(valor_produto,valor_produto - (valor_produto * 0.05)))
elif modo_ptgo == 3:
    print('Em até 2 vezes no cartão de crédito o preço do produto permaneçe o mesmo R${:.2f}'.format(valor_produto))
elif modo_ptgo == 4:
    parcelas = float(input('Quantas parcelas você deseja : '))
    print('O pagamento do produto em 3x ou mais no cartão de crédito tem um juros de acresimo de 20% \n'
          'ou seja o produto que custava R${:.2f} vai para R${:.2f}, o seja o mesmo tem um acressimo de R${:.2f} .'.format(valor_produto,valor_produto + (valor_produto * 0.20),valor_produto * 0.20))
    print('Sua compra será parcelada em {}x de {:.2f} com juros .'.format(parcelas,(valor_produto+(valor_produto * 0.20)) // parcelas))
else:
    print('Modo de pagamento incorreto ! Tente novamente .')
