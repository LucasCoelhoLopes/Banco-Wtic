import os

def tela_inicial():
    tela_nome = 'tela_inical'

    os.system('cls')

    print('Seja Bem-vindo(a) ao Banco Wtic!\n')
    print('O que deseja fazer?')
    print('1 - Login    2 - Cadastro    3 - Sair\n')
    
    opcao = input('Informe a opção desejada: ')

    from Tratamento_de_dados import Fluxo_das_opcoes
    return_tratamento_opcao = Fluxo_das_opcoes.tratar_opcao(tela_nome, opcao)

    if return_tratamento_opcao == True:
        if opcao == '1':
            from Telas import Tela_login
            Tela_login.login()

        if opcao == '2':
            from Telas import Tela_cadastro
            Tela_cadastro.cadastro_nome()
        
        else:
            Fluxo_das_opcoes.fechar_programa()

    else:
        print('Opção inválida.')
        os.system('pause')
        tela_inicial()
