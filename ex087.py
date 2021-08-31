matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = soma3 = maior2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
        if coluna == 2:
            soma3 += matriz[linha][2]
        if linha == 1:
            if maior2 < matriz[1][coluna]:
                maior2 = matriz[1][coluna]
print('-=-' * 10)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=-' * 10)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior2}')
