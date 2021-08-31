dicionario = dict()
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f'Média de {dicionario["nome"]}: '))
if dicionario['media'] >= 7:
    dicionario['situação'] = 'Aprovado'
elif 7 > dicionario['media'] >= 5:
    dicionario['situação'] = 'Recuperação'
else:
    dicionario['situação'] = 'Reprovado'
print('--' * 15)
for k, v in dicionario.items():
    print(f' - {k} é igual a {v}')