lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    perg = ' '
    while perg not in 'NS':
        perg = str(input('Quer continuar? [S/N]')).upper()
    if perg == 'N':
        break
print(f'Você digitou {lista}.')
print(f'Foram digitados {len(lista)} números.')
print(f'A lista em ordem decrescente é {sorted(lista,reverse=True)}')
if 5 in lista:
    print(f'O número 5 foi digitado na posição nº: {lista.index(5)+1}')
else:
    print('O número 5 nao foi digitado na lista.')
