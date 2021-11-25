#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
from time import sleep
print('=-=' * 10)
print('\033[1;30;41m ANALIZADOR DE TRIÂNGULOS 2.0\033[m ')
print('=-=' * 10)

s1 = float(input('Digite o primeiro seguimento :'))
s2 = float(input('Digite o segundo seguimento  :'))
s3 = float(input('Digite o terceiro seguimento :'))

print('Analizando ...')
sleep(0.5)

if s1 < s2 + s3 and s2 < s1 +s3 and s3 < s1 + s2:
    print('Os segumentos acima PODEM formar um triâmgulo! ', end='')
    if s1 == s2 == s3:
         print('EQUILATERO!')
    elif s1 != s2 != s3 != s1:
         print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo')