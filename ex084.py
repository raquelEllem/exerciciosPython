lista = []
pessoas = []
opcao = ''
pesomai = pesomen = 0
nomes = []
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        pesomai = pesomen = lista[1]
    else:
        if lista[1] > pesomai:
            pesomai = lista[1]
        if lista[1] < pesomen:
            pesomen = lista[1]

    pessoas.append(lista[:])
    lista.clear()
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break
print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {pesomai}kg. Peso de  ', end='')
for p in pessoas:
    if p[1] == pesomai:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {pesomen}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesomen:
        print(f'{p[0]} ', end='')
