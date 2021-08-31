from math import hypot
catOposto = float(input('Cateto oposto: '))
catAdjacente = float(input('Cateto adjacente: '))
hipotenusa = hypot(catOposto, catAdjacente)
print('Hipotenusa = {:.2f}'.format(hipotenusa))