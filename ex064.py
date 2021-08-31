num = 0
total = 0
soma = 0
while num != 999:
    soma += num
    total += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} número e a soma entre eles foi de {}'.format(total - 1, soma))