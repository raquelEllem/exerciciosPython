valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
mensalidade = valor / (anos * 12)
valMaxPres = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'. format(valor, anos, mensalidade))
if valMaxPres >= mensalidade:
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo NEGADO!')

