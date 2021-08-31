n = str(input('Digite o nome: ')).strip()
nome = n.split()
print('Primeiro: {}'.format(nome[0]))
print('Último: {}'.format(nome[(len(nome)-1)]))


