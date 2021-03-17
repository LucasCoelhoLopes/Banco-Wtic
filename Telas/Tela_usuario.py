import os

def tela_usuario(usuario):
    tela_nome = 'tela_usuario'

    from Tratamento_de_dados import Tratamento_de_dados_usuario
    nome_real = Tratamento_de_dados_usuario.tratar_nome_real(usuario)

    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    print(f'Bem-vindo(a) {nome_real}! O que deseja fazer?')
    print('1 - Operações Bancárias  2 - Configurações do usuário')
    
    opcao = input('Opção: ')

    if opcao.title() == 'Voltar':
        from Telas import Tela_login
        Tela_login.login()

    from Tratamento_de_dados import Fluxo_das_opcoes
    return_tratar_opcao = Fluxo_das_opcoes.tratar_opcao(tela_nome, opcao)

    if return_tratar_opcao == True:
        if opcao == '1':
            from Telas import Tela_operacoes_bancarias
            Tela_operacoes_bancarias.operacoes_Bancarias(usuario, nome_real)
        
        else:
            from Telas import Tela_configuracoes_usuario
            Tela_configuracoes_usuario.configuracoes_usuario(usuario)
    
    else:
        print('Opção inválida')
        os.system('Pause')
        tela_usuario(usuario)