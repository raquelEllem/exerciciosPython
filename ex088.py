from random import randint
from time import sleep
#print('--' * 15)
#print('JOGO NA MEGA SENA')
#print('--' * 15)
# quant = int(input('Quantos jogos você quer que eu sorteie? '))
# print(f'---- SORTEANDO {quant} JOGOS ----')
# for n in range(1, quant+1):
#     print(f'Jogo {n}: {randint(1, 60)}, {randint(1, 60)}, {randint(1, 60)}, {randint(1, 60)}, {randint(1, 60)}')
#     sleep(1)
# print('---- BOA SORTE! ----')

lista = list()
jogos = list()
print('--' * 15)
print('JOGO NA MEGA SENA')
print('--' * 15)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('--' * 4, f'SORTEANDO {quant} JOGOS', '--' * 4)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('--' * 3, 'BOA SORTE!', '--' * 3)
