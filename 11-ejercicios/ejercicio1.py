"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:

 - Recorrer la lista y mostrarla
    - En una función. Que recorra listas y devuelva un string
 - Ordenarla y mostrarla
 - Mostrar su longitud
 - Mostrar un elemento que pida el usuario
"""


#--------------------------
#Funcion que recorre listas y devuelve un string
numeros = [1,2,6,7,9,4]
nombres = ["Joel", "Requena", "Martos"]
recorrer = ""

def recorreListas(nombreLista):
    for recorrer in nombreLista:
        print(str(recorrer))
    
recorreListas(numeros)
recorreListas(nombres)


#--------------------------
#Ordenar y mostrar la lista

numeros.sort()
print(numeros)

nombres.sort()
print(nombres)

#--------------------------
#Mostrar la longitud de la lista
print("La longitud de la lista es de " + str(len(numeros)) + " elementos.")

#--------------------------

#Mostrar un elemento que pida el usuario
numeroUsuario = input("Elige un indice le cual mostrar: ")
print(numeros[int(numeroUsuario)])