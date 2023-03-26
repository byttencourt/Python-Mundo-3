def cabeçalho(texto):
    print('–' * 30)
    print(f'{texto:^30}'.title())
    print('–' * 30)


def area(larg, comp):
    area = larg * comp
    print(f'A área de um Terreno de {larg}mts x {comp}mts é igual a {area:.2f}m2.')



#prog principal
cabeçalho('Controle de terrenos')
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)