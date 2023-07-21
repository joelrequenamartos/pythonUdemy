"""
Hacer un programa que muestre todos los numeros
entre dos numeros que diga el usuario
"""

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))


if num1 < num2 :
    for printNumeros in range(num1, num2 + 1):
        print(printNumeros)
else:
    print("El numero 1 debe ser menor al numero 2")

    