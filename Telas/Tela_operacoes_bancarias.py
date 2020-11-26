import os

def operacoes_Bancarias(usuario, nome_real):
    tela_nome = 'operacoes_Bancarias'

    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    print(f'Bem-vindo {nome_real}! Qual operação deseja realizar?')
    print('1 - Depósito    2 - Saque    3 - Transferência    4 - Extrato')
    opcao = input('Opcao: ')

    if opcao.title() == 'Voltar':
        from Telas import Tela_usuario
        Tela_usuario.tela_usuario(usuario)

    from Tratamento_de_dados import Fluxo_das_opcoes
    return_tratar_opcao = Fluxo_das_opcoes.tratar_opcao(tela_nome, opcao)

    if return_tratar_opcao == True:
        if opcao == '1':
            deposito(usuario, nome_real)

        if opcao == '2':
            saque(usuario, nome_real)

        if opcao == '3':
            transferencia(usuario, nome_real)

        else:
            extrato(usuario, nome_real)

    else:
        print('Opção inválida.')
        os.system('pause')
        operacoes_Bancarias(usuario, nome_real)

def deposito(usuario, nome_real):
    from Tratamento_de_dados import Tratamento_de_dados_usuario
    saldo = Tratamento_de_dados_usuario.tratar_saldo(usuario)

    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    print(f'Saldo atual: R${saldo}')

    valor_deposito = input('Digite o valor a ser depositado: ')

    if valor_deposito.title() == 'Voltar':
        operacoes_Bancarias(usuario, nome_real)

    return_deposito = Tratamento_de_dados_usuario.tratar_numero_float(valor_deposito)

    if return_deposito == True:
        valor_deposito = float(valor_deposito)
        
        Tratamento_de_dados_usuario.tratar_deposito(usuario, valor_deposito)
        
        print(f'\nValor de R${valor_deposito} depositado com sucesso!')
        os.system('Pause')
        operacoes_Bancarias(usuario, nome_real)

    else:
        print('Valor inválido.')
        os.system('Pause')
        deposito(usuario, nome_real)

def saque(usuario, nome_real):
    from Tratamento_de_dados import Tratamento_de_dados_usuario
    saldo = Tratamento_de_dados_usuario.tratar_saldo(usuario)
    
    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    print(f'Saldo atual: R${saldo}')

    valor_saque = input('Digite o valor a ser sacado: ')

    if valor_saque.title() == 'Voltar':
        operacoes_Bancarias(usuario, nome_real)

    return_tratar_numero_float = Tratamento_de_dados_usuario.tratar_numero_float(valor_saque)

    if return_tratar_numero_float == True:
        return_tratar_saque = Tratamento_de_dados_usuario.tratar_saque(usuario, valor_saque)

        if return_tratar_saque == True:
            print(f'Valor de R${valor_saque} sacado com sucesso!')
            os.system('Pause')
            operacoes_Bancarias(usuario, nome_real)

        else:
            print('Saldo insuficiente.')
            os.system('Pause')
            saque(usuario, nome_real)

    else:
        print('Valor inválido.')
        os.system('Pause')
        saque(usuario, nome_real)

def transferencia(usuario, nome_real):
    from Tratamento_de_dados import Tratamento_de_dados_usuario
    saldo = Tratamento_de_dados_usuario.tratar_saldo(usuario)
    
    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    print(f'Saldo atual: R${saldo}')

    valor_transferencia = input('\nDigite o valor da tranferência: ')

    if valor_transferencia.title() == 'Voltar':
        operacoes_Bancarias(usuario, nome_real)
    
    usuario_transferencia = input('Insira o nome de usuário da pessoa que deseja transferir: ')
    usuario_nome = input('Insira o nome completo da pessoa: ')
    usuario_cpf = input('Insira o CPF da pessoa: ')

    return_tratar_numero_float = Tratamento_de_dados_usuario.tratar_numero_float(valor_transferencia)

    if return_tratar_numero_float == True:
        return_tratar_transferencia = Tratamento_de_dados_usuario.tratar_tranferencia(valor_transferencia, usuario_transferencia, usuario_nome, usuario_cpf, usuario)

        if return_tratar_transferencia == True:
            print(f'Valor de R${valor_transferencia} transferido com sucesso!')
            os.system('Pause')
            operacoes_Bancarias(usuario, nome_real)
        
        else:
            print('Dados incorretos.')
            os.system('Pause')
            transferencia(usuario, nome_real)
    
    else:
        print('Valor inválido.')
        os.system('Pause')
        transferencia(usuario, nome_real)

def extrato(usuario, nome_real):
    from Tratamento_de_dados import Tratamento_de_dados_usuario
    saldo = Tratamento_de_dados_usuario.tratar_saldo(usuario)
    
    os.system('cls')
    print(f'Banco Wtic - Usuário atual: {usuario}\n')
    print(f'Nome: {nome_real}')
    print(f'Saldo atual: R${saldo}\n')
    Tratamento_de_dados_usuario.tratar_extrato(usuario)
    print('')

    os.system('Pause')
    operacoes_Bancarias(usuario, nome_real)