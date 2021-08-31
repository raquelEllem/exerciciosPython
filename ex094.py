pessoa = dict()
cadastro = list()
opcao = ''
somaIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    somaIdade += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()[0]
        if opcao in 'NS':
            break
        print('ERRO! Responda apenas S ou N.')
    if opcao == 'N':
        break
print('--' * 20)
print(f' A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
mediaIdade = somaIdade / len(cadastro)
print(f' B) A média de idade é de {mediaIdade:.2f} anos.')
print(' C) As mulheres cadastradas foram ', end='')
for p in cadastro:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(' D) Pessoas das pessoas com idade acima média: ')
for p in cadastro:
    if p['idade'] > mediaIdade:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
