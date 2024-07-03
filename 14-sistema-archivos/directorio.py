import os

#Crear Carpetas
'''
if not os.path.isdir("./miCarpeta"):
    os.mkdir("./miCarpeta")
else:
    print("Ya existe la carpeta")
'''
    
#Eliminar Carpetas
#os.rmdir("./miCarpeta")

#Copiar / Eliminar (dentro del if jeje)
'''import shutil
rutaOriginal = "./miCarpeta"

if os.path.isdir("./miCarpetaRenombrada"):
    os.rmdir("./miCarpetaRenombrada")

rutaNueva = "./miCarpetaRenombrada"
shutil.copytree(rutaOriginal, rutaNueva)
'''

#Mostrar contenido de la carpeta
'''
contenido = os.listdir("./miCarpeta")
print(contenido) #te lo imprime como una lista

for fichero in contenido:
    print("Fichero: " + fichero)
'''