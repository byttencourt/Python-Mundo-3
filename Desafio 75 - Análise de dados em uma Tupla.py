lista = int(input('Digite 1o primeiro valor: ')), \
        int(input('Digite 2o primeiro valor: ')), \
        int(input('Digite 3o primeiro valor: ')), \
        int(input('Digite 4o primeiro valor: '))
print(f'Você digitou {lista}')
print(f'O numero nove apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O número 3 foi digitado pela vez na posição {1 + lista.index(3)}.')
else:
    print('O numero 3 nao foi digitado em nenhuma posição.')
print('O números pares são: ', end=' ')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
print('\n-> Fim!')


