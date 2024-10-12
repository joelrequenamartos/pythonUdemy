"""
Proyecto Python y Mysql
- Abrir Asistente
- Login o registro
- Si elegimos registro, creará un usuario en la base de datos
- Si elegimos login, identifica al usuario y nos preguntará:
 - Crear nota, mostrar nota, borrar nota, etc.
"""

from usuarios import acciones

print("""
      Acciones disponibles:
        - Registro
        - Login
""")

hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()