import cgitb
import sqlite3

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
        nome = input('Nome: ')
        email = input('Email: ')
        telefone = input('Telefone: ')
        idade = int(input('Idade: '))
        inserir_pessoa(nome, email, telefone, idade)
        print('Pessoa inserida com sucesso!')

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
        email = input('Novo email: ')
        telefone = input('Novo telefone: ')
        idade = int(input('Nova idade: '))
        atualizar_pessoa(id, nome, email, telefone, idade)
        print('Pessoa atualizada com sucesso!')
    elif opcao == 4:
        id = int(input('ID da pessoa a ser excluída: '))
        excluir_pessoa(id)
        print('Pessoa excluída com sucesso!')
    elif opcao == 5:
        
        tbpessoas = exibir_pessoas()
        for pessoa in tbpessoas:
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
