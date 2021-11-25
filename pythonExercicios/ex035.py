#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

'''Analizador de TriÂmgulos'''
'''CORES'''
cores = {'limpa':       '\033[m',
          'azul' :      '\033[34m',
          'amarelo' :   '\033[33m',
          'vermelho' :  '\033[31m',
          'verde' :     '\033[32m',
          'roxo' :      '\033[35m'
          }
print('-=-'*15)
print('Analizador de Triângulos')
print('-=-'*15)
s1= float(input('Primeiro seguimento: '))
s2 = float(input('Segundo  seguimento:  '))
s3 = float(input('Terceiro seguimento: '))

a1 = s1 + s2
b1 = s1 + s3
c1 = s2 + s3

print('Os seguintes sequimentos foram digitados \n'
      'PRIMEIRO SEGUIMENTO {}{}{} \n'
      'SEGUNDO  SEGUIMENTO {}{}{} \n'
      'TERCEIRO SEGUIMENTO {}{}{}'.format(cores['vermelho'],s1,cores['limpa'],cores['amarelo'],s2,cores['limpa'],cores['roxo'],s3,cores['limpa'])
)
if a1 > s3 and b1 > s2 and c1 > s1:
    print('Os segumentos acima {}PODEM{} formar um triâmgulo!'.format(cores['verde'],cores['limpa']))
else:
    print('Os seguimentos acima {}NÃO PODEM{} formar um triângulo'.format(cores['vermelho'],cores['limpa']))

        # FIM SOLUÇÃO DO ALUNO #

print('*-*'*15)

if s1 < s2 + s3 and s2 < s1 +s3 and s3 < s1 + s2:
    print('Os segumentos acima {}PODEM{} formar um triâmgulo!'.format(cores['verde'],cores['limpa']))
else:
    print('Os seguimentos acima {}NÃO PODEM{} formar um triângulo'.format(cores['vermelho'], cores['limpa']))