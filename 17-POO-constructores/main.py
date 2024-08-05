from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", "110", "70", "4")
carro1 = Coche("Rojo", "Seat", "Panda", "120", "80", "4")
carro2 = Coche("Verde", "Citroen", "Xsara", "130", "90", "4")
carro3 = Coche("Azul", "Mercedes", "Clase A", "350", "400", "4")


print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar Tipado
#carro3 = "prueba"
if type(carro3) == Coche:
    print("es correcto")
else:
    print("no es correcto")
    
# Visibilidad
print(carro.soyPublico)
print(carro.getPrivado())