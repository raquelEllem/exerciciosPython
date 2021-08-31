print('========== LOJAS S2 ==========')
preco = float(input('Digite o preço da compras: R$ '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desconto = preco * 0.9
    print('Sua compra de R${} vai custar R${} no final.'.format(preco, desconto))
elif opcao == 2:
    desconto = preco * 0.95
    print('Sua compra de R${} vai custar R${} no final.'.format(preco, desconto))
elif opcao == 3:
    desconto = preco
    print('Sua compra de R${} vai custar R${} no final.'.format(preco, desconto))
elif opcao == 4:
    desconto = preco * 1.2
    print('Sua compra de R${} vai custar R${} no final.'.format(preco, desconto))
else:
    print('Opção não encontrada. Tente novamente!')