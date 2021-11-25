#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a PRIMEIRA NOTA: '))
n2 = float(input('Digite a SEGUNDA NOTA: '))
m = (n1 + n2 ) / 2
print("A nota media do aluno é {:.1f}".format(m)) #foco no {:.1f}