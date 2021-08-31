from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('Você nasceu em {}, tem {} anos em {}.'.format(ano, idade, date.today().year))
alistamento = 18 - idade
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(alistamento))
    print('Seu alistamento será em {}'.format(date.today().year + alistamento))
elif idade == 18:
    print('Você deve se alistar este ano!')
else:
    alistamento = alistamento * (-1)
    print('Você já deveria ter se alistado há {} anos.'.format(alistamento))
    print('Seu alistamento foi em {}'.format(date.today().year - alistamento))
