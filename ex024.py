cidade = str(input('Digite o nome da cidade: ')).strip()
dividido = cidade.capitalize().split()
print('A cidade começa com a palavra "Santo": {}' .format('Santo' in dividido[0]))


