lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c}º valor: ')))
print(f'Você digitou os valores {lista}')
print(f'O maior número da lista é {max(lista)} nas posições', end=' ')
for c, dado in enumerate(lista):
    if dado == max(lista):
        print(f'{c}..', end=' ')
print()
print(f'O menor valor digitado é {min(lista)} nas posições', end=' ')
for c, dado in enumerate(lista):
    if dado == min(lista):
        print(f'{c}..', end=' ')

