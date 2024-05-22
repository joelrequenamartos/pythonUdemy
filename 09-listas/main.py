"""
LISTAS / ARRAY
COLECCIONES DE DATOS BAJO UN UNICO NOMBRE
PODEMOS USAR UN INDICE NUMERICO PARA ACCEDER A ELLOS.
"""

pelicula = "batman"
print(pelicula)

peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
print(peliculas)
print(peliculas[0])
print(peliculas[1])
print(peliculas[2])
print(peliculas[1:]) #del indice 1 en adelante


#tupla de valores, no se pueden modificar.
cantantes = list(("Drake", "Bbno", "Manolo"))
print(cantantes)
print(cantantes[0])
print(cantantes[1])
print(cantantes[-1]) #el primero empezando por el final, orden invertido
print(cantantes[0:1]) #del indice 0 al 1
cantantes[2] = "McDalenas"
print(cantantes)

#years = list(range(2020,2050))
#print(years)

variada = ["Joel", 22, 1.75, False, "Texto"]
print(variada)

#añadir elemento a lista
cantantes.append("Pepito")
print(cantantes)

#Recorrer lista con un for
print("\n *****LISTADO PELICULAS*****")
for listadoPeliculas in peliculas:
    print(listadoPeliculas)
    #print(f"{listadoPeliculas.index} {listadoPeliculas}")
    
    
nuevaPelicula = ""
while nuevaPelicula != "parar":
    nuevaPelicula = input("Introduce una nueva pelicula: ") #le damos el valor mediante el input al nuevo valor de nuevaPelicula.
    
    if nuevaPelicula != "parar": #si no le ponemos esto, añadiría el "parar" tambien a la lista.
        peliculas.append(nuevaPelicula) #con el metodo append añadimos al final de la lista una nueva entrada.
    
    print(peliculas)

#listas multidimensionales, listas de listas.
print("-- Listado de contactos --")
contactos = [
    [
        'Antonio',
        'antonio@mail.com'
    ],
    [
        'Luis',
        'luis@mail.com'
    ],
    [
        'Salva',
        'salva@mail.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Mail: " + elemento)
    print("\n")
#print(contactos[1][0])