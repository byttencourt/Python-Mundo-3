def aumentar(n, p=5, moeda=False):
    '''
    Função que Aumenta porcentagem
    :param n: valor a base
    :param p: porcentagem ser acrescida (padrao 5%)
    :param moeda: (Opcional) se True ativa conversao para moeda
    :return: retorna o valor + porcentagem
    '''
    n += n * p / 100
    if moeda:
        return f'R$ {n:.2f}'
    else:
        return n


def diminuir(n, p=5, moeda=False):
    """
    Função que Subtrai em 1 o valor
    :param n: número base
    :param p: porcentagem ser decrescida (padrao 5%)
    :param moeda: (Opcional) se True ativa conversao para moeda
    :return: retorna o valor - porcentagem
    """
    n -= n * p / 100
    if moeda:
        return f'R$ {n:.2f}'
    else:
        return n


def dobro(n, moeda=False):
    """
    Função que dobra o valor
    :param n: Valor de entrada
    :param moeda: (Opcional) se True ativa conversao para moeda
    :return: retorna o dobro
    """
    if moeda:
        return f'R$ {n * 2:.2f}'
    else:
        return n * 2


def metade(n, moeda=False):
    """
    Função que divide o valor em metade
    :param n: valor de entrada
    :param moeda: (Opcional) se True ativa conversao para moeda
    :return: retorna a metade
    """
    if moeda:
        return f'R$ {n / 2:.2f}'
    else:
        return n / 2



def moeda(n):
    return f'R$ {n:.2f}'


def resumo(n, a, d):
    """
    Função que resume as Operações: Aumentar e diminuir porcentagem, metade, dobro
    :param n: valor de entrada
    :param a: Porcentagem de aumento
    :param d: Porcentagem de desconto
    :return: retorna os resultados
    """
    print('-' * 30)
    print('      RESUMO DO VALOR')
    print('-' * 30)
    print(f'Preço Analizado: \t{moeda(n):>10}')
    print(f'Dobro do Preço: \t{dobro(n, True):>10}')
    print(f'Metade do Preço: \t{metade(n, True):>10}')
    print(f'{a} % de aumento: \t{aumentar(n, a, True):>10}')
    print(f'{d} % de desconto: \t{diminuir(n, d, True):>10}')
    print('-' * 30)

