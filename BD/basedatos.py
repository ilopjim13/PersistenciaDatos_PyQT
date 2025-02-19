import sqlite3

#Crear las tablas que necesiteis brothers nico gay

conn = sqlite3.connect("viajes.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS destino (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS viaje (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        destino_id INTEGER NOT NULL,
        fecha_salida TEXT NOT NULL,
        fecha_regreso TEXT NOT NULL,
        precio REAL NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES cliente(id),
        FOREIGN KEY (destino_id) REFERENCES destino(id)
    )
""")

conn.commit()
conn.close()

