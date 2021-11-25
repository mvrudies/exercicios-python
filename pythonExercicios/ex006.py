#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
#d = n * 2
#t = n * 3
#r = n ** (1/2) #Raiz quadrada
#print("O número digitado foi {} \n Seu dobro é {} ,\n Seu triplo {} e \n A raiz quadrada é {:.2f} ".format(n, d, t, r))

print("O número digitado foi {} \n Seu dobro é {} ,\n Seu triplo {} e \n A raiz quadrada é {:.2f} ".format(n,(n*2),(n*3), pow(n,(1/2))))