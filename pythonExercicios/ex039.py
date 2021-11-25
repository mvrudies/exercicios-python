#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_atual = date.today().year
print(('*'* 2),'SISTEMA DE ALISTAMENTO ',('*' * 2))
print('CÓDIGOS DE REFERENCIA AO  SEXO DO USUÁRIO\n'
      '[1] MASCULINO\n'
      '[2] FEMININO')
sexo = int(input('Digite o código do seu sexo : '))
if sexo == 1:
    ano_nasc = int(input('Qual o ano de nascimento : '))
    idade = ano_atual - ano_nasc
    if ano_nasc < ano_atual:
        print('Quem nasceu em {} tem {} anos em {}'.format(ano_nasc, idade, ano_atual))
        if idade == 18:
             print('Você tem que se alistar IMEDIATAMENTE !')
        elif idade < 18:
             print('Ainda faltam {} anos para o seu alistamento militar '.format(18-idade))
             print('Seu alistamento será em {} !' .format(ano_nasc + 18))
        elif idade > 18:
             print('Você  deveria ter se alistado há {} anos '.format(idade-18))
             print('Seu alistamento foi em {}'.format(ano_nasc + 18))
    elif ano_nasc > ano_atual:
        print('Você ainda não nasceu !')
        print('Porém faltam {} anos para se alistar  no ano de {}'.format(18 - idade,ano_nasc + 18))
elif sexo == 2:
    print('Você é mulher e não participa do alistamento militar obrigatorio !')
else:
    print('Você digitou um código incorreto tente novamente !')