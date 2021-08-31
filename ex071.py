print('==' * 20)
print('{:^30}'.format('BANCO AR'))
print('==' * 20)
valor = int(input('Qual valor você quer sacar? '))
total = valor
cedula = 50
totalCedulas = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedulas = 0
        if total == 0:
            break
print('==' * 20)
print('Volte sempre!')
