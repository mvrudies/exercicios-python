#ython 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

print(('*'*5),'VERIFICAÇÃO DE MÉDIAS',('*'*5))
n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a segunda nota : '))
media = (n1+n2) / 2
print('Aluno tirando {} e {} , a média é {} '.format(n1,n2,media))
if media >= 7.0:
      print('ALUNO APROVADO')
elif media >= 5 and media < 6.9:
     print('ALUNO EM RECUPERAÇÃO')
else:
      print('ALUNO REPROVADO')
