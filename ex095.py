jogador = dict()
gols = list()
geral = list()
opcao = ''
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for n in range(0, tot):
        gols.append(int(input(f'  Quantos gols na {n+1}ª partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    geral.append(jogador.copy())
    opcao = str(input('Quer continuar? [S/N] ')).upper()[0]
    if opcao == 'N':
        break

print(geral)
print('--' * 15)
print('cod' , end='')
for i in (jogador.keys()):
    print(f' {i:<15}', end='')
print()
for k, v in enumerate(geral):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 15)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para) '))
    if busca == 999:
        break
    if busca >= len(geral):
        print('Código inválido!')
    else:
        print(f'   LEVANTAMENDO DO JOGADOR {geral[busca]["nome"]}:')
        for i, v in enumerate(geral[busca]['gols']):
            print(f'  - No jogo {i + 1} fez {v} goals.')
    print('---' * 10)
print('<< VOLTE SEMPRE >>')