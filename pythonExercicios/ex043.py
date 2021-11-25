#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
#e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

print('*' * 5, 'CALCULADORA IMC','*' * 5)
print('TABELA DE IMC \n'
      '- Abaixo de 18,5: Abaixo do Peso\n'
      '- Entre 18,5 e 25: Peso Ideal\n'
      '- Entre 25 até 30: Sobrepeso\n'
      '- Entre 30 até 40: Obesidade\n'
      '- Acima de 40: Obesidade Mórbida')

peso = float(input('Digite seu peso (Kg) :'))
alt = float(input('Digite sua altura (m) :'))
imc = peso / (alt * alt)
print('Seu IMC corresponde a {:.1f}'.format(imc))

if imc <= 18.5:
    print('IMC abaixo de 18,5: Abaixo do Peso')
elif 18.5 <= imc <= 25:
    print('IMC entre 18,5 e 25: Peso Ideal')
elif  25 <= imc <= 30:
    print('IMC entre 25 até 30: Sobrepeso')
elif 30 <= imc <= 40:
    print('IMC entre 30 até 40: Obesidade')
else:
    print('IMC acima de 40: Obesidade Mórbida')