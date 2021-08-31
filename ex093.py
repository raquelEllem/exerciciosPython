jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for n in range(0, tot):
    gols.append(int(input(f'  Quantos gols na {n+1}ª partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('--' * 15)
print(jogador)
print('--' * 15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('--' * 15)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} goals.')
print(f'Foi um total de {jogador["total"]} goals.')