ficha = []
composta = []
opcao = opc = ''
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar? [S/N] '))
    if opcao in 'Nn':
        break
print('--' * 10)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('--' * 10)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('--' * 10)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')