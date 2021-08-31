def notas(*n, sit=False):
    """
    -> Função para analisar notas e situaçãoes de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário, com várias informações sobre a situação da turma
    """
    dic = dict()
    dic['quantNotas'] = len(n)
    dic['maiorNota'] = max(n)
    dic['menorNota'] = min(n)
    dic['media'] = sum(n)/len(n)
    if dic['media'] <= 5:
        sit = 'Ruim'
    elif dic['media'] >= 7:
        sit = 'Boa'
    else:
        sit = 'Razoável'
    dic['situação'] = sit
    return dic


resp = notas(9.5, 5.5, 10, sit=True)
print(resp)
help(notas)