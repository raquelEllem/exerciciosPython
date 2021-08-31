maior = 0
menor = 100000000
for c in range(1, 6):
    peso = float(input('Peso {}ª pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi de {:.1f}Kg'.format(maior))
print('O menor peso lido foi de {:.1f}Kg'.format(menor))