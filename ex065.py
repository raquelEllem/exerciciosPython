cont = soma = media = maior = menor = 0
res = 'S'
while res == 'S':
    num = int(input('Digite um número: '))
    res = str(input('Quer continuar? [S/N] ').strip().upper())
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
media = soma / cont
print('Você digitou {} números e a média foi de {:.2f}'.format(cont, media))
print('O maior valor foi de {} e o menor foi {}'.format(maior, menor))
