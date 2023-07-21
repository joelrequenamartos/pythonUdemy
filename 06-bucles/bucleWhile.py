"""
Bucles while.


while condición:
    bloque instrucciones
    actualización contador
"""

contador = 1
while contador <= 100:
    print(f"Estoy en el numero {contador}")
    contador += 1
    
contador2 = 1
muestrame = str(0)
while contador2 <= 100:
    muestrame = muestrame + ", " + str(contador2)
    contador2 += 1
print (muestrame)

print("#### EJEMPLO ####")
numeroUsuario = int(input("¿De que número quieres la tabla?: "))

if numeroUsuario < 1:
    numeroUsuario = 1
    
print(f"Tabla del {numeroUsuario}")

contador3 = 1
while contador3 <= 10:
    print(f"{numeroUsuario} x {contador3} = {numeroUsuario * contador3}")
    contador3 += 1
else:
    print("Tabla terminada")