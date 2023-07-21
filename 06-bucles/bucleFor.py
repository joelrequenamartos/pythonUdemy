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
    if numeroUsuario == 33:
        print("Me repites ese numerín? jiji")
        print("")
        break
    print(f"{numeroUsuario} x {numeroTabla} = {numeroTabla * numeroUsuario}")
else:
    print("Tabla finalizada")
    print("")