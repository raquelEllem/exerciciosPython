km = float(input('Quantos km rodados? '))
dias = int(input('Quantos dias alugado? '))
print('O valor a pagar é de R${:.2f}'.format((km * 0.15) + (dias * 60)))
