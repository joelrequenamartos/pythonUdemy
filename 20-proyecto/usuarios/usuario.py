import hashlib
import usuarios.conexion as conexion
import mysql


connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        # Verificar si el correo electrónico ya está registrado
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (self.email,))
        if cursor.fetchone():
            print(f"Error: El correo '{self.email}' ya está registrado.")
            return [0, self]
        
        # Define la consulta SQL para insertar un nuevo usuario
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (%s, %s, %s, %s)"
        # Crear una tupla con los datos del usuario
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest())
        
        # Manejar errores
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]  # Indicar cuántas filas fueron afectadas
        except mysql.connector.errors.IntegrityError as e:
            if e.errno == 1062:  # Error por entrada duplicada
                print(f"Error: Entrada duplicada. El correo '{self.email}' ya está registrado.")
                result = [0, self]
            else:
                print(f"Error de integridad: {e}")
                result = [0, self]
        except mysql.connector.Error as e:
            print(f"Error en la conexión o ejecución: {e}")
            result = [0, self]
        except Exception as e:
            print(f"Error inesperado: {e}")
            result = [0, self]
        
        return result
        
    def identificar(self):
        #Consulta comprobar si existe usuario.
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        
        #Cifrado password
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        #Datos Consulta
        usuario = (self.email, cifrado.hexdigest())
        
        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        
        return result