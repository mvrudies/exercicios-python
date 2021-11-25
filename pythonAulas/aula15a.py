'''cont =1
while  True:
    print(cont,' ... ' ,end='')
    cont += 1
print('Acabou')''


n = s = 0
while n != 999 :  #CONDIÇÃO COM FLAG
    n = int(input('Digite um numero: '))
    s += n
s -= 999     
print('A soma é {}'.format(s)) '''''

n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('A soma é {}'.format(s))
print(f'A soma vale{s}')

nome = 'josé'
idade = 33
print(f'O {nome} tem {idade} anos ')

a1 = 15
b1 = 16

print(f'soma = {a1 + b1}')