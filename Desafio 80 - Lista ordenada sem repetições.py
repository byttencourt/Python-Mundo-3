lista = []
for c in range(0, 5):
    n = int(input('Digite um número; '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionei {n} ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionei o valor {n} a posição {pos}.')
                break
            pos += 1
print(lista)




















