num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\33[34m', end=' ')
        cont += 1
    else:
        print('\33[m', end=' ')
    print('{} '.format(c), end=' ')
if cont == 2:
    print('\n{} É um número primo!'.format(num))
else:
    print('\n{} NÃO é um número primo'.format(num))
