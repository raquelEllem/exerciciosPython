def voto(anoNas):
    from datetime import datetime
    atual = datetime.now().year
    global idade
    idade = atual - anoNas
    if 16 <= idade < 18 or idade >= 65:
        return 'OPCIONAL.'
    elif 65 >= idade >= 18:
        return 'OBRIGATÓRIO.'
    else:
        return 'NEGADO.'


anoNas = int(input('Em que ano você nasceu? '))
opc = voto(anoNas)
print(f'Com {idade} anos: VOTO {opc}')