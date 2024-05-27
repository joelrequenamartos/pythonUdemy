"""
Ejercicio 4.
Crear un script con 4 variables.
Una lista, una string, un entero y un booleano.
Y que imprima un mensaje según el tipo de dato de cada variable.
"""



def variableChecker(variableName, variableType):
    checkType = type(variableName)
    
    if checkType == variableType:
        print(f"Correcto, la variable es un/a {variableType}")
    else:
        print(f"No, la variable no es un/a {variableType}")
        
print("Pruebas Lista")
print("-------------")
testList = ["Hola mundo", 2]
print(type(testList))
variableChecker(testList, list)
variableChecker(testList, bool)
print("\n")

print("Pruebas String")
print("-------------")
testStr = "nombre"
print(type(testStr))
variableChecker(testStr, str)
variableChecker(testStr, bool)
print("\n")

print("Pruebas Integer")
print("-------------")
testInt = 19
print(type(testInt))
variableChecker(testInt, bool)
variableChecker(testInt, int)
print("\n")

print("Pruebas Booleano")
print("-------------")
testBool = True
print(type(testBool))
variableChecker(testBool, bool)
variableChecker(testBool, list)

