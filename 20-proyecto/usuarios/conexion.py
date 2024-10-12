import mysql.connector

def conectar():
# Conectar a la base de datos
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="masterPython",
        port=3306
    )
    # Crear un cursor para ejecutar consultas en la base de datos
    cursor = database.cursor(buffered=True)
    
    return[database, cursor]