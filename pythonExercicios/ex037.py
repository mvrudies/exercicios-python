#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1
# para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('Você terá três opções de conversão \n'
      ' 1 - converter {} para binário \n'
      ' 2 - converter {} para octal   \n'
      ' 3 - converter {} para hexadecimal'.format(numero, numero, numero))
opção = int(input('Qual tipo de conversão você quer ?   '))
print('O conversão escolhida foi a {}'.format(opção))
if opção == 1:
    print('O número {} após a conversão para binário vira {}'.format(numero,bin(numero)[2:]))
elif opção == 2:
    print('O número {} após a conversão para octal vira {}'.format(numero,oct(numero)[2:]))
elif opção == 3:
    print('O número {} após a conversão para hexadecimal vira {}'.format(numero,hex(numero)[2:]))
else:
    print('Você não escolheu nenhuma das 3 opções disponivéis , tente novamente !')
