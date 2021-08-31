def fatorial(num, show=False):
    # help da função
    """
    --> Cálcula o fatorial de um número
    :param num: o número a ser calculado
    :param show: (opcional) mostra ou não a conta
    :return: o valor do fatorial de um número
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(3, True))
help(fatorial)
