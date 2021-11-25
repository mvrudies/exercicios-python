#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("Digite a temperatuda em graus Celsius "))
f = ((9 * c) / 5) + 32
k = c + 273
print('A temperatura de {} Celsius corresponde a {} Fahrenheit'.format(c,f))
print('A temperatura de {} Celsius corresponde a {} Kelvin'.format(c,k))
