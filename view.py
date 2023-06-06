import sqlite3 as lite

#criando conexao
try:
    con_ban_dados = lite.connect('cadastro.db')
    print('Conexão com banco de dados realizado com sucesso !')
except sqlite3.Error as e:
    print('Erro ao conectar com banco de dados:', e)

#trabalhando com tabela de cursos ----------------------------

#criar cursos(CREATE C) Crud
def criar_cursos(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)'
        cur.execute(query,i)

#criar_cursos(['Python', 'Semanas', 50])

# ver todos os cursos (READ R) cRud
def ver_cursos():
    lista = []
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    
    return lista
#print(ver_cursos())

#Atualizar os cursos(update U) crUd
def atualizar_cursos(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?'
        cur.execute(query,i)

l = ['Python', 'Duas Semanas', 50, 1]
#atualizar_cursos(l)

# Deletar os cursos(Delete D) cruD
def deletar_cursos(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'DELETE FROM Cursos WHERE id=?'
        cur.execute(query,i)
    
#deletar_cursos([1])

#trabalhando com tabela de turmas ----------------------------

# Criar turmas (Inserir) Crud
def criar_turmas(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'INSERT INTO Turmas (nome, cursos_nome, data_inicio) VALUES (?, ?, ?)'
        cur.execute(query, i)

# ver todos as turmas (READ R) cRud
def ver_turmas():
    lista = []
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        cur.execute('SELECT * FROM Turmas')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    
    return lista

# Atualizar Turmas(update U) crUd
def atualizar_turma(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'UPDATE Turma SET nome=?, cursos_nome=?, data_inicio=? WHERE id=?'
        cur.execute(query,i)

# Deletar Turmas(Delete D) cruD
def deletar_turma(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'DELETE FROM Turmas WHERE id=?'
        cur.execute(query,i)


#trabalhando com tabela de alunos ----------------------------

# Criar Alunos (Inserir) Crud
def criar_alunos(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        cur.execute(query, i)

# ver alunos (READ R) cRud
def ver_alunos():
    lista = []
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    
    return lista

# Atualizar alunos(update U) crUd
def atualizar_aluno(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'UPDATE Turma SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?'
        cur.execute(query,i)

# Deletar aluno(Delete D) cruD
def deletar_aluno(i):
    with con_ban_dados:
        cur = con_ban_dados.cursor()
        query = 'DELETE FROM Alunos WHERE id=?'
        cur.execute(query,i)