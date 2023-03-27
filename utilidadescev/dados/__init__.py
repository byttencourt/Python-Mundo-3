def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO!: \"{entrada}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)


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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!Digite um valor Real valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida.\033[m')
            return 0
        else:
            return n




