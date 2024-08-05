import sqlite3

# Conexión 
conexion = sqlite3.connect('./19-bbdd/pruebas.db')

# Creación cursor sql
cursor = conexion.cursor()

#cursor.execute("DROP TABLE IF EXISTS productos")

# Creación tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo varchar(255),
    Descripcion text,
    precio int(255)
);
""")


# Guardar Cambios
conexion.commit()

# Insertar Datos
"""
cursor.execute("INSERT INTO productos VALUES(null, 'producotoUno', 'descProducto', 10)")
conexion.commit()
"""
# Listar Datos
cursor.execute("Select * FROM productos;")
productos = cursor.fetchall()

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()


# Insertar muchos registros de golpe IMPORTANTE

productos = [
    ("Ordenador", "Buen pc", 700),
    ("Telefono", "Buen telefono", 140),
    ("Placa Base", "Segunda Mano", 80),
    ("Tablet", "Buena tablet", 250)
]

cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)
conexion.commit()

# Actualizar un valor
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

# Listar Datos
cursor.execute("Select * FROM productos;")
productos = cursor.fetchall()


for producto in productos:
    print(producto)
    

# Cerrar conexión
conexion.close()