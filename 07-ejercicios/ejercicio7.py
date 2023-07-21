num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))


if num1 < num2:
    for printNumeros in range(num1, num2 + 1):
        if printNumeros%2 != 0:
            print(printNumeros)
else:
    print("El numero 1 debe ser menor al numero 2")