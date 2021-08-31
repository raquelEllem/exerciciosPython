num1 = int(input('1º número: '))
num2 = int(input('2º número: '))
num3 = int(input('3º número: '))
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('Maior número digitado {}'.format(maior))

if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('Menor número digitado {}'.format(menor))