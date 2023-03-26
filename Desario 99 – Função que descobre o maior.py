from time import sleep
def title(text):
    print(f'  {text}'.title())
    print('-', '-' * len(text), '-')


def maior(*lista): #recebe varios parametros
    title('Mega power lista')
    print('Analizando a lista... ')
    if len(lista) > 0:
        for n in range(len(lista)):
            print(lista[n], end=' ')
            sleep(0.3)
        print(f'Foram informados ao todo {len(lista)} números na lista.')
        print(f'O maior número da lista é {max(lista)}')
    else:
        print('Digite um número válido!')

print()


maior(2, 9, 4, 5, 7, 1)
maior(3, 7, 0)
maior(6)
maior()