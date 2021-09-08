def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar este número')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número real válido.')
            continue
        else:
            return n


inte = leiaInt('Digite um Inteiro: ')
fl = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {inte} e o real foi {fl}')