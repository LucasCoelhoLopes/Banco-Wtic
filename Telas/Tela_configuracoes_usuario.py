import os

def configuracoes_usuario(usuario):
    tela_nome = 'configuracoes_usuario'

    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    print('1 - Alterar informações pessoais 2 - Encerrar conta')
    opcao = input('Opcao: ')

    if opcao.title() == 'Voltar':
        from Telas import Tela_usuario
        Tela_usuario.tela_usuario(usuario)

    from Tratamento_de_dados import Fluxo_das_opcoes
    return_tratar_opcao = Fluxo_das_opcoes.tratar_opcao(tela_nome, opcao)

    if return_tratar_opcao == True:
        if opcao == '1':
            informacoes_pessoais(usuario)

        else:
            encerrar_conta(usuario)
    
    else:
        print('Opção inválida.')
        os.system('pause')
        configuracoes_usuario(usuario)

def informacoes_pessoais(usuario):
    tela_nome = 'informacoes_pessoais'

    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    print('1 - Alterar usuário 2 - Alterar senha')
    opcao = input('Opção: ')

    if opcao.title() == 'Voltar':
        configuracoes_usuario(usuario)

    from Tratamento_de_dados import Fluxo_das_opcoes
    return_tratar_opcao = Fluxo_das_opcoes.tratar_opcao(tela_nome, opcao)

    if return_tratar_opcao == True:
        if opcao == '1':
            alterar_usuario(usuario)
        
        else:
            alterar_senha(usuario)
    
    else:
        print('Opção inválida.')
        os.system('pause')
        informacoes_pessoais(usuario)

def alterar_usuario(usuario):
    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    senha = input('Insira sua senha: ')

    if senha.title() == 'Voltar':
        informacoes_pessoais(usuario)

    from Tratamento_de_dados import Tratamento_de_dados_usuario
    return_tratar_senha = Tratamento_de_dados_usuario.tratar_senha(usuario, senha)

    if return_tratar_senha == True:
        novo_usuario = input('Crie um novo nome de usuário: ')

        return_tratar_novo_usuario = Tratamento_de_dados_usuario.tratar_novo_usuario(usuario, novo_usuario)

        if return_tratar_novo_usuario == True:
            print('Usuário atualizado com sucesso!')
            os.system('Pause')
            informacoes_pessoais(novo_usuario)
        
        else:
            print('Usuário inválido.')
            os.system('Pause')
            alterar_usuario(usuario)
    
    else:
        print('Senha incorreta.')
        os.system('Pause')
        alterar_usuario(usuario)

def alterar_senha(usuario):
    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    senha = input('Insira sua senha atual: ')

    if senha.title() == 'Voltar':
        informacoes_pessoais(usuario)

    from Tratamento_de_dados import Tratamento_de_dados_usuario
    return_tratar_senha = Tratamento_de_dados_usuario.tratar_senha(usuario, senha)

    if return_tratar_senha == True:
        nova_senha = input('Crie uma nova senha: ')

        return_tratar_nova_senha = Tratamento_de_dados_usuario.tratar_nova_senha(usuario, nova_senha)

        if return_tratar_nova_senha == True:
            print('Senha atualizada com sucesso!')
            os.system('Pause')
            informacoes_pessoais(usuario)
        
        else:
            print('Senha inválida.')
            os.system('Pause')
            alterar_senha(usuario)
    
    else:
        print('Senha incorreta.')
        os.system('Pause')
        alterar_senha(usuario)

def encerrar_conta(usuario):
    Tela_nome = 'encerrar_conta'

    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    senha = input('Insira sua senha: ')

    if senha.title() == 'Voltar':
        configuracoes_usuario(usuario)

    from Tratamento_de_dados import Tratamento_de_dados_usuario
    return_tratar_senha = Tratamento_de_dados_usuario.tratar_senha(usuario, senha)

    if return_tratar_senha == True:
        while True:
            os.system('cls')
            print(f'Banco Wtic - Usuário atual: {usuario}\n')
            print('Deseja realmente encerrar sua conta? Não será possível recuperalá novamente.')
            opcao = input('1 - Encerrar conta    2 - Voltar: ')

            from Tratamento_de_dados import Fluxo_das_opcoes
            return_tratar_opcao = Fluxo_das_opcoes.tratar_opcao(Tela_nome, opcao)

            if return_tratar_opcao == True:
                if opcao == '1':
                    Tratamento_de_dados_usuario.encerrar_conta(usuario)
                    
                    print('Conta encerrada com sucesso!')
                    os.system('Pause')
                    from Telas import Tela_inicial
                    Tela_inicial.tela_inicial()

                else:
                    configuracoes_usuario(usuario)
            
            else:
                print('Opção inválida')
                os.system('Pause')
                continue
    
    else:
        print('Senha incorreta.')
        os.system('Pause')
        encerrar_conta(usuario)