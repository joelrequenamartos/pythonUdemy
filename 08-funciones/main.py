"""
Funciones
Una funcion es conjunto de instrucciones agrupadas bajo un mismo nombre que
pueden reutilizarse invocando a la funcion tantas veces como haga falta

def nomnbreFuncion(parametros):
    conjunto de instrucciones
    
nomnbreFuncion(parametro1)
nomnbreFuncion(parametro2)
"""
print("##### Ejemplo 1 #####")

def muestraNombre():
    print("Joel")
    print("Pol")
    print("Angela")
    print("Paco")
    print("")
#Invocar funcion
muestraNombre()


print("##### Ejemplo 2 #####")

def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es {nombre}")
    
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarTuNombre(nombre, edad)

print("\n")
print("##### Ejemplo 3 #####")

def tabla(numero):
    print(f"Tabla de multiplicar del número: {numero}.")
    
    for contador in range (11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    
    print("\n")
    
tabla(12)

print("---------------------")
for numTabla in range (1, 11):
    tabla(numTabla)
    
print("\n")
print("##### Ejemplo 4 #####")

#parametros opcionales

def getEmpleado (nombre, dni = None):
    print("Empleado.")
    print(f"Nombre: {nombre}")
    
    if dni != None:
        print("Identificacion.")
        print(f"DNI: {dni}")
    
    
getEmpleado("Joel")


print("\n")
print("##### Ejemplo 5 #####")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    
    return saludo

print(saludame("Joel"))

print("\n")
print("##### Ejemplo 6 #####")

def calculadora (numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    divi = numero1 / numero2
    
    cadena = ""
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multi: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(divi)
    
    return cadena
    
print(calculadora(2,3))
print("")
print(calculadora(5,5, True))
print("")
print(calculadora(2,9, False))

print("\n")
print("##### Ejemplo 7 #####")

def getNombre(nombre):
    texto =f"El nombre es {nombre}"
    return texto

def getApellido(apellido):
    texto =f"Los apellidos son {apellido}"
    return texto

print(getNombre("Joel"), getApellido("Requena Martos"))

def getAll(nombre, apellido):
    texto =getNombre(nombre) + " " + getApellido(apellido)
    return texto
    
print(getAll("Joel", "Requena Martos"))

print("\n")
print("##### Ejemplo 8 #####")
#Funciones Lambda, funciones anonimas.

dimeElYear = lambda year: f"El año es {year}"
print(dimeElYear(1234))

dimeElYear2 = lambda year: f"El año es {year * 2}"
print(dimeElYear2(1234))
