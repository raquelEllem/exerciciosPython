from random import shuffle
al1 = input('Aluno 1: ')
al2 = input('Aluno 2: ')
al3 = input('Aluno 3: ')
al4 = input('Aluno 4: ')
lista = [al1, al2, al3, al4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

