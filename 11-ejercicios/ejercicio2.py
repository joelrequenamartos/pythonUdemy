"""
Ejercicio 2.
Escribir un programa que añada valores a una lista mientras
que su longitud sea menor a 120 y luego mostrar la lista
"""

numeracion = []

for numeros in range(0,121):
    numeracion.append(f"indice numero: {numeros}")
    print(numeracion[numeros])