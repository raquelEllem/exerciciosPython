distancia = float(input('Distância da viagem, em km: '))
if distancia <= 200:
    print('Valor da passagem: R${}'.format(distancia * 0.5))
else:
    print('Valor da passagem: R${}'.format(distancia * 0.45))
