def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mErro digite um número válido.\033[m')
        if ok:
            break
    return valor

#principal
n = leiaint('Digite um número: ')
print(f'voce acabou de digitar {n}')
