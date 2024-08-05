import mysql.connector

# Conexion base de datos
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="masterPythonTest"
)

#print(database)

#Creación de cursor y base de datos
cursor = database.cursor(buffered=True)
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS masterPythonTest")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
#cursor.execute("USE masterPythonTest")
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(ID)
)  
""")


#Listamos e insertamos datos a las tablas
"""
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

#Lo comentamos para no estar insertando datos todo el rato.

#cursor.execute("INSERT INTO VEHICULOS VALUES(null, 'Ford', 'Fiesta', 20800)")

coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'C3', 2000),
    ('Merc', 'C3', 35000)
]

cursor.executemany("INSERT INTO vehiculos VALUES(null,%s, %s, %s)", coches)
"""
database.commit()

#Listamos e imprimimos todas las tablas
cursor.execute("SELECT * FROM vehiculos") #le podemos añadir el 'WHERE' o el 'AND'
result = cursor.fetchall()

print("Todos mis coches")
for coche in result :
    print(coche[1], coche[2], coche[3])
    # En vez de hacer un select de una sola tabla, podemos
    # seleccionar que numero de la tupla queremos imprimir 
    # haciendo = print(coche[1])


cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renault' ")
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Merc' ")

database.commit()
print(cursor.rowcount, "Borrados")

#Actualizar
cursor.execute("UPDATE vehiculos SET modelo='Leon' where marca='Seat'")
database.commit()
print(cursor.rowcount, "Actualizados")