tabela = ('Palmeiras', 'Bragantino', 'Atlético-MG',
          'Fortaleza', 'Atlético-PR', 'Bahia',
          'Fluminense', 'Flamengo', 'Santos',
          'Atlético-GO', 'Ceará', 'Corinthians',
          'Juventude', 'São Paulo', 'Internacional',
          'América-MG', 'Sport', 'Cuiabá',
          'Chapecoense', 'Grêmio')
print('**' * 25)
print(f'Lista com os times do Brasileirão: {tabela}')
print('**' * 25)
print(f'Os cinco primeiros são: {tabela[0:5]}')
print('**' * 25)
print(f'Os últimos quatro são: {tabela[-4:]}')
print('**' * 25)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('**' * 25)
print(f'O {tabela[7]} está na 8ª posição')
print('**' * 25)
print(f'O Chapecoense está na {tabela.index("Chapecoense")+1}ª posição')