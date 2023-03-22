lista = [[], []]
for c in range(7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-='*30)
print(f'Todos os valores são {lista}.')
print(f'Valores pares digitados foram: {sorted(lista[0])}')
print(f'Valores ímpares digitados foram: {sorted(lista[1])}')



