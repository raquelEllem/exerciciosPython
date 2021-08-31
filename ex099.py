from time import sleep
def maior(* num):
    print('Analisando os valores passados...')
    sleep(0.5)
    maior = cont = 0
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi de {maior}')
    print('--' * 10)
    sleep(0.2)

maior(1, 2, 3, 4, 5, 6)
maior(11, 25, 32, 14, 25, 16)