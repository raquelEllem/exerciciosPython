from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= 1
    if passo == 0:
        passo = 1
    print('-' * 15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' ')
            cont += passo
            sleep(0.5)
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)