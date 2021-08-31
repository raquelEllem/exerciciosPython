lista = []
opcao = ''
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Quer continuar? [S/N] ').strip().upper())
    if opcao == 'N':
        break
lista.sort()
print(f'Você adicionou os valores: {lista}')