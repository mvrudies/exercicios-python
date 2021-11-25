#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tota_mulher_20 = 0
for p in range (1,5):
    print('=' * 25)
    print('{}º PESSOA'.format(p))
    nome =  str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo =  str(input('SEXO [M\F]:')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < C20:
        tota_mulher_20 += 1

media = soma_idade /4
print('A média de idade do grupo é {} anos '.format(media))
print('O homem mais velho é o {} e tem {} anos !'.format(nome_velho, maior_idade_homem))
print('E {} mulheres tem menos que 20 anos !'.format(tota_mulher_20))