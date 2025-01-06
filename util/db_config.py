import sqlite3

def create_db():
    """Crea la base de datos si no existe."""
    conn = sqlite3.connect('resultados.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resultados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            resultado TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def result_test(name, result):
    conn = sqlite3.connect('resultados.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO resultados (nombre, resultado)
        VALUES (?, ?)
    ''', (name, result))
    
    conn.commit()
    conn.close()