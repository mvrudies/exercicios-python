# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso_maior = 0
peso_menor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}º pessoa :  '.format(c)))
    if c == 1:
        peso_maior = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print('O maior peso é o {}'.format(peso_maior))
print('O menor peso é o {}'.format(peso_menor))
