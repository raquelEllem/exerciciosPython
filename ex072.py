numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove',
           'vinte')
while True:
    opcao = int(input('Digite um número entre 0 e 20: '))
    if 0 <= opcao <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {numeros[opcao]}')