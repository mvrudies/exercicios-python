#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#$0 – 1 – 1 – 2 – 3 – 5 – 8
print('=' * 25)
print('SEQUÊNCIA DE FIBONACCI')
print('=' * 25)

n = int(input("Que termo deseja encontrar: "))
t1 = 0
t2 = 1
print('~' * 50)
print('{} ➔ {} ➔'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' {} ➔ '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')

#if (n==1) or (n==2):
#    print("1")
#else:
#    count=3

#    while count <= n:
#        termo = ultimo + penultimo
#        penultimo = ultimo
#        ultimo = termo
#        count += 1
#        print(termo, '➔ ', end ='')
#print('FIM')
print('~' * 50)