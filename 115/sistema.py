from interface import menu

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('\033[31mSaindo do sistema..\033[m')
        break
    else:
        print('\033[31mResposta nao encontrada.. \033[m')

