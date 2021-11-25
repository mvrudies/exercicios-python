#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lido
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = media = soma = num = 0
continua = 'S'
num_maior = num_menor = 0
while continua in 'S':
    num = int(input('Digite um número : '))
    cont += 1
    soma += num
    if cont == 1:
        num_maior = num_menor = num
    else:
        if num >= num_maior:
            num_maior = num
        if num <= num_menor:
            num_menor = num

    continua = str(input('Quer continuar [S/N] ? ')).upper()
media = soma / cont
print('Você digitou {} números e a média foi de {}'.format(cont,media))
print('O maior valor foi {} e o menor foi {}'.format(num_maior,num_menor))




