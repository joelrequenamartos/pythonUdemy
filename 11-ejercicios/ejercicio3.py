"""
Ejercicio 3.
Programa que compruebe si una variable está vacía,
si está vacía rellenarla con un texto predeterminado,
y mostrarlo por pantalla en mayusculas
"""
test1 = "hola"
test2 = ""

def variableChecker(variableName):
    if len(variableName) <= 0:
        print("Variable vacía.")
        variableName = "esta variable ya no está vacía"
        print(variableName.upper())
        #capitalize te pone la primera letra en mayusculas
        #lower te las pone todas en minuscula y upper todas masc.
    else:
        print("Variable correcta")
        
variableChecker(test1)
variableChecker(test2)