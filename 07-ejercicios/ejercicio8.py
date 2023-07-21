"""
Calcular X por ciento de un numero introducido.
"""

numero = int(input("Introduce un numero: "))
porcentaje = int(input(f"Que porcentaje quieres sacar de {numero}?: "))

operacion = numero * (porcentaje / 100)
print(f"El {porcentaje}% de {numero} es: {operacion}")