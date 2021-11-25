# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

totalCadastro = 0
mulher = 0
homem = 0
maiorIdade = 0

while True:
   print('-' * 20)
   print('CADASTRE UMA PESSOA')
   print('-' * 20)
   idade = int(input('Idade: '))
   sexo = ' '
   while sexo not in 'MF':
      sexo = str(input('Sexo [M/F]')).strip().upper()[0]
   totalCadastro += 1
   if idade >= 18:
      maiorIdade += 1
   if sexo == 'M':
      homem += 1
   if sexo == 'F' and idade <= 20:
      mulher += 1
   print('-' * 20)
   continua = ' '
   while continua not in 'SN':
      continua = str(input('Quer Continuar ? [S/N]')).strip().upper()[0]
   if continua == 'N':
      break
print(f'{totalCadastro} pessoas foram cadastradas !')
print(f'{maiorIdade} tem mais de 18 anos !')
print(f'{homem} são do sexo masculino ')
print(f'{mulher} tem menos de 20 anos !')
