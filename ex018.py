import math
angulo = float(input('Digite o valor do ângulo: '))
cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('Dado o ângulo {} \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(angulo, sen, cos, tan))
