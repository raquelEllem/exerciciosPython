velocidade = float(input('Digite a velocidade: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = velocidade - 80
    print('O valor a ser pago é de R${}'.format(multa * 7))
print('--FIM--')
