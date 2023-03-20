lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}º valor: ')))
print(f'Você digitou os valores {lista}')
menor = min(lista)
maior = max(lista)
print(f'O maior número da lista é {maior} nas posições', end=' ')
for c in lista:
    if c == maior:
        print(f'{c}..', end=' ')
print('')
print(f'O menor valor digitado é {menor} nas posições', end=' ')
for c in lista:
    if c == menor:
        print(f'{c}..', end=' ')

