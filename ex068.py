from random import randint
print('~~' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitorias = 0
while True:
    computador = randint(0, 11)
    print('-------' * 20)
    jogador = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ').strip().upper())
    soma = computador + jogador
    jogada = soma % 2
    if escolha == 'P':
        if jogada == 0:
            print(f'Você jogou {jogador} e o computador {computador}.')
            print(f'Total de {soma} DEU PAR')
            print('Você VENCEU!')
            vitorias += 1
        elif jogada == 1:
            print(f'Você jogou {jogador} e o computador {computador}.')
            print(f'Total de {soma} DEU ÍMPAR')
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if jogada == 0:
            print(f'Você jogou {jogador} e o computador {computador}.')
            print(f'Total de {soma} DEU PAR')
            print('Você PERDEU!')
            break
        elif jogada == 1:
            print(f'Você jogou {jogador} e o computador {computador}.')
            print(f'Total de {soma} DEU ÍMPAR')
            print('Você VENCEU!')
            vitorias += 1
print(f'GAME OVER!! Você venceu {vitorias} vezes.')
