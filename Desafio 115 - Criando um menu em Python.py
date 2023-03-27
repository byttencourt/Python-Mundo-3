
def sistemacadastro():
    from utilidadescev.dados import leiaint
    from time import sleep
    '''
    Sistema que cadastra pessoas e acessa banco de dados.
    :return:
    '''
    while True:
        print('–' * 40)
        print(f'{"MENU PRINCIPAL":^40}')
        print('–' * 40)
        print('\033[33m1 \033[34m- Ver pessoas Cadastradas\033[m')
        print('\033[33m2 \033[34m- Cadastrar novas pessoas\033[m')
        print('\033[33m3 \033[34m- Sair do sistema\033[m')
        print('–' * 40)
        n = leiaint('\033[33msua opção: \033[m')
        print('Aguarde...')
        sleep(0.5)
        if n == 1:
            print('\033[32mAcessando banco de dados do sistema de cadastro.\033[m')
            sleep(0.5)
        elif n == 2:
            print('\033[32mInicando sistema de cadastro.\033[m')
            sleep(0.5)
        else:
            print('\033[31mSaindo do Programa...Quit command executed.\033[m')
            sleep(0.5)
            break

sistemacadastro()