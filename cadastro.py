#importando SQLite3
import sqlite3

#criando conexao
try:
    con_ban_dados = sqlite3.connect('cadastro.db')
    print('Conexão com banco de dados realizado com sucesso !')
except sqlite3.Error as e:
    print('Erro ao conectar com banco de dados:', e)

#criando tabela de cursos
try:
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        cur.execute(
            """ CREATE TABLE IF NOT EXISTS cursos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            duracao TEXT,
            preco REAL
            ) """
        )
        print('Tabela cursos criado com sucesso !')
except sqlite3.Error as e:
    print('Erro ao criar a tabela cursos:', e)

#criando tabela de turmas
try:
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        cur.execute(
            """ CREATE TABLE IF NOT EXISTS turmas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            curso_nome TEXT,
            data_inicio DATE,
            FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
            ) """
        )
        print('Tabela turmas criado com sucesso !')
except sqlite3.Error as e:
    print('Erro ao criar a tabela turmas:', e)

#criando tabela de alunos
try:
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        cur.execute(
            """ CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento DATE,
            cpf TEXT,
            turma_nome TEXT,
            FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
            ) """
        )
        print('Tabela alunos criado com sucesso !')
except sqlite3.Error as e:
    print('Erro ao criar a tabela alunos:', e)