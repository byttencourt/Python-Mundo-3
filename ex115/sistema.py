from lib import menu
from time import sleep
from lib.arquivo import *
from lib import leiaint

arq = 'curso em video.txt'
if arquivoexiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado.')
    criararquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # listar arquivo
        lerarquivo(arq)
    elif resposta == 2:
        print('Opção 2')
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title().strip()
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('\033[31mSaindo do sistema..\033[m')
        break
    else:
        print('\033[31mResposta nao encontrada.. \033[m')
    sleep(1)