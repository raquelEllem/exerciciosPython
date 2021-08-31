from random import randint
from time import sleep
lista = list()
def sorteia():
    print('Sorteando 5 valores...', end=' ')
    sleep(0.3)
    for i in range(0, 5):
        sleep(0.2)
        num = randint(0, 10)
        lista.append(num)
        print(f'{num}', end=' ')
    print('PRONTO!')

def somaPar(lst):
    soma = pos = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lst}, temos {soma}')

sorteia()
somaPar(lista)