#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


salário = float(input('Digite o valor do salário R$: '))
novo = salário + (salário * 15 / 100)
print('O novo salário do funcionário com 15% de aumento é : R$', salário + (salário * 0.15))
print('Um funcionário que ganhava R${:.2f},com 15% de aumento passa a receber R${:.2f}'.format(salário, novo))
