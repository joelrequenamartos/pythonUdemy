"""
    # FOR
    for variable in elemento_iterable ( lista, rango, tupla, etc)
        bloque de instrucciones
"""

contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el " + str(contador))
    resultado += contador
    
print(f"El resultado es: {resultado}")

#Ejemplo con tablas de multiplicar.

print("")
print("----------------------")
numeroUsuario = int(input("¿De que número quieres la tabla?: "))
if numeroUsuario < 1:
    numeroUsuario = 1
    
    
print(f"#### Tabla de multiplicar del número {numeroUsuario} ####")

for numeroTabla in range(1,11):
        print(f"{numeroUsuario} x {numeroTabla} = {numeroTabla * numeroUsuario}")
else:
    print("Tabla finalizada")
    print("")
#no hace falta tener un if para poder poner un else en un for, no todos los lenguajes tiene eso.
    
for yamaha in range(1,8):
    print("tengo la yamaha R" + str(yamaha))