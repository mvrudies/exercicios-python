#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input("Digite Algo")
print('O que foi digitado é do tipo :', type(n))
print("É um valor númerico ?",n.isnumeric())
print("São somente letras ?", n.isalpha())
print("É alfanúmerico?", n.isalnum())
print("São Letras maiúsculas ?", n.isupper())
print("São Letras minúsculas ?", n.islower())
print("É um espaço ?", n.isspace())
print("O valor é um capitalizada ?", n.istitle())
