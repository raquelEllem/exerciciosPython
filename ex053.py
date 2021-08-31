frase = str(input('Digite uma frase: ').strip().upper())
palavras = frase.split()
juncao = ''.join(palavras)
'''inverso = ''
for letra in range(len(juncao) - 1, -1, -1):
    inverso += juncao[letra]'''
inverso = juncao[::-1]
if inverso == juncao:
    print('É palíndromo, {} e {}'.format(juncao, inverso))
else:
    print('NÃO é palíndromo, {} e {}'. format(juncao, inverso))

