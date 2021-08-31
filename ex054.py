from datetime import date
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(menor))
