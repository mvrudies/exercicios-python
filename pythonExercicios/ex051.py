#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 18)
print('10 TERMOS DE UMA PA ')
print('=' * 18)

primeiro_termo = int(input('Primeiro Termo :'))
razão = int(input('Razão : '))
décimo = primeiro_termo + (10 - 1) * razão

for c in range (primeiro_termo, décimo + razão, razão):
    print('{}'.format(c), end= ' ➔ ')
print('ACABOU')
