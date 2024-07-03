from io import open
import pathlib
import shutil

# Abrir archivo
#archivo = open("fichero.txt", "a+")
ruta = str(pathlib.Path().absolute()) + "/fichero.txt"
archivo = open(ruta, "a+")

#Escribir en archivo
archivo.write("Soy un texto de prueba\n")

#Cerrar archivo.
archivo.close()


#--------
ruta = str(pathlib.Path().absolute()) + "/fichero.txt"
with open(ruta, "r") as archivoLectura:
        lista = archivoLectura.readlines()
archivoLectura.close()

for frase in lista:
    print("-" + frase.strip())

print("--------")
for frase2 in lista:
    lista_frase = frase.split()
    print(lista_frase)

#Copiar archivos
#Se le pasa una ruta a una variable y la ruta de destino a otra.
"""
rutaOriginal = str(pathlib.Path().absolute()) + "/fichero.txt"
rutaNueva = str(pathlib.Path().absolute()) + "/ficherocopiado.txt"
rutaAlternativa = "../01-holamundo/ficherocopiado.txt"

shutil.copyfile(rutaOriginal, rutaNueva)
shutil.copyfile(rutaOriginal, rutaAlternativa)
"""

#Mover archivos
"""
rutaOriginal = str(pathlib.Path().absolute()) + "/fichero.txt"
rutaDos = str(pathlib.Path().absolute()) + "/ficheroCopy_Nuevo.txt"
shutil.move(rutaOriginal, rutaDos)
"""

#Eliminar Archivos
import os

os.remove(str(pathlib.Path().absolute()) + "/ficherocopiado.txt")