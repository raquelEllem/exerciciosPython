from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
rankig = list()
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=-' * 10)
#cria uma lista e coloca em ordem decrescente os valores --
#key=itemgetter(1) --> esse 1 é pq pega o índice randint, que são 1
# e não 0 (0 é jogador1, jogador2 ...
rankig = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('  == Ranking dos Jogadores ==')
for i, v in enumerate(rankig):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
