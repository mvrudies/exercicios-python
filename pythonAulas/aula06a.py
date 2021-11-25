n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
s = n1 + n2
print('A soma vale', s)

# print('A soma entre ', n1 ,'e', n2,'Equivale a',s) // ANTIGO
print('A soma entre {} e {} equivale a {}'.format(n1, n2, s))
