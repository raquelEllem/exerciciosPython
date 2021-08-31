from random import randint
from time import sleep
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
tentativas = 1
computador = randint(0, 10)
jogador = int(input('Qual é seu palpite? '))
while jogador != computador:
    if jogador > computador:
        sleep(0.3)
        print('Menos... Tente mais uma vez.')
        jogador = int(input('Qual é seu palpite? '))
        tentativas += 1
    elif jogador < computador:
        sleep(0.3)
        print('Mais... Tente mais uma vez.')
        jogador = int(input('Qual é seu palpite? '))
        tentativas += 1
print('ACERTOU com {} tentativas. Parabéns!'.format(tentativas))