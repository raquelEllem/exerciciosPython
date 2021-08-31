print('----' * 10)
print('LOJA')
print('----' * 10)
cont = total = maisMil = maisBarato = 0
nomeProduto = ''
while True:
    nome = str(input('Nome do produto: ').strip())
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if preco > 1000:
        maisMil += 1
    if cont == 1:
        nomeProduto = nome
        maisBarato = preco
    else:
        if preco < maisBarato:
            maisBarato = preco
            nomeProduto = nome
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ').strip().upper())[0]
    if opcao == 'N':
        break
print('------ Fim do Programa -------')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {maisMil} produtos que custam mais de R$1000.00 ')
print(f'O produto mais barato foi {nomeProduto} que custa R${maisBarato:.2f}')
