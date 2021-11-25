#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# SOLICITAÇÃO DOS NÚMEROS

n1 = int(input('Digite o primeiro valor :'))
n2 = int(input('Digite o segundo valor  :'))
n3 = int(input('Digite o terceiro valor :'))

# FORMA SIMPLES E EFICAZ
if n1 < n2 and n1 < n3:
    print('O número {} é o menor'.format(n1))
if n2 < n1 and n2 < n3:
    print('O numero {} é o menor'. format(n2))
if n3 < n1 and n3 < n2:
    print('O número {} é o menor'.format(n3))
if n1 > n2 and n1 > n3 :
    print('O número {} é o maior'.format(n1))
if n2 > n1 and n2 > n3:
    print(('O número {} é o maior '.format(n2)))
if n3 > n1 and n3 > n1:
    print('O número {} é o maior '.format(n3))

print('*'*20)

# METODO EXPLICADO PELO CURSO

'''Verificando quem é o menor'''
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
'''Verificando quem é o maior '''
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))