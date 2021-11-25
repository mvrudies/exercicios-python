#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
x = 0
while True:
    num = int(input('Quer ver a tabuada de qual valor : '))
    print('-' * 32)
    if num < 0 :
        break
    else:
        print(f'A tabuada do {num} é : ')
        for c in range (1,11):
         print(f'{num} X {c} = {num * c}')
    print('-' * 32)
    x += 1
print(f'PROGRAMA EXECUTADO  {x} VEZES \n'
      f'PROGRAMA ENCERRADO !')



