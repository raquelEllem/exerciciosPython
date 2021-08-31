nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Tirando {:.1f} e {:.1f} sua média foi de {:.1f}'.format(nota1, nota2, media))
    print('O aluno está REPROVADO.')
elif 6.9 > media > 5:
    print('Tirando {:.1f} e {:.1f} sua média foi de {:.1f}'.format(nota1, nota2, media))
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('Tirando {:.1f} e {:.1f} sua média foi de {:.1f}'.format(nota1, nota2, media))
    print('O aluno está APROVADO.')