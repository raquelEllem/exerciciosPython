frase = str(input('Digite uma frase: ')).lower().strip()
print('Quantidade de "a/A": {}'.format(frase.count('a')))
print('Posição em que "a/A" aparece a primera vez: {}'.format(frase.find('a') + 1))
print('Posição em que "a/A" aparece a última vez: {}'.format(frase.rfind('a') + 1))
