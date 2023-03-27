def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida.\033[m')
            return 0
        else:
            return n

def linha(tam=40):
    return '–' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} \033[34m- {item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[33mSua opção: \033[m')
    return opc
