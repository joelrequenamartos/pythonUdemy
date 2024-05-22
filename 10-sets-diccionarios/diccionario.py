"""
Los diccionarios son como listas, pero tienen un indice alfanumerico en vez de numerico.

Los diccionarios son un tipo de datos que almacenan un conjunto de datos
En formate clave > valor
Es parecido a un array asociativo / json.
"""

persona = {
    "nombre": "Joel",
    "apellidos": "Requena",
    "web": "joel.com"
}

print(persona)
print(type(persona))

print(persona["apellidos"])
print(persona["nombre"])

# Lista con Diccionarios

contactos = [
    {
        'nombre': 'Joel',
        'email': 'joel@mail.com',
    },
    {
        'nombre': 'Luis',
        'email': 'luis@mail.com',
    },
    {
        'nombre': 'Tapia',
        'email': 'tapia@mail.com',
    }
]

print(contactos)
print(contactos[2]['nombre']) 

print(contactos[0]['nombre']) 
contactos[0]['nombre'] = "Spiderman"
print(contactos[0]['nombre']) 

print("\n Listado")
for contacto in contactos:
    print(f"Nombre del contacto numero: {contacto['nombre']}")
    print(f"Apellido del contacto: {contacto['nombre']}")

