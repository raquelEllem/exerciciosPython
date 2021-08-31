r1 = float(input('Reta um: '))
r2 = float(input('Reta dois: '))
r3 = float(input('Reta três: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo')
else:
    print('Os seguimentos acima NÃO podem formar um triângulo')