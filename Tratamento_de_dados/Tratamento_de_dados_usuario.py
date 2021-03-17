import os

def tratar_login(usuario, senha):
    try:
        DIRETORIO_SENHA = f'Usuários\\{usuario}\\senha.txt'

        with open(DIRETORIO_SENHA) as senha_txt:
            senha_real = senha_txt.readline()

        if senha == senha_real:
            return True

        else:
            return False
    
    except FileNotFoundError:
        return False

def tratar_nome_real(usuario):
    DIRETORIO_NOME_REAL = f'Usuários\\{usuario}\\nome.txt'

    with open(DIRETORIO_NOME_REAL) as nome_txt:
        nome_real = nome_txt.readline()

    return nome_real

def tratar_saldo(usuario):
    DIRETORIO_SALDO = f'Usuários\\{usuario}\\saldo.txt'

    with open(DIRETORIO_SALDO) as saldo_txt:
        saldo = saldo_txt.readline()
        return saldo

def tratar_numero_float(valor):
    ponto = 0

    if len(valor) == 0:
        return False 
    
    for x in valor:
        if x.isnumeric() == True:
            pass
        
        else:
            if x == ".":
                if ponto == 0:
                    ponto += 1
                    pass

                else:
                    return False
            
            else:
                return False

    return True

def tratar_deposito(usuario, valor_deposito):
    DIRETORIO_SALDO = f'Usuários\\{usuario}\\saldo.txt'
    DIRETORIO_EXTRATO = f'Usuários\\{usuario}\\extrato.txt'

    with open(DIRETORIO_SALDO) as saldo_txt:
        saldo = saldo_txt.readline()
        saldo_final = float(saldo) + float(valor_deposito)

    #Atualizo o saldo do usuário
    arquivo = open(DIRETORIO_SALDO, 'w')
    arquivo.write(str(f'{saldo_final:.2f}'))
    arquivo.close()

    #Armezeno o valor do depósito para criar um histórico que será usado no extrato
    arquivo = open(DIRETORIO_EXTRATO, 'a')
    arquivo.write(str(f'Depósito feito no valor de R${valor_deposito:.2f}\n'))
    arquivo.close()

def tratar_saque(usuario, valor_saque):
    DIRETORIO_SALDO = f'Usuários\\{usuario}\\saldo.txt'
    valor_saque = float(valor_saque)
    
    with open(DIRETORIO_SALDO) as saldo_txt:
        saldo = saldo_txt.readline()
        saldo = float(saldo)
    
    if saldo == 0:
        return False
    
    elif saldo >= valor_saque:
        valor_final = saldo - valor_saque

        #Atualizo o saldo do usuário
        arquivo = open(DIRETORIO_SALDO, 'w')
        arquivo.write(str(f'{valor_final:.2f}'))
        arquivo.close()

        #Armezeno o valor do saque para criar um histórico que será usado no extrato
        DIRETORIO_EXTRATO = f'Usuários\\{usuario}\\extrato.txt'

        arquivo = open(DIRETORIO_EXTRATO, 'a')
        arquivo.write(str(f'Saque feito no valor de R${valor_saque:.2f}\n'))
        arquivo.close()

        return True
    
    else:
        return False

def tratar_tranferencia(valor_transferencia, usuario_transferencia, usuario_nome, usuario_cpf, usuario):
    valor_transferencia = float(valor_transferencia)
    usuario_nome = usuario_nome.title()
    
    try:
        DIRETORIO_NOME = f'Usuários\\{usuario_transferencia}\\nome.txt'
        DIRETORIO_CPF = f'Usuários\\{usuario_transferencia}\\cpf.txt'

        with open(DIRETORIO_NOME) as nome_txt:
            nome_real = nome_txt.readline()

        with open(DIRETORIO_CPF) as cpf_txt:
            cpf_real = cpf_txt.readline()

        if usuario_nome.title() == nome_real and usuario_cpf == cpf_real:
            DIRETORIO_TRANSFERE_SALDO = f'Usuários\\{usuario}\\saldo.txt' #O que está transferindo
            DIRETORIO_RECEBEBE_SALDO = f'Usuários\\{usuario_transferencia}\\saldo.txt' #O que está recebendo

            with open(DIRETORIO_TRANSFERE_SALDO) as saldo_txt:
                valor_saldo = saldo_txt.readline()
                valor_saldo = float(valor_saldo)

            if valor_saldo >= valor_transferencia:
                
                #Diminuo o valor do saldo de quem tranferiu
                valor_final_tranferencia = valor_saldo - valor_transferencia
                
                arquivo = open(DIRETORIO_TRANSFERE_SALDO, 'w')
                arquivo.write((str(f'{valor_final_tranferencia:.2f}')))
                arquivo.close()

                #Aumento o valor do saldo de quem recebeu a transferencia
                with open(DIRETORIO_RECEBEBE_SALDO) as saldo_txt:
                    valor_saldo = saldo_txt.readline()
                    valor_saldo = float(valor_saldo)

                valor_final_recebe = valor_saldo + valor_transferencia 

                arquivo = open(DIRETORIO_RECEBEBE_SALDO, 'w')
                arquivo.write(str(f'{valor_final_recebe:.2f}'))
                arquivo.close()

                #Armezeno o valor da transferência para criar um histórico que será usado no extrato de quem transferiu
                DIRETORIO_EXTRATO = f'Usuários\\{usuario}\\extrato.txt'

                arquivo = open(DIRETORIO_EXTRATO, 'a')
                arquivo.write(str(f'Transferência para {usuario_nome} no valor de R${valor_transferencia:.2f}\n'))
                arquivo.close()

                #Armezeno o valor da transferência para criar um histórico que será usado no extrato de quem recebeu
                DIRETORIO_EXTRATO = f'Usuários\\{usuario_transferencia}\\extrato.txt'

                arquivo = open(DIRETORIO_EXTRATO, 'a')
                arquivo.write(str(f'Transferência recebida de {usuario} no valor de R${valor_transferencia:.2f}\n'))
                arquivo.close()

                return True

            else:
                return False

        else:
            return False
    
    except FileNotFoundError:
        return False

def tratar_extrato(usuario):
    DIRETORIO_EXTRATO = f'Usuários\\{usuario}\\extrato.txt'
    
    with open(DIRETORIO_EXTRATO) as extrato_txt:
        for line in extrato_txt:
            print(line, end = '')

def tratar_senha(usuario, senha):
    DIRETORIO_SENHA = f'Usuários\\{usuario}\\senha.txt'

    with open(DIRETORIO_SENHA) as senha_txt:
        senha_real = senha_txt.readline()

    if senha == senha_real:
        return True

    else:
        return False

def tratar_novo_usuario(usuario, novo_usuario):
    DIRETORIO_USUARIO = f'Usuários\\{usuario}'
    DIRETORIO_NOVO_USUARIO = f'Usuários\\{novo_usuario}'
    
    if len(usuario) <= 1 or ' ' in usuario:
        return False

    else:
        os.rename(DIRETORIO_USUARIO, DIRETORIO_NOVO_USUARIO)
        return True

def tratar_nova_senha(usuario, nova_senha):
    if len(nova_senha) <= 1 or ' ' in nova_senha:
        return False
    
    else:
        arquivo_txt_senha = f'Usuários\\{usuario}\\senha.txt'

        arquivo = open(arquivo_txt_senha, 'w')
        arquivo.write(nova_senha)
        arquivo.close()
        
        return True

def encerrar_conta(usuario):
    import shutil 
    DIRETORIO_USUARIO = f'Usuários\\{usuario}'

    shutil.rmtree(DIRETORIO_USUARIO)