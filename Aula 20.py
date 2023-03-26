def cabecalho(texto):
    print('-'*30)
    print(f'{texto:^30}')
    print('-'*30)


def soma(a, b):
    soma = a + b
    print(f'A soma entre {a} e {b} é {soma}')


def contador(* num):
    print(num)


def dobra(lst):
   pos = 0
   for pos in range(len(lst)):
       lst[pos] *= 2
       pos += 1



valores = [6, 3, 9, 1, 0, 2]

dobra(valores)
print(valores)


cabecalho('fodase')
soma(1, 5)
contador(5, 1, 2, 10, 15)