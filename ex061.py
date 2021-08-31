print('Gerador de PA')
print('===' * 7)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')