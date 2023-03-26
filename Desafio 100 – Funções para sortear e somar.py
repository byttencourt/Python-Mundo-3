from random import randint
from time import sleep
def sorteio(lista):
    print(f'Sorteando os 5 valores da lista: ', end='')
    for r in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f' {n} ', end='')
        sleep(0.3)
    print('Pronto')

def somapar(lista):
    soma = 0
    print(f'Somando os valores pares de: ', end='')
    for n in range(len(lista)):
        if lista[n] % 2 == 0:
            print(f' {lista[n]}', end=' ')
            soma += lista[n]
            sleep(0.3)
    print(f'. Temos {soma}.')
    print(' Fim')

numeros = list()
sorteio(numeros)
somapar(numeros)