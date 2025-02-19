import sqlite3

#Crear las tablas que necesiteis brothers nico gay

conn = sqlite3.connect("viajes.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS cliente") 
cursor.execute("DROP TABLE IF EXISTS destino") 
cursor.execute("DROP TABLE IF EXISTS vuelo") 
cursor.execute("DROP TABLE IF EXISTS avion") 
cursor.execute("DROP TABLE IF EXISTS viaje") 

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
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS vuelo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        destino_id INTEGER NOT NULL,
        avion_id INTEGER NOT NULL,
        cantidad_asientos INTEGER NOT NULL,
        precio REAL NOT NULL,
        FOREIGN KEY (destino_id) REFERENCES destino(id) 
        FOREIGN KEY (avion_id) REFERENCES avion(id) 
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS avion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        modelo TEXT NOT NULL,
        categoria TEXT NOT NULL,
        porcentaje_precio REAL NOT NULL,
        capacidad_total INTEGER NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS viaje (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        vuelo_id INTEGER NOT NULL,
        fecha_salida TEXT NOT NULL,
        fecha_regreso TEXT NOT NULL,
        precio REAL NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES cliente(id),
        FOREIGN KEY (vuelo_id) REFERENCES vuelos(id)
    )
""")

cursor.execute("""
    INSERT INTO destino (nombre, precio) VALUES 
    ('España', 200),
    ('Italia', 250),
    ('Francia', 180);
""")

cursor.execute("""
    INSERT INTO avion (modelo, categoria, porcentaje_precio, capacidad_total) VALUES 
    ('Boeing 737', 'Económico', 1.2, 180),
    ('Airbus A320', 'Económico', 1.1, 160),
    ('Boeing 777', 'Premium', 1.5, 300);
""")

conn.commit()
conn.close()

