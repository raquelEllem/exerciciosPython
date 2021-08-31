nome = input('Digite seu nome completo: ')
print('Maiúsculas: {}'.format(nome.upper()))
print('Minúsculas: {}'.format(nome.lower()))
tam = len(nome) - nome.count(' ')
print('Quantidade de letras, sem espaços: {}'.format(tam))
nome1 = nome.split()
print('Primeiro nome: {}'.format(len(nome1[0])))

