lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = tcol = mvseglinha = 0

for l in range(3):
    for c in range(3):
        lista[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
        if lista[l][c] % 2 == 0:
            par += lista[l][c]

for l in range(3):
    tcol += lista[l][2]

for col in range(3):
    if mvseglinha == 0:
        mvseglinha = lista[1][col]
    elif mvseglinha < lista[1][col]:
        mvseglinha = lista[1][col]
print(lista)
print('-='*30)

for l in range(3):
    for c in range(3):
        print(f'[{lista[l][c]:^5}]', end='  ')
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares é {par}')
print(f'A soma dos valores da terceira coluna totaliza {tcol}')
print(f'O maior valor da segunda linha é {mvseglinha}')
