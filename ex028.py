from random import randint
from time import sleep
escolhaPC = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 à 5. Tente adivinhar...')
print('-=-' * 20)
numeroUser = int(input('Em que número eu pensei??  '))
print('Processando...')
sleep(2)
if escolhaPC == numeroUser:
        print('Parabéns você acertou!')
else:
    print('Tente novamente :/ Eu pensei em {}'.format(escolhaPC))
print('--FIM--')
