n1 = float(input('Digite a nota da N1 :'))
n2 = float(input('Digite a nota da N2 :'))
n3 = float(input('Digite a nota da N3 :'))
print('*** CALCULANDO AS NOTAS ***')
print('*** MÉDIA FINAL PRONTA ! ***')
m = (n1 + n2+ n3)/3
print('Sua nota final é : {:.1F}'.format(m))
print('*** STATUS ***')
if m >=6:
    print('*** ALUNO APROVADO ***')
else:
    print('*** ALUNO REPROVADO ***')
print('*** FIM DO PROGRAMA ***')