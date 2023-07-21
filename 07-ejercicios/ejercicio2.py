"""
Ejercicio 2
Escribir un script que nos muestre por pantalla todos los numeros pares del 1 al 120
"""

numero = 0

for numero in range (1,121):
    if numero % 2 == 0:
        print(f"El numero {numero}.")