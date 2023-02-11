import cgitb
import sqlite3
import re

# Criar o banco de dados
conn = sqlite3.connect('pessoas1.db')
cursor = conn.cursor()

# Criar a tabela de pessoas
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        idade INTEGER NOT NULL
);
""")

# Função para inserir uma pessoa
def inserir_pessoa(nome, email, telefone, idade):
    cursor.execute(" INSERT INTO pessoas (nome, email, telefone, idade) VALUES (?,?,?,?)", (nome, email, telefone, idade))
    conn.commit()

# Função para buscar todas as pessoas
def buscar_pessoas():
    cursor.execute("""
    SELECT * FROM pessoas;
    """)
    return cursor.fetchall()
    

# Função para buscar uma pessoa pelo ID
def buscar_pessoa(id):
    cursor.execute("""
    SELECT * FROM pessoas WHERE id=?;
    """, (id,))
    return cursor.fetchone()

# Função para atualizar uma pessoa
def atualizar_pessoa(id, nome, email, telefone, idade):
    cursor.execute("""
    UPDATE pessoas
    SET nome=?, email=?, telefone=?, idade=?
    WHERE id=?;
    """, (nome, email, telefone, idade, id))
    conn.commit()

# Função para excluir uma pessoa
def excluir_pessoa(id):
    cursor.execute("""
    DELETE FROM pessoas WHERE id=?;
    """, (id,))
    conn.commit()

# Função para excluir uma pessoa
def exibir_pessoas():
    cursor.execute("SELECT * FROM pessoas")
    return cursor.fetchall()

# Função que retorna se email válido
def validar_email(email):
    parametro = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return parametro.match(email)

# Função que retorna se string tem apenas caracteres válidos
def validar_texto(texto):
    parametro = r'^[a-zA-Z\u00C0-\u00FF]+$'
    op = re.search(parametro, texto)
    return bool(op)

# Função que retorna se string tem apenas caracteres válidos
def validar_idade(id):
    if id >= 1 | id <= 120:
        return True
    else:
        return False

def guarda_lista():
    nome = input('Nome: ')
    while validar_texto(nome) == False: #Valida texto
        print("Caractere inválido")
        nome = input('Nome: ')
        if validar_texto(nome):
            break  

    email = input('Email: ')
    while validar_email(email) != True: #Valida email
        print("email inválido")
        email = input('Email: ')
        if validar_email(email):
            break        

    telefone = input('Telefone: ')

    idade = int(input('Idade: '))
    while validar_idade(idade) != True: #Valida idade
        print("Idade inválida")
        idade = input('Idade: ')
        if validar_idade(idade):
            break  
        
    inserir_pessoa(nome, email, telefone, idade)
    print('Pessoa inserida com sucesso!')

# Loop para a interface do usuário
while True:
    print('1 - Inserir pessoa')
    print('2 - Buscar pessoa')
    print('3 - Atualizar pessoa')
    print('4 - Excluir pessoa')
    print('5 - Exibir todas pessoas')
    print('0 - Sair')

    opcao = int(input('Opção: '))

    if opcao == 1:
        guarda_lista()

    elif opcao == 2:
        id = int(input('ID da pessoa a ser buscada: '))
        pessoa = buscar_pessoa(id)
        if pessoa:
                print('Nome:', pessoa[1])
                print('Email:', pessoa[2])
                print('Telefone:', pessoa[3])
                print('Idade:', pessoa[4])
        else:
                print('Pessoa não encontrada.')

    elif opcao == 3:
        id = int(input('ID da pessoa a ser atualizada: '))

        nome = input('Novo nome: ')
        while validar_texto(nome) == False: #Valida texto
            print("Caractere inválido")
            nome = input('Nome: ')
            if validar_texto(nome):
                break  

        email = input('Novo email: ')
        while validar_email(email) != True: #Valida email
            print("email inválido")
            email = input('Email: ')
            if validar_email(email):
                break 

        telefone = input('Novo telefone: ')

        idade = int(input('Nova idade: '))
        while validar_idade(idade) != True: #Valida idade
            print("Idade inválida")
            idade = input('Idade: ')
            if validar_idade(idade):
                break  
    
        atualizar_pessoa(id, nome, email, telefone, idade)
        print('Pessoa atualizada com sucesso!')

    elif opcao == 4:
        id = int(input('ID da pessoa a ser excluída: '))
        excluir_pessoa(id)
        print('Pessoa excluída com sucesso!')

    elif opcao == 5:
        
        pessoas = exibir_pessoas()
        for pessoa in pessoas:
            print('\n------------------------------------')
            print('ID:', pessoa[0])
            print('Nome:', pessoa[1])
            print('Email:', pessoa[2])
            print('Telefone:', pessoa[3])
            print('Idade:', pessoa[4])
            print('------------------------------------')

    elif opcao == 0:
        break

    else:
        print('Opção inválida.')

conn.close()
