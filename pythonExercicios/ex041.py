#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date
cores = {'limpa':       '\033[m',
          'azul' :      '\033[34m',
          'amarelo' :   '\033[33m',
          'vermelho' :  '\033[31m',
          'verde' :     '\033[32m',
          'roxo'  :     '\033[35m',
          'ciano' : '    \033[36m'
          }
ano_atual = date.today().year
ano_nascimento = int(input('Qual Ano o atleta nasceu ? '))
idade = ano_atual - ano_nascimento
print('O Atleta tem {}{}{} anos !'.format(cores['verde'],idade,cores['limpa']))
if idade <= 9:
   print('Classificação  {} MIRIM'.format(cores['ciano']))
elif idade <= 14 :
    print('Classificação {} INFANTIL'.format(cores['amarelo']))
elif idade <= 19:
    print('Classificação {} JÚNIOR'.format(cores['verde']))
elif idade <= 25:
    print('Classificação {} SÊNIOR'.format((cores['roxo'])))
else:
    print('Classificação {} MASTER'.format(cores['vermelho']))
