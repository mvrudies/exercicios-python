#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=-' * 10)
print('GERADOR DE PA AVANÇADO')
print('=-' * 10)

termo_1 = int(input('Digite o primeiro termo :'))
razão = int(input('Digite a razão da pa : '))
cont = 1
mais = 10
total = 0
while  mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ➔ '.format(termo_1), end= '' )
        termo_1 += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos vocÊ quer mostar a mais : '))
print('Progressão finalizada com {} termos mostrados'.format(total))