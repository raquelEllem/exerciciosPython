principal = [[], []]
for n in range(0, 7):
    valor = int(input(f'Digite o {n+1}º valor: '))
    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)

principal[0].sort()
principal[1].sort()
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores ímpares digitados foram: {principal[1]}')

