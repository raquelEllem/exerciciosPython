lista = []
for n in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))
print('=-=' * 10)
print(f'Você digitou os valores {lista}')
maior = lista[0]
menor = lista[0]
for n in lista:
    if maior < n:
        maior = n
    if menor > n:
        menor = n

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')