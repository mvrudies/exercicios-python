#Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input("Digite um número"))
#su = n + 1
#an = n - 1
#print('O número digitado foi {}, o Sucessor é {} e o Antecessor é o {}'.format(n, su, an))

print('O número digitado foi {}, o Sucessor é {} e o Antecessor é o {}'.format(n, (n+1), (n-1)))
