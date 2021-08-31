lista = []
listaPar = []
listaImpar = []
opcao = ''
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break

for n in range (0, len(lista)):
     if lista[n] % 2 == 0:
         listaPar.append(lista[n])
     else:
         listaImpar.append(lista[n])

print(f'A lista completa é {lista}')
print(f'A lista de pares é {listaPar}')
print(f'A lista de ímpares é {listaImpar}')

