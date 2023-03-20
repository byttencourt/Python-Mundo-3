num = [2, 5, 9, 1]
print(num)
# num[2] = 3
num.append(7), num.append(8)
num.insert(3, 4), num.insert(5, 6)
print(num)
if 9 in num:
    num.remove(9)
else:
    print('Nao existe o numero 9 na lista ')

print(f'Essa lista tem {len(num)} elementos.')
print(num)
# print(f'Em ordem crescente fica {sorted(num)}.')
# print(f'Em ordem decrescente fica {sorted(num,reverse=True)}.')

print('=' * 30)

lista = []
lista.append(5)
lista.append(9)
lista.append(4)
for c, valor in enumerate(lista):
    print(f'{c}º posição = {valor}.')
print('cheguei no final da lista.')

print('=' * 30)
save = lista[:]
for cont in range(0, 5):
    lista.append(int(input('digite um novo valor: ')))
    print(lista)
    print(save)


