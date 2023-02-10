import sqlite3

conn = sqlite3.connect('pessoas.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        idade INTEGER NOT NULL
    );
""")