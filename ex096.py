def calc(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {area:.1f}m².')

print('Controle de Terrenos')
print('--' * 10)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
calc(larg, comp)
