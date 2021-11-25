# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

frase = str(input('Digite uma frase : ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('você digitou {} e o inverso é {} '.format(junto, inverso))
if inverso == junto:
    print('É PALÍNDROMO')
else:
    print('A frase não é um palindromo !')
