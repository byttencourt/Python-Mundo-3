lista = []
for c in range(6):
    tamanho = len(lista)
    n = int(input('Digite um número: '))
    if tamanho > 0:
        for y in range(tamanho):
            if n <= lista[y]:
                lista.insert(y, n)
                break
    if c == 0:
        lista.append(n)
print(lista)
