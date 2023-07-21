"""
Variables globales vs Variables locales.

Variables Global: Se declaran fuera de una funcion, están disponibles dentro y fuera de ellas.

Variable Local: Se declaran dentro de una funcion y no se pueden usar fuera de ellas a no ser que se haga un return.

"""

frase = "keyboard enjoyer"

print(frase)

def holaMundo():
    frase = "Hola Mundo"       #toggle to see changes between global and local var
    print("dentro de la funcion")
    print(frase)
    year = 2023
    print(year)
    
    global personalWebsite
    personalWebsite = "joelrequena.com"
    print("Dentro: " + personalWebsite)
    return year
    
holaMundo()

print("Fuera: " + personalWebsite)
#print(year)