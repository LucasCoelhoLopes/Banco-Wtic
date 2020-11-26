import os

def login():
    os.system('cls')
    print('Banco Wtic\n')
    print('Digite "Voltar" para retornar ao menu anterior.')
    print('Digite abaixo seus dados corretamente para entrar em sua conta.\n')

    usuario = input('Informe seu nome de usuário: ')

    if usuario.title() == 'Voltar':
        from Telas import Tela_inicial
        Tela_inicial.tela_inicial()
    
    senha = input('Informe sua senha: ')
    
    from Tratamento_de_dados import Tratamento_de_dados_usuario
    return_tratar_login = Tratamento_de_dados_usuario.tratar_login(usuario, senha)

    if return_tratar_login == True:
        from Telas import Tela_usuario
        Tela_usuario.tela_usuario(usuario)

    else:
        print('Usuário e/ou senha inválidos!')
        os.system('Pause')
        login()