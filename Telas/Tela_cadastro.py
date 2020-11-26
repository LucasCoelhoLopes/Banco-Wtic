import os

def cadastro_nome():
    os.system('cls')
    print('Banco Wtic - Tela de cadastro\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    nome = input('Insira seu nome completo: ')

    if nome.title() == 'Voltar':
        from Telas import Tela_inicial
        Tela_inicial.tela_inicial()

    from Tratamento_de_dados import Tratamento_de_dados_cadastro
    return_tratar_nome = Tratamento_de_dados_cadastro.tratar_nome(nome)

    if return_tratar_nome == False:
        print('Nome inválido.')
        os.system('pause')
        cadastro_nome()

    else:
        cadastro_data(nome)

def cadastro_data(nome):
    os.system('cls')
    print('Banco Wtic - Tela de cadastro\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    data = input('Insira sua data de nascimento (Mínimo 18 anos de idade): ')

    if data.title() == 'Voltar':
        from Telas import Tela_inicial
        Tela_inicial.tela_inicial()

    from Tratamento_de_dados import Tratamento_de_dados_cadastro
    return_tratar_data = Tratamento_de_dados_cadastro.tratar_data(data)
    
    if return_tratar_data == False:
        print('Data inválida.')
        os.system('pause')
        cadastro_data(nome)

    else:
        cadastro_cpf(nome, data)

def cadastro_cpf(nome, data):
    os.system('cls')
    print('Banco Wtic - Tela de cadastro\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    cpf = input('Insira seu CPF (Contém 11 digitos): ')

    if cpf.title() == 'Voltar':
        from Telas import Tela_inicial
        Tela_inicial.tela_inicial()

    from Tratamento_de_dados import Tratamento_de_dados_cadastro
    return_tratar_cpf = Tratamento_de_dados_cadastro.tratar_cpf(cpf)
    
    if return_tratar_cpf == False:
        print('CPF inválido.')
        os.system('pause')
        cadastro_cpf(nome, data)
    
    else:
        cadastro_usuario(nome, data, cpf)

def cadastro_usuario(nome, data, cpf):
    os.system('cls')
    print('Banco Wtic - Tela de cadastro\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    usuario = input('Crie um nome de usuário (Não pode conter espaçamento): ')
    
    if usuario.title() == 'Voltar':
        from Telas import Tela_inicial
        Tela_inicial.tela_inicial()

    from Tratamento_de_dados import Tratamento_de_dados_cadastro
    return_tratar_usuario = Tratamento_de_dados_cadastro.tratar_usuario(nome, data, cpf, usuario)
    
    if return_tratar_usuario == False:
        print('Esse usuário é inválido ou já existe.')
        os.system('Pause')
        cadastro_usuario(nome, data, cpf)

    else:
        cadastro_senha(usuario)

def cadastro_senha(usuario):
    os.system('cls')
    print('Banco Wtic - Tela de cadastro\n')
    print('Digite "Voltar" para retornar ao menu anterior.\n')
    senha = input('Crie uma senha para sua conta: ')

    if senha.title() == 'Voltar':
        from Telas import Tela_inicial
        Tela_inicial.tela_inicial()
    
    from Tratamento_de_dados import Tratamento_de_dados_cadastro
    return_tratar_senha = Tratamento_de_dados_cadastro.tratar_senha(senha, usuario)
    
    if return_tratar_senha == False:
        print('Não utilize espaçamento em sua senha.')
        os.system('pause')
        cadastro_senha(usuario)
    
    else:
        print('Conta registrada com sucesso!')
        os.system('pause')
        
        Tratamento_de_dados_cadastro.tratar_saldo_inical(usuario)
        Tratamento_de_dados_cadastro.tratar_extrato_incial(usuario)

        from Telas import Tela_inicial
        Tela_inicial.tela_inicial()