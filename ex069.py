maior18 = homensCad = mulheresMenos = 0

while True:
    print('CADASTRE UMA PESSOA')
    print('---' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ').strip().upper())[0]
    print('--' * 5)
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homensCad += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos += 1
    opcao = ' '
    while opcao not in 'NS':
        opcao = str(input('Quer continuar? [S/N] ').strip().upper())[0]
    if opcao == 'N':
        break
print('----- FIM DO PROGRAMA ------')
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homensCad} homens cadastrados')
print(f'E temos {mulheresMenos} mulheres com menos de 20 anos')