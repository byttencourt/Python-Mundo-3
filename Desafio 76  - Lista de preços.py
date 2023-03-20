lista = ('Lápis', 3.75,
         'Borracha', 2,
         'caderno', 15.90,
         'estojo', 25,
         'trasferidor', 4.20,
         'compasso', 9.99,
         'mochila', 120,
         'canetas', 22.30,
         'livro', 34.90)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇO'))
print('-'*50)
for c in range(0, len(lista), 2):
    print(f'{lista[c].title():.<40}R${lista[c+1]:>8.2f}')
print('=' * 50)
