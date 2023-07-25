nombre = "Joel"

print(nombre)
print(type(nombre))

comprobar = isinstance(nombre, str)
if comprobar:
    print("Es un string")
else:
    print("No es un string")
    
if not isinstance(nombre, float):
    print("No es un numero con decimales")
    
frase = "          hola me llamo joel"
print(frase.strip())

year = 2023
print(year)

del year
#print(year)

texto = "Esternocle idomastoideo"
if len(texto) <= 0:
    print("la variable esta vacía")
else:
    print("la variable tiene contenido")
    print(len(texto))
    
print(texto.find("idomastoideo"))

nuevafrase = texto.replace("idomastoideo", "wtf")
print(nuevafrase)

print(str(nuevafrase.upper))
print(nuevafrase.upper)