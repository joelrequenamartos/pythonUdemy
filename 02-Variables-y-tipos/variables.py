texto = "Master en Python!"
texto2 = " con Joel Requena"

print(texto + texto2)


numero = 74
decimal = 3.3

print (numero)
print (decimal)
print ( numero + decimal )
print("---")

decimal = 8.8
print (numero)
print (decimal)
print ( numero + decimal )

#Concatenación

nombre = "Joel"
apellidos = "Requena"
web = "joelrequenamartos.es"

print (nombre + " " + apellidos + " - " + web)
print (f"{nombre} {apellidos} - {web}") #mejor opción maybe
print ("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))

print(nombre, apellidos, web) #esto no es concatenar, es listar variables