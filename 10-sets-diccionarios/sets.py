"""
Set es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden.
"""

personas = {
    "Victor", "Manolo", "Fran"
}

print(type(personas))
print(personas)

personas.add("Joel")
print(personas)

personas.remove("Victor")
print(personas)