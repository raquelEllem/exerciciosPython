r1 = float(input('Reta um: '))
r2 = float(input('Reta dois: '))
r3 = float(input('Reta três: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Os segmentos não podem formar um triângulo.')