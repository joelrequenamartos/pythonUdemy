#ejemplo 1
print("##### EJEMPLO 1 #####")

color = input("Adivina cual es mi color favorito: ")

if color == "amarillo":
    print("Nice")
    print("El color es amarillo")
else:
    print(f"Mi color favorito no es el {color}")
    
print("\n---------------------------------------")

#ejemplo 2
print("##### EJEMPLO 2 #####")
year = int(input("En que año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")
    
    
print("\n---------------------------------------")

#ejemplo 3
print("##### EJEMPLO 3 #####")
nombre = "Joel Requena"
ciudad = "Sabadell"
continente = "Europa"
edad = "18"
mayoriaEdad = "18"

if edad >= mayoriaEdad:
    print(f"{nombre} es mayor de edad")
    
    if continente != "Europa":
        print(f"{nombre} no es Europeo")
    else:
        print(f"{nombre} es Europeo y de la ciudad de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")
    

print("\n---------------------------------------")

#ejemplo 4
print("##### EJEMPLO 4 #####")

dia = int(input("Introduce el día de la semana: "))
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es Martes")
    else:
        if dia == 3:
            print("Es Miercoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    print("Es Finde")"""
                    

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia >= 8:
    print("No hay tantos dias en la semana")
else:
    print("Es fin de semana")
    
    
print("\n---------------------------------------")

#ejemplo 5
print("##### EJEMPLO 6 #####")
edadMinima = 18
edadMaxima = 65
edadOficial = int(input("¿Que edad tienes "))

if edadOficial >= edadMinima and edadOficial <= edadMaxima:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")
    
    """
    Operadores logicos
    and Y
    or O
    "! negación
    not NO
    """
    
print("\n---------------------------------------")

#ejemplo 6
print("##### EJEMPLO 6 #####")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana")
else:
    print(f"El pais {pais} no es de habla hispana")
    
    

print("\n---------------------------------------")

#ejemplo 7
print("##### EJEMPLO 7 #####")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es país de habla hispana")
else:
    print(f"El pais {pais} es de habla hispana")
    
    print("\n---------------------------------------")

#ejemplo 8
print("##### EJEMPLO 8 #####")

pais = "España"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es país de habla hispana")
else:
    print(f"El pais {pais} es de habla hispana")
    

