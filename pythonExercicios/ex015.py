#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado


# Valor do carro por dia R$60,00
# Valor da Kilometregem R$0,15 rodado
#
dias =int(input('Quantos dias o veiculo ficou alugado ? '))
km = float(input('Quantos Km  foram precorridos pelo veiculo '))

valord  = dias * 60.00
valorkm = km * 0.15


print('O valor a ser pago pelo aluguel do Veiculo  é de R$ {:.2f} . \n'
      ' e o valor dos dias alugados é de R$  {:.2f} \n'
      ' O valor dos KM rodados foram de R$ {:.2f}'.format((valord + valorkm), valord, valorkm))
