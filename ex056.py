mediaIdade = 0
maiorIdadeH = 0
nomeMaiorIdadeH = ''
menor20 = 0
for c in range(1, 5):
    print('------ {}ª ------'.format(c))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper())
    mediaIdade += idade
    if sexo == 'M':
        if idade > maiorIdadeH:
            maiorIdadeH = idade
            nomeMaiorIdadeH = nome
    else:
        if idade < 20:
            menor20 += 1
mediaIdade = mediaIdade / 4
print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeH, nomeMaiorIdadeH))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menor20))