import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    
    # Método para registrar un nuevo usuario
    def registro(self):
        print("\nOk! Vamos a registrarte en el sistema.")
    
        # Solicita información al usuario para el registro
        nombre = input("¿Cuál es tu nombre?: ")
        apellidos = input("¿Cuáles son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu nueva contraseña: ")
        
        # Crea una instancia de la clase Usuario con los datos proporcionados
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        
        # Llama al método registrar de la clase Usuario
        registro = usuario.registrar()
        
        # Verifica si el registro fue exitoso
        if registro[0] >= 1:
            print(f"\nPerfecto, {registro[1].nombre} te has registrado correctamente.")
        else:
            print("No te has registrado bien!")
        
    # Método para iniciar sesión en el sistema
    def login(self):
        print("¡Identifícate en el sistema!")
        
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            
            # Asegúrate de que login no es None y que tiene al menos 4 elementos
            if login and len(login) >= 4 and email == login[3]:
                print(f"Bienvenido {login[1]}, te has loggeado correctamente.")
                self.proximasAcciones(login)
            else:
                print("Email o contraseña incorrectos.")
        except Exception as e:
            # Puedes descomentar las siguientes líneas para obtener más detalles del error
            #print(type(e))
            #print(type(e).__name__)
            print("Login Incorrecto.")
    
    # Método para mostrar las próximas acciones
    def proximasAcciones(self, usuario):
        print("""
              Acciones disponibles:
              - Crear Notas
              - Mostrar Notas
              - Eliminar Notas
              - Salir
        """)
        
        accion = input("¿Qué quieres hacer? ")
        hazEl = notas.acciones.Acciones()
        
        if accion == "crear":
            print("Vamos a crear una nota.")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
            
        elif accion == "mostrar":
            print("Vamos a mostrar las notas.")
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            print("Vamos a eliminar una nota.")
            self.proximasAcciones(usuario)
            
        elif accion == "salir":
            print("Chau")
            exit()
