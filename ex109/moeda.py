def aumentar(num=0, taxa=0, form=True):
    res = num + (num * taxa/100)
    return moeda(res) if form is True else res


def diminuir(num=0, taxa=0, form=True):
    res: float = num - (num * taxa/100)
    return moeda(res) if form else res


def dobro(num=0, form=True):
    res = num * 2
    if form:
        return moeda(res)
    else:
        return res


def metade(num=0, form=True):
    res = num / 2
    return res if form is not True else moeda(res)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
