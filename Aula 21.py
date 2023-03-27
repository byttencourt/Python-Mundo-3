def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno by nino
    """
    print('Iniciando contagem: ', end='')
    for c in range(i, f+1, p):
        print(f'{c} ', end='')
    print('Fim!')



help(contador)

def somar(a=0, b=0, c=0):
    soma = a + b + c
    print(soma)

somar(3, 2, 5)
somar(3, 2)
somar(3)
somar()

