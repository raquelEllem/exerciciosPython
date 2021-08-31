listagem = ('APRENDER', 'PROGRAMAR',
            'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for pos in listagem:
    print(f'\nNa palavra {pos} temos ', end=' ')
    for letra in pos:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
