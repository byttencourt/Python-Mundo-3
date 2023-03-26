from time import sleep
def titulo(text):
    print('--', '–' * len(text), '--')
    print(f'   {text} '.title())
    print('--', '–' * len(text), '--')


def contador(i, f, p):
    if i > f and p > 0:
        print(f'1 Contagem de {i} até {f} pulando de {-p} em {-p}: ', end='')
        for r in range(i, f-1, -p):
            print(f' {r}. ', end='')
            sleep(0.5)
        print()
    if i > f and p < 0:
        print(f'2 Contagem de {i} até {f} de {p} em {p}.')
        for r in range(i, f, p):
            print(f' {r}. ', end='')
            sleep(0.5)
        print()
    if i > f and p == 0:
        print(f'3 Contagem de {i} até {f} com passo negativo -1.')
        for r in range(i, f, -1):
            print(f' {r}. ', end='')
            sleep(0.5)
        print()
    else:
        print(f'4 Contagem de {i} até {f} pulando de {p} em {p}: ', end='')
        for a in range(i, f+1, p):
            print(f' {a}. ', end=' ')
            sleep(0.3)
        print()
        print('-' * 15)
        print()

print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)




