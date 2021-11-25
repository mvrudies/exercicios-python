#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite o nome completo: ')).strip()
print('Analisando seu nome ....')
print('Seu nome completo em maiúsculas é {}'.format(nome.upper()))
print('Seu nome completo em minúsculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome)))
print('O nome tem {} caracteres sem contar os espaços'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras !'.format(separa[0],len(separa[0])))