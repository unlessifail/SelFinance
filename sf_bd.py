import sqlite3

conn = sqlite3.connect('financas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transacoes (
        transacao_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_ID INTEGER,
        desc_movimentacao TEXT,
        valor_movimentacao REAL,
        categ_movimentacao TEXT,
        data_movimentacao DATE,
        FOREIGN KEY (usuario_ID) REFERENCES usuarios (usuario_ID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_email TEXT,
        usuario_senha TEXT,
        usuario_nome TEXT,
        usuario_pic_path TEXT,
        usuario_saldo,
    )
''')

conn.commit()