import os

def tratar_opcao(opcao):
    OPCOES_DISPONIVEIS = ('1', '2', '3')

    if opcao in OPCOES_DISPONIVEIS:
        return True

    else:
        return False

def tratar_nome(nome):
    nome_separado = nome.split(' ')

    nome_valido = False

    if len(nome_separado) >= 2:
        for nome in nome_separado:
            if nome.isalpha() == True:
                nome_valido = True

            else:
                return False

    if nome_valido == True:
        return True

    else:
        return False

def tratar_data(data):
    data_numeros = data.split('/')
    
    ULTIMO_DIA = 31
    ULTIMO_MES = 12
    ANO_MINIMO = 1920
    ANO_MAXIMO = 2002

    for numero in data_numeros:
        if numero.isnumeric() == False:
            return False

    iterador = 0
    for item in data_numeros:
        if iterador == 0:
            dia = int(item)
            iterador += 1
        
        elif iterador == 1:
            mes = int(item)
            iterador += 1

        elif iterador == 2:
            ano = int(item)
            iterador += 1

    if dia < 1 or dia > ULTIMO_DIA:
        return False
    
    elif mes < 1 or mes > ULTIMO_MES:
        return False

    elif ano < ANO_MINIMO or ano > ANO_MAXIMO:
        return False

    else:
        return True

def tratar_cpf(cpf):
    if cpf.isnumeric() == False or len(cpf) != 11:
        return False
    
    else:
        return True

def criar_usuario(nome, data, cpf, usuario):
    diretorio_usuario = f'Usuários\\{usuario}'
    
    arquivo_txt_nome = f'Usuários\\{usuario}\\nome.txt'
    arquivo_txt_data = f'Usuários\\{usuario}\\data.txt'
    arquivo_txt_cpf = f'Usuários\\{usuario}\\cpf.txt'

    try:
        os.mkdir(diretorio_usuario)

        arquivo = open(arquivo_txt_nome, 'w')
        arquivo.write(nome.title())
        arquivo.close()

        arquivo = open(arquivo_txt_data, 'w')
        arquivo.write(data)
        arquivo.close()

        arquivo = open(arquivo_txt_cpf, 'w')
        arquivo.write(cpf)
        arquivo.close()

        return True
    
    except OSError:
        return False 

def tratar_usuario(nome, data, cpf, usuario):
    nome_pasta_usuarios = 'Usuários'
    
    if len(usuario) <= 1 or ' ' in usuario:
        return False

    try:
        os.mkdir(nome_pasta_usuarios)
        criar_usuario(nome, data, cpf, usuario)
        return True

    except FileExistsError:
        try:
            return_criar_usuario = criar_usuario(nome, data, cpf, usuario)
            
            if return_criar_usuario == True:
                return True
            
            else: 
                return False

        except FileExistsError:
            return False

def tratar_senha(senha, usuario):
    if len(senha) <= 1 or ' ' in senha:
        return False
    
    else:
        arquivo_txt_senha = f'Usuários\\{usuario}\\senha.txt'

        arquivo = open(arquivo_txt_senha, 'w')
        arquivo.write(senha)
        arquivo.close()
        
        return True

def tratar_saldo_inical(usuario):
    DIRETORIO_SALDO = f'Usuários\\{usuario}\\saldo.txt'
    SALDO_INICIAL = '0'

    arquivo = open(DIRETORIO_SALDO, 'w')
    arquivo.write(SALDO_INICIAL)
    arquivo.close

def tratar_extrato_incial(usuario):
    DIRETORIO_EXTRATO = f'Usuários\\{usuario}\\extrato.txt'
    EXTRATO_INICIAL = 'Histórico de transações:\n'

    arquivo = open(DIRETORIO_EXTRATO, 'w')
    arquivo.write(EXTRATO_INICIAL)
    arquivo.close()