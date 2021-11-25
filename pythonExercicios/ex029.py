#Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

print('==' * 25)
print('*** SISTEMA DE VERIFICAÇÃO VELOCIDADE ****')
velocidade = float(input("Qual a velocidade de do veiculo ?"))
sleep(3)
if velocidade > 80:
    print('MULTADO! VOCÊ EXCEDEU O LIMITE DE VELOCIDADE PERMITIDO QUE É DE 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança ')
print('*** FIM DO PROGRAMA ***')

print('==' * 25)

#if velocidade <= 80 :
#    print('VELOCIDADE DENTRO DO PATRÃO')
#else:
#    multa = velocidade ** 7
#    print('O VEICULO SUPEROU A VELOCIDADE E SERÁ MULTADO EM R${:.2f}'.format(multa))
