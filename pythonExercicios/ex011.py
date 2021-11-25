#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


al = float(input('Digite a ALTURA em metros: '))
la = float(input('Digite a LARGURA em metros: '))
mq = al * la
ti = mq / 2

print('A área dessa parede é {} X {} equivalente a {}m² e precisamos de {} litros de tinta para pintar toda área'.format(al, la, mq, ti))


