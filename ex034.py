salario = float(input('Digite o salário: R$ '))
if salario > 1250:
    print('Salário com aumento de 10%: R${:.2f} '.format(salario*1.10))
else:
    print('Salário com aumento de 15%: R${:.2f} '.format(salario*1.15))