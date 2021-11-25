'''Sistema de cores'''''
''' \033[0:30:41m
    \033[4:33:44m
    \033[1:35:43m
    \033[30:42m
    \033[m
    \033[7:30m'''
print('\033[0:33:44mOlá Mundo !\033[m')

a = 3
b = 5
print('Os valores são \33[32m{}\033[m e \033[31m{}\033[m !'.format(a, b))

nome = 'Carlos'
print('Olá, Muito prazer em te conhecer,{}{}{}'.format('\033[4;35m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pb': '\033[7;30m'}
print('Olá ,{}{}{} prazer em te conhecer !'.format(cores['pb'], nome, cores['limpa']))
