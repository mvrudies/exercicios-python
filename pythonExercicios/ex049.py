#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print("="*20)
cont = 0
n = int(input('Digite um número qualquer: ' ))
print("="*20)
print('A Tabuada de {} é :'.format(n))
for cont in range (1,11):
    print('{} X {:2} = {}'.format(n,cont,n * cont))
print("="*20)
