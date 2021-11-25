nome = str(input('Qual seu nome ? '))

""" Estrutura condicional aninhada """
if nome == 'Gustavo':
    print('Que nome bonito !')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(' Seu nome é popular no Brasil !')
elif nome in "Ana Claudia Jéssica Juliana Amanda":
    print('Belo nome feminino !')
else:
    print('Seu nome é normal !')
""" Fim das Estruturas """
print('Tenha um bom dia, {}!'.format(nome))
