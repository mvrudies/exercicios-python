#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

# Aumentos múltiplos
cores = {'limpa':       '\033[m',
         'azul':        '\033[34m',
         'amarelo':     '\033[33m',
         'vermelho':    '\033[31m',
         'verde':       '\033[32m',
         'roxo':        '\033[35m',
         'ciano':       '\033[36m'
         }

nome = str(input('Qual o seu nome ?'))
salario = float(input('Qual o seu salário ? R$'))

if salario <= 1250.00:
    reajuste = salario + (0.15 * salario)  # 10%
else:
    reajuste = salario + (0.10 * salario)  # 15%

print('Olá {}{}{} o seu salário  subiu de R$ {}{:.2f}{} para R$ {}{:.2f}{} ! '.format(cores['azul'],nome,cores['limpa'],cores['vermelho'],salario,cores['limpa'],cores['verde'],reajuste,cores ['limpa']))