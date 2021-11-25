#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância da viagem  ? '))
print('Você está prestes a iniciar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
   # print('O preço da passagem para uma viagem de {}Km vai ser de R${:.2f}'.format(distancia, preço))
else:
    preço = distancia * 0.45
    #print('O preço da passagem para uma viagem de {}Km vai ser de R${:.2f}'.format(distancia, preço))
print('E o preço da sua passagem será de R${:.2f} '.format(preço))

#if simplificado
#preço = distancia  * 0.50 if distancia <=200 else distancia * 0.45