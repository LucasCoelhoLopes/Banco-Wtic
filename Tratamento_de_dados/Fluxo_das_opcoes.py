def tratar_opcao(tela_nome, opcao):
    
    if tela_nome == 'tela_inical':
        OPCOES_DISPONIVEIS = ('1', '2', '3')

        if opcao in OPCOES_DISPONIVEIS:
            return True

        else:
            return False

    if tela_nome == 'tela_usuario' or tela_nome == 'configuracoes_usuario' or tela_nome ==  'informacoes_pessoais' or tela_nome == 'encerrar_conta':
        OPCOES_DISPONIVEIS = ('1', '2')

        if opcao in OPCOES_DISPONIVEIS:
            return True

        else:
            return False
    
    if tela_nome == 'operacoes_Bancarias':
        OPCOES_DISPONIVEIS = ('1', '2', '3', '4')

        if opcao in OPCOES_DISPONIVEIS:
            return True

        else:
            return False

def fechar_programa():
    print('Obrigado por usar o Banco Wtic!')
    from sys import exit
    exit(0)