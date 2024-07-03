#Capturar excepciones y manejar errores en codigo susceptible a errores.
'''
try:
    nombre = input("Cual es tu nombre?: ")
    if len(nombre)>1:
        nombre_usuario = "Tu nombre es " + nombre

    print(nombre_usuario)
    
except:
    print("Ha ocurrido un error, mete bien el nombre.")

else:
    print("Se ha insertado un nombre correcto")
    
finally:
    print("Fin de la iteración")
    
'''

#Manejar varias excepciones.
'''
try:
    numero = int(input("Introduce un numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))
except TypeError:
    print("Error, no pueden multiplicarse cadenas")
except ValueError:
    print("Error, debes introducir un numero!")
except Exception as e:
    print("Ha ocurrido un error:", type(e).__name__)
    print(type(e))
'''
try:
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    edad = int(edad)

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenidx {nombre}!")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error: ", e)