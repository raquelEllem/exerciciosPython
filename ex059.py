num1 = float(input('Primeiro valor: '))
num2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {:.1f} e {:.1f} é {:.1f}'.format(num1, num2, soma))
        print('=-=-=-=-' * 10)
    elif opcao == 2:
        mult = num1 * num2
        print('O produto entre {:.1f} e {:.1f} é {:.1f}'.format(num1, num2, mult))
        print('=-=-=-=-' * 10)
    elif opcao == 3:
        maior = num1
        if num2 > maior:
            maior = num2
        print('Entre {:.1f} e {:.1f} o maior é {:.1f}'.format(num1, num2, maior))
        print('=-=-=-=-' * 10)
    elif opcao == 4:
        num1 = float(input('Primeiro valor: '))
        num2 = float(input('Segundo valor: '))
        print('=-=-=-=-' * 10)
    else:
        print('Opção inválida!')
        print('=-=-=-=-' * 10)
print('Fim do programa!')

